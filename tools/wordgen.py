#!/usr/bin/env python3
"""Generate Proto-Sevelian roots that obey the phonotactics in data/phonology.json.

Roots follow the canon C1(R)e(R)C2 (proto/02-phonotactics.md). Use this to
stress-test the phonotactics and audition the language's sound before
committing roots to the lexicon.

Examples:
    python3 tools/wordgen.py -n 20
    python3 tools/wordgen.py -n 10 --grade zero
    python3 tools/wordgen.py -n 5 --all-grades --seed 7
"""

import argparse
import json
import random
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "phonology.json"

GRADES = ("e", "o", "zero", "e-long", "o-long")
GRADE_VOWEL = {"e": "e", "o": "o", "e-long": "ē", "o-long": "ō"}


class Inventory:
    def __init__(self, data):
        cons = data["consonants"]
        self.resonants = list(cons["resonants"])
        self.voiced_stops = set(cons["stops"]["voiced"])
        self.consonants = (
            cons["stops"]["voiceless"]
            + cons["stops"]["voiced"]
            + cons["stops"]["aspirated"]
            + cons["laryngeals"]
            + cons["fricatives"]
            + self.resonants
        )
        weights = data["weights"]
        self.weights = [weights.get(c, 1.0) for c in self.consonants]
        self.syllabic = data["syllabic_resonants"]
        self.p_onset_r = data["root"]["onset_resonant_probability"]
        self.p_coda_r = data["root"]["coda_resonant_probability"]

    def pick_consonant(self, rng):
        return rng.choices(self.consonants, weights=self.weights, k=1)[0]

    def pick_resonant(self, rng):
        return rng.choice(self.resonants)


def legal(inv, c1, onset_r, coda_r, c2):
    if c1 == c2:
        return False
    if len({c1, c2} & inv.voiced_stops) == 2:
        return False
    if onset_r and c1 in inv.resonants:
        return False
    # rule 5: no identical resonant on both sides of the root vowel
    pre_vowel = {onset_r, c1 if c1 in inv.resonants else None} - {None}
    post_vowel = {coda_r, c2 if c2 in inv.resonants else None} - {None}
    if pre_vowel & post_vowel:
        return False
    # resonant C2 next to a coda resonant would make an illegal RR cluster
    if coda_r and c2 in inv.resonants:
        return False
    return True


def make_root(inv, rng):
    while True:
        c1 = inv.pick_consonant(rng)
        onset_r = inv.pick_resonant(rng) if rng.random() < inv.p_onset_r else None
        coda_r = inv.pick_resonant(rng) if rng.random() < inv.p_coda_r else None
        c2 = inv.pick_consonant(rng)
        if legal(inv, c1, onset_r, coda_r, c2):
            return (c1, onset_r, coda_r, c2)


def render(inv, root, grade):
    c1, onset_r, coda_r, c2 = root
    if grade != "zero":
        v = GRADE_VOWEL[grade]
        return "*" + c1 + (onset_r or "") + v + (coda_r or "") + c2 + "-"
    # zero grade: a resonant next to the vowel slot becomes syllabic;
    # prefer the coda resonant (PIE-style: *pʰerkʷ- > *pʰr̥kʷ-)
    if coda_r:
        nucleus = inv.syllabic[coda_r]
        return "*" + c1 + (onset_r or "") + nucleus + c2 + "-"
    if onset_r:
        return "*" + c1 + inv.syllabic[onset_r] + c2 + "-"
    # no resonant: bare skeleton (surfaces only with a syllabic suffix)
    return "*" + c1 + c2 + "-"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("-n", type=int, default=10, help="number of roots (default 10)")
    parser.add_argument("--grade", choices=GRADES, default="e", help="ablaut grade to render (default e)")
    parser.add_argument("--all-grades", action="store_true", help="show every grade of each root")
    parser.add_argument("--seed", type=int, help="random seed for reproducible output")
    args = parser.parse_args()

    inv = Inventory(json.loads(DATA_PATH.read_text(encoding="utf-8")))
    rng = random.Random(args.seed)

    for _ in range(args.n):
        root = make_root(inv, rng)
        if args.all_grades:
            print("  ".join(f"{g}: {render(inv, root, g)}" for g in GRADES))
        else:
            print(render(inv, root, args.grade))


if __name__ == "__main__":
    main()
