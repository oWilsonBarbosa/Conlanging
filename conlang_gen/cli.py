"""Command-line interface for the syllable/word generator."""

from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

from .generate import Word, generate_words
from .inventory import TEMPLATE_INVENTORY, Inventory
from .real_language import build_inventory_from_language
from .reference_data import (
    ReferenceDataError,
    search_bdproto_languages,
    search_phoible_languages,
)
from .stats import NaturalismReport, analyze


def _print_words(words: list[Word], columns: int = 6) -> None:
    texts = [w.text for w in words]
    width = max((len(t) for t in texts), default=0)
    for i in range(0, len(texts), columns):
        row = texts[i : i + columns]
        print("  ".join(t.ljust(width) for t in row))


def _print_naturalism_report(report: NaturalismReport) -> None:
    print()
    print(f"Words generated:          {report.num_words}")
    print(f"Avg syllables per word:   {report.avg_syllables_per_word:.2f}")
    if report.consonant_vowel_ratio is not None:
        print(f"Consonant/vowel ratio:    {report.consonant_vowel_ratio:.2f}")
    if report.onset_clusters_checked:
        print(
            f"Onset clusters attested:  {report.onset_clusters_attested}/{report.onset_clusters_checked} "
            f"({report.onset_legality_rate:.0%})"
        )
    if report.coda_clusters_checked:
        print(
            f"Coda clusters attested:   {report.coda_clusters_attested}/{report.coda_clusters_checked} "
            f"({report.coda_legality_rate:.0%})"
        )
    if not report.onset_clusters_checked and not report.coda_clusters_checked:
        print("No consonant clusters were generated (or no real cluster data to check against).")


def cmd_generate(args: argparse.Namespace) -> int:
    try:
        inventory = Inventory.load(args.inventory)
    except (FileNotFoundError, ValueError, KeyError) as exc:
        print(f"error: could not load inventory {args.inventory!r}: {exc}", file=sys.stderr)
        return 1

    rng = random.Random(args.seed)
    words = generate_words(inventory, args.count, rng=rng, unique=not args.allow_repeats)
    print(f"{inventory.name} ({len(inventory.consonants)}C / {len(inventory.vowels)}V):")
    _print_words(words)
    return 0


def cmd_new_inventory(args: argparse.Namespace) -> int:
    path = Path(args.output)
    if path.exists() and not args.force:
        print(f"error: {path} already exists (use --force to overwrite)", file=sys.stderr)
        return 1
    inventory = Inventory.from_dict(TEMPLATE_INVENTORY)
    inventory.save(path)
    print(f"Wrote template inventory to {path}. Edit its consonants/vowels/syllable_patterns, then run:")
    print(f"  python -m conlang_gen generate --inventory {path}")
    return 0


def cmd_search_language(args: argparse.Namespace) -> int:
    search = search_phoible_languages if args.source == "phoible" else search_bdproto_languages
    matches = search(args.query, limit=args.limit)
    if not matches:
        print(f"No {args.source.upper()} languages match {args.query!r}.")
        return 1
    for name in matches:
        print(name)
    return 0


def cmd_from_language(args: argparse.Namespace) -> int:
    try:
        result = build_inventory_from_language(
            args.language, source=args.source, inventory_id=args.inventory_id
        )
    except ReferenceDataError as exc:
        print(f"error: {exc}", file=sys.stderr)
        search = search_phoible_languages if args.source == "phoible" else search_bdproto_languages
        suggestions = search(args.language, limit=10)
        if suggestions:
            print("Did you mean one of:", file=sys.stderr)
            for name in suggestions:
                print(f"  {name}", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    real = result.real_inventory
    print(f"{real.language_name} [{real.source}] (Glottocode: {real.glottocode or 'unknown'})")
    if real.inventory_id is not None:
        print(f"  Inventory ID: {real.inventory_id}", end="")
        if real.other_inventory_ids:
            print(
                f"  (other sources available: {', '.join(real.other_inventory_ids)}"
                " -- pick with --inventory-id)"
            )
        else:
            print()
    print(f"  Consonants ({len(real.consonants)}): {' '.join(real.consonants)}")
    print(f"  Vowels ({len(real.vowels)}): {' '.join(real.vowels)}")
    if real.unclassified:
        print(f"  Unclassified phonemes (excluded): {' '.join(real.unclassified)}")
    if result.cluster_profile is not None:
        print(
            f"  Matched Phonotacticon data: {len(result.cluster_profile.onsets)} onset shapes, "
            f"{len(result.cluster_profile.codas)} coda shapes attested."
        )
    else:
        print("  No Phonotacticon match found for this language -- using generic syllable shapes.")
    print()

    rng = random.Random(args.seed)
    words = generate_words(result.inventory, args.count, rng=rng, unique=not args.allow_repeats)
    _print_words(words)

    if args.save_inventory:
        result.inventory.save(args.save_inventory)
        print(f"\nSaved inventory to {args.save_inventory}")

    if not args.no_stats:
        report = analyze(words, result.cluster_profile)
        _print_naturalism_report(report)

    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m conlang_gen",
        description="Random syllable and word generator for conlangs, with real-language phonology data.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_generate = subparsers.add_parser("generate", help="Generate words from a custom inventory file.")
    p_generate.add_argument("--inventory", required=True, help="Path to an inventory JSON file.")
    p_generate.add_argument("--count", type=int, default=20, help="Number of words to generate.")
    p_generate.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility.")
    p_generate.add_argument(
        "--allow-repeats", action="store_true", help="Allow duplicate words in the output."
    )
    p_generate.set_defaults(func=cmd_generate)

    p_new = subparsers.add_parser("new-inventory", help="Write a template inventory JSON file to edit.")
    p_new.add_argument("--output", default="inventories/my_conlang.json", help="Output path.")
    p_new.add_argument("--force", action="store_true", help="Overwrite an existing file.")
    p_new.set_defaults(func=cmd_new_inventory)

    p_search = subparsers.add_parser(
        "search-language", help="Search PHOIBLE or BDPROTO for language names (for use with from-language)."
    )
    p_search.add_argument("query", help="Substring to search for, e.g. 'Hawaiian' or 'Proto'.")
    p_search.add_argument(
        "--source",
        choices=["phoible", "bdproto"],
        default="phoible",
        help="Which database to search (default: phoible, ~2,700 living/historical languages).",
    )
    p_search.add_argument("--limit", type=int, default=25)
    p_search.set_defaults(func=cmd_search_language)

    p_real = subparsers.add_parser(
        "from-language",
        help="Generate words using a real phoneme inventory, and score naturalism.",
    )
    p_real.add_argument("language", help="Exact language name, e.g. 'Hawaiian'.")
    p_real.add_argument(
        "--source",
        choices=["phoible", "bdproto"],
        default="phoible",
        help="phoible (default): ~2,700 living/historical languages. "
        "bdproto: ~800 languages, mostly reconstructed proto-languages.",
    )
    p_real.add_argument(
        "--inventory-id",
        default=None,
        help="Disambiguate between PHOIBLE's multiple source inventories for one language name.",
    )
    p_real.add_argument("--count", type=int, default=20, help="Number of words to generate.")
    p_real.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility.")
    p_real.add_argument(
        "--allow-repeats", action="store_true", help="Allow duplicate words in the output."
    )
    p_real.add_argument(
        "--save-inventory", default=None, help="Also save the derived inventory to this JSON path."
    )
    p_real.add_argument(
        "--no-stats", action="store_true", help="Skip the naturalism report."
    )
    p_real.set_defaults(func=cmd_from_language)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)
