#!/usr/bin/env python3
"""Check a draft phonological inventory against cross-linguistic data.

Reports, for an inventory you supply:

  1. how typologically common each segment is (PHOIBLE, 2,176 languages)
  2. implicational violations -- marked segments whose usual unmarked partner
     you left out
  3. inventory size and consonant/vowel balance against the attested range
  4. optionally, attested allophony rules for your segments (PBase)

None of this tells you your conlang is wrong. Real inventories are lopsided and
a perfectly symmetric chart is the main thing that reads as artificial. Treat
every flag as "here is what you are departing from", not as an error.

Usage:
    python3 analysis/inventory_check.py analysis/examples/starter.txt
    python3 analysis/inventory_check.py my_lang.txt --allophony
    python3 analysis/inventory_check.py my_lang.txt --json > report.json
"""

import argparse
import json
import sys

from phoible_db import (
    adds_features,
    Phoible,
    clts_names,
    counterpart_distance,
    norm,
    pbase_rules,
    read_inventory,
)

TIERS = [
    (0.60, "core", "in the majority of languages"),
    (0.30, "common", "widespread"),
    (0.10, "uncommon", "a real choice, not a default"),
    (0.01, "rare", "marked; expect it to need support"),
    (0.0, "very rare", "fewer than 1 in 100 languages"),
]

# Present in >=60% of languages. Absence is not an error -- WALS 18A finds
# languages with no fricatives at all, no nasals, and no bilabials -- but it is
# worth doing on purpose rather than by accident.
CORE_SEGMENTS = "m i k j u a p w n t l s ŋ e b o".split()


def tier_of(frequency):
    for threshold, label, gloss in TIERS:
        if frequency >= threshold:
            return label, gloss
    return "very rare", ""


def percentile(sorted_values, value):
    below = sum(1 for v in sorted_values if v < value)
    return 100.0 * below / len(sorted_values)


def report_frequency(db, names, inventory):
    rows = []
    for segment in inventory:
        frequency = db.frequency(segment)
        label, _ = tier_of(frequency)
        if db.counts.get(segment, 0) == 0:
            label = "unattested"
        rows.append(
            {
                "segment": segment,
                "name": names.get(segment, ""),
                "languages": db.counts.get(segment, 0),
                "frequency": frequency,
                "tier": label,
            }
        )
    rows.sort(key=lambda r: -r["frequency"])
    return rows


def report_implications(db, names, inventory, args):
    """Split implication violations into counterpart gaps and co-occurrence.

    A counterpart gap is the interesting kind: you have the marked member of a
    pair (/z/, /ẽ/, /ɭ/) without its unmarked partner. Plain co-occurrence
    ("languages with /ɳ/ tend to have /l/") is true but is mostly telling you
    that your draft is small, so it is reported separately.

    Everything must clear the lift bar -- P(B|A) beating B's base rate -- or
    the report fills up with "your inventory implies /m/". The one exemption is
    for pairs where A is B plus an added feature (/ẽ/ over /e/, /iː/ over /i/).
    There the implication is real however common B is, and a lift bar would
    throw it away: /ĩ/ implies /i/ without a single exception, yet /i/ is so
    near-universal that the lift is only 6 points.
    """
    held = set(inventory)
    counterparts, co_occurrence = [], []
    for segment in inventory:
        for implied, conditional, lift, n_source, exceptions in db.implications(
            segment,
            min_conditional=args.min_conditional,
            min_languages=args.min_languages,
        ):
            if implied in held:
                continue
            distance = counterpart_distance(names.get(segment), names.get(implied))
            is_counterpart = (
                distance is not None and distance <= args.max_feature_distance
            )
            exempt = adds_features(names.get(segment), names.get(implied))
            if lift < args.min_lift and not exempt:
                continue
            record = {
                "have": segment,
                "missing": implied,
                "conditional": conditional,
                "lift": lift,
                "languages_with_source": n_source,
                "attested_exceptions": exceptions,
                "feature_distance": distance,
            }
            (counterparts if is_counterpart else co_occurrence).append(record)
    counterparts.sort(key=lambda v: -v["conditional"])
    co_occurrence.sort(key=lambda v: -v["conditional"])
    return counterparts, co_occurrence


