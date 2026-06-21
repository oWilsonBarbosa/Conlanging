#!/usr/bin/env python3
"""Build a compact WALS phonology summary for the Inventory Builder app.

PHOIBLE gives raw per-segment frequencies; WALS adds the *typological* view —
categorical classes (inventory-size bands, voicing contrast, uncommon/absent
consonants) over its curated ~200-language sample. Crossing the two gives the
app richer Level-1 feedback ("16 consonants = an 'Average' inventory, the most
common WALS class").

Input  : WALS CLDF tables (codes.csv, values.csv) from
         https://github.com/cldf-datasets/wals  (cldf/)
Output : app/data/wals-phonology.json

WALS is CC-BY 4.0 (Dryer & Haspelmath 2013). Attribution is carried in the JSON
meta and app/data/wals-phonology.LICENSE. Re-run after pinning a release:

    scripts/fetch_data.sh wals
    python3 scripts/build_wals_phonology.py /path/to/cldf
"""
from __future__ import annotations
import csv, json, sys
from pathlib import Path
from collections import defaultdict, Counter
from datetime import date

CLDF = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp")
CODES = CLDF / ("codes.csv" if (CLDF / "codes.csv").exists() else "wals_codes.csv")
VALUES = CLDF / ("values.csv" if (CLDF / "values.csv").exists() else "wals_values.csv")
OUT = Path(__file__).resolve().parent.parent / "app" / "data" / "wals-phonology.json"

# Features crossed with Level 1, with short app-facing names. Size features carry
# the published WALS bin edges (inclusive upper bounds; null = open top band).
FEATURES = {
    "1A": {"name": "Consonant inventory size",
           "bins": [[14, "Small"], [18, "Moderately small"], [25, "Average"],
                    [33, "Moderately large"], [None, "Large"]]},
    "2A": {"name": "Vowel-quality inventory size",
           "bins": [[4, "Small (2-4)"], [6, "Average (5-6)"], [None, "Large (7-14)"]]},
    "4A": {"name": "Voicing in plosives & fricatives"},
    "6A": {"name": "Uvular consonants"},
    "8A": {"name": "Lateral consonants"},
    "9A": {"name": "The velar nasal /ŋ/"},
    "11A": {"name": "Front rounded vowels"},
    "18A": {"name": "Absence of common consonants"},
    "19A": {"name": "Presence of uncommon consonants"},
}


def main() -> None:
    codes = {r["ID"]: r for r in csv.DictReader(CODES.open(encoding="utf-8"))}
    dist = defaultdict(Counter)
    for r in csv.DictReader(VALUES.open(encoding="utf-8")):
        p = r["Parameter_ID"]
        if p in FEATURES and r["Code_ID"]:
            dist[p][r["Code_ID"]] += 1

    out_features = {}
    for pid, meta in FEATURES.items():
        items = sorted(dist[pid].items(), key=lambda kv: int(codes[kv[0]].get("Number") or 0))
        total = sum(n for _, n in items)
        feat = {"name": meta["name"], "n": total,
                "dist": {codes[cid]["Name"]: n for cid, n in items}}
        if "bins" in meta:
            feat["bins"] = meta["bins"]
        out_features[pid] = feat

    summary = {
        "meta": {
            "source": "WALS Online (CLDF)",
            "citation": "Dryer, M.S. & Haspelmath, M. (eds.) 2013. WALS Online. Leipzig: MPI-EVA.",
            "url": "https://wals.info",
            "repo": "https://github.com/cldf-datasets/wals",
            "license": "CC-BY-4.0",
            "generated": date.today().isoformat(),
            "note": "Counts are languages in the WALS sample per category; the sample "
                    "(~200/100-language phonology samples) is smaller and differently "
                    "balanced than PHOIBLE, so treat it as a typological cross-check.",
        },
        "features": out_features,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(summary, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"wrote {OUT}  ({OUT.stat().st_size/1024:.1f} KB)")
    for pid, f in out_features.items():
        print(f"  {pid:>4} {f['name']:<34} n={f['n']}  cats={len(f['dist'])}")


if __name__ == "__main__":
    main()
