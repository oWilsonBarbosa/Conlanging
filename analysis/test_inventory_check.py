#!/usr/bin/env python3
"""Checks that the loaders still reproduce known figures. Run: python3 test_inventory_check.py

These assert against numbers derived from the shipped data, so a failure means
either a dataset was replaced or the parsing changed -- both worth knowing.
"""

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

failures = []


def check(label, actual, expected):
    ok = actual == expected
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {actual!r}")
    if not ok:
        failures.append(f"{label}: expected {expected!r}, got {actual!r}")


def close(label, actual, expected, tolerance):
    ok = abs(actual - expected) <= tolerance
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {actual:.3f}")
    if not ok:
        failures.append(f"{label}: expected ~{expected}, got {actual}")


db = Phoible.load()

check("languages after Glottocode dedup", db.n, 2176)
close("/m/ frequency", db.frequency("m"), 0.966, 0.002)
close("/i/ frequency", db.frequency("i"), 0.936, 0.002)
close("/k/ frequency", db.frequency("k"), 0.904, 0.002)
check("smallest inventory", db.sizes()[0], 11)
check("largest inventory", db.sizes()[-1], 161)

# Normalization: precomposed and decomposed nasal vowels must compare equal.
# Getting this wrong silently reports attested segments as unattested.
check("NFD normalization of nasal vowel", norm("ĩ") == norm("ĩ"), True)
assert db.counts.get(norm("ĩ"), 0) > 300, "nasal /ĩ/ should be attested"

# Nasal vowels imply their oral counterpart: this was exceptionless for /ĩ/.
implied = dict((seg, p) for seg, p, _, _, _ in db.implications("ĩ"))
check("ĩ implies i", implied.get(norm("i")), 1.0)

# /b/ does NOT reliably imply /p/ -- lift is near zero, so the lift filter
# should drop it entirely.
b_implies = {
    seg for seg, _, lift, _, _ in db.implications("b") if lift >= 0.10
}
check("b does not imply p", norm("p") in b_implies, False)

names = clts_names()
check("CLTS names loaded", len(names) > 5000, True)
check("z/s are counterparts", counterpart_distance(names[norm("z")], names[norm("s")]), 2)
check(
    "z/b are not counterparts",
    counterpart_distance(names[norm("z")], names[norm("b")]) > 2,
    True,
)
check(
    "consonant/vowel never counterparts",
    counterpart_distance(names[norm("s")], names[norm("i")]),
    None,
)

# The lift exemption must fire for "A is B plus a feature" and only there.
# Without it /ĩ/ -> /i/ is lost; with it applied too widely, /p/ -> /k/ and
# /i/ -> /a/ get reported as markedness gaps, which they are not.
check("nasalized vowel adds a feature over its oral base",
      adds_features(names[norm("ĩ")], names[norm("i")]), True)
check("long vowel adds a feature over its short base",
      adds_features(names[norm("iː")], names[norm("i")]), True)
check("p is not k plus a feature", adds_features(names[norm("p")], names[norm("k")]), False)
check("i is not a plus a feature", adds_features(names[norm("i")], names[norm("a")]), False)

lift_by_target = {seg: lift for seg, _, lift, _, _ in db.implications("p")}
check("p -> k would fail the lift bar on its own",
      lift_by_target.get(norm("k"), 0) < 0.10, True)

rules = pbase_rules(["k"])
check("PBase has rules for /k/", len(rules[norm("k")]) > 100, True)

inventory = read_inventory("examples/starter.txt")
check("starter inventory size", len(inventory), 16)

print()
if failures:
    print(f"{len(failures)} failure(s):")
    for f in failures:
        print("  " + f)
    sys.exit(1)
print("all checks passed")