def report_shape(db, inventory):
    consonants = [s for s in inventory if db.seg_class.get(s) == "consonant"]
    vowels = [s for s in inventory if db.seg_class.get(s) == "vowel"]
    tones = [s for s in inventory if db.seg_class.get(s) == "tone"]
    unknown = [s for s in inventory if s not in db.seg_class]

    sizes = db.sizes()
    return {
        "size": len(inventory),
        "size_percentile": percentile(sizes, len(inventory)),
        "attested_range": [sizes[0], sizes[-1]],
        "attested_median": sizes[len(sizes) // 2],
        "consonants": len(consonants),
        "vowels": len(vowels),
        "tones": len(tones),
        "unclassified": unknown,
        "cv_ratio": (len(consonants) / len(vowels)) if vowels else None,
        "missing_core": [s for s in map(norm, CORE_SEGMENTS) if s not in set(inventory)],
    }


def print_text_report(db, names, inventory, freq_rows, violations, shape, allophony,
                      show_co_occurrence=False):
    print(f"Inventory: {len(inventory)} segments")
    print(f"Reference: PHOIBLE, {db.n} languages (one inventory per Glottocode)")
    print()

    print("=" * 72)
    print("1. CROSS-LINGUISTIC FREQUENCY")
    print("=" * 72)
    print(f"{'seg':<8} {'langs':>6} {'freq':>7}  {'tier':<11} name")
    print("-" * 72)
    for row in freq_rows:
        print(
            f"{row['segment']:<8} {row['languages']:>6} "
            f"{row['frequency'] * 100:>6.1f}%  {row['tier']:<11} {row['name'][:34]}"
        )

    counterparts, co_occurrence = violations

    print()
    print("=" * 72)
    print("2. IMPLICATIONAL CHECK")
    print("=" * 72)

    def table(rows):
        print(f"{'have':<8} {'missing':<8} {'P(B|A)':>8} {'n(A)':>6} {'exceptions':>11}")
        print("-" * 72)
        for v in rows:
            print(
                f"{v['have']:<8} {v['missing']:<8} "
                f"{v['conditional'] * 100:>7.1f}% {v['languages_with_source']:>6} "
                f"{v['attested_exceptions']:>11}"
            )

    if not counterparts:
        print("No counterpart gaps. Every marked segment has its unmarked partner.")
    else:
        print("Counterpart gaps -- you have the marked member of a pair without")
        print("the unmarked one. These are the ones worth a decision.")
        print()
        table(counterparts)
        print()
        print("'exceptions' counts real languages that do exactly what you are")
        print("doing. A high count means you are in decent company.")

    if co_occurrence:
        print()
        print(
            f"Also {len(co_occurrence)} plain co-occurrence tendencies "
            "(segments that pattern"
        )
        print("together without being counterparts).", end=" ")
        if show_co_occurrence:
            print()
            print()
            table(co_occurrence)
        else:
            print("Pass --all-implications to see them.")

    print()
    print("=" * 72)
    print("3. SHAPE")
    print("=" * 72)
    print(
        f"size {shape['size']} segments "
        f"({shape['size_percentile']:.0f}th percentile; "
        f"attested {shape['attested_range'][0]}-{shape['attested_range'][1]}, "
        f"median {shape['attested_median']})"
    )
    print(f"consonants {shape['consonants']}   vowels {shape['vowels']}", end="")
    if shape["tones"]:
        print(f"   tones {shape['tones']}", end="")
    if shape["cv_ratio"]:
        print(f"   C/V ratio {shape['cv_ratio']:.1f}")
    else:
        print()
    if shape["unclassified"]:
        print(
            "unclassified (not in PHOIBLE, so excluded from the C/V count): "
            + " ".join(shape["unclassified"])
        )
    if shape["missing_core"]:
        print()
        print("core segments (>=60% of languages) you do not have:")
        print("  " + " ".join(shape["missing_core"]))
        print("  Gaps are fine and often good -- just make them deliberate.")

    if allophony:
        print()
        print("=" * 72)
        print("4. ATTESTED ALLOPHONY (PBase, 306 languages)")
        print("=" * 72)
        for segment, rules in allophony.items():
            if not rules:
                continue
            print(f"\n/{segment}/ -- {len(rules)} distinct attested rules, showing 5:")
            for language, output, environment, description in rules[:5]:
                # PBase writes the target segment as 'X' in its descriptions.
                # Only the first X is the rule's target; later ones can mean
                # other things, so leave those as written.
                detail = description.replace("X", f"/{segment}/", 1)
                where = f" {environment}" if environment else ""
                print(f"  {language[:20]:<20} -> {output:<8}{where}  {detail[:42]}")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Check a draft phonological inventory against PHOIBLE, CLTS and PBase.",
    )
    parser.add_argument("inventory", help="file with one segment per line")
    parser.add_argument(
        "--allophony",
        action="store_true",
        help="look up attested allophony rules in PBase (slower)",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON instead of text")
    parser.add_argument(
        "--min-conditional",
        type=float,
        default=0.90,
        help="P(B|A) needed to call something an implication (default 0.90)",
    )
    parser.add_argument(
        "--min-lift",
        type=float,
        default=0.10,
        help="how far P(B|A) must beat the base rate of B, to suppress trivia "
        "such as 'everything implies /m/' (default 0.10)",
    )
    parser.add_argument(
        "--min-languages",
        type=int,
        default=25,
        help="ignore implications from segments attested in fewer languages "
        "than this (default 25)",
    )
    parser.add_argument(
        "--max-feature-distance",
        type=int,
        default=2,
        help="CLTS feature-word distance below which two segments count as a "
        "markedness counterpart rather than mere co-occurrence (default 2)",
    )
    parser.add_argument(
        "--all-implications",
        action="store_true",
        help="also print plain co-occurrence tendencies, not just counterparts",
    )
    parser.add_argument(
        "--no-cache", action="store_true", help="re-parse PHOIBLE from the zip"
    )
    args = parser.parse_args(argv)

    inventory = read_inventory(args.inventory)
    if not inventory:
        raise SystemExit("inventory file is empty")

    db = Phoible.load(use_cache=not args.no_cache)
    names = clts_names()

    freq_rows = report_frequency(db, names, inventory)
    counterparts, co_occurrence = report_implications(db, names, inventory, args)
    shape = report_shape(db, inventory)
    allophony = pbase_rules(inventory) if args.allophony else None

    if args.json:
        json.dump(
            {
                "reference_languages": db.n,
                "frequency": freq_rows,
                "counterpart_gaps": counterparts,
                "co_occurrence_gaps": co_occurrence,
                "shape": shape,
                "allophony": allophony,
            },
            sys.stdout,
            ensure_ascii=False,
            indent=2,
        )
        print()
    else:
        print_text_report(
            db,
            names,
            inventory,
            freq_rows,
            (counterparts, co_occurrence),
            shape,
            allophony,
            show_co_occurrence=args.all_implications,
        )


if __name__ == "__main__":
    main()
