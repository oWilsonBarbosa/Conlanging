#!/usr/bin/env python3
"""Build a compact, offline frequency summary from PHOIBLE.

The Phonological Inventory Builder app (``app/``) needs naturalness signals —
how common each segment is, how big real inventories are, and which segments
imply which — but it must run offline as a static page. Vendoring the full
24 MB PHOIBLE table is wasteful, so this script distils it into a small JSON.

Input  : PHOIBLE 2.0 aggregated table ``phoible.csv``
         https://github.com/phoible/dev (data/phoible.csv)
Output : app/data/phoible-summary.json

The PHOIBLE *data* is CC-BY-SA 3.0 (Moran & McCloy 2019). This summary is an
adaptation and is therefore released under the SAME license, with attribution —
see app/data/phoible-summary.LICENSE. Re-run after pinning a PHOIBLE release:

    scripts/fetch_data.sh phoible      # or download data/phoible.csv directly
    python3 scripts/build_phoible_summary.py /path/to/phoible.csv
"""
from __future__ import annotations
import csv, json, sys, statistics as st
from pathlib import Path
from datetime import date

SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/phoible.csv")
OUT = Path(__file__).resolve().parent.parent / "app" / "data" / "phoible-summary.json"

# Counterpart implications to surface in the UI ("you have A but not B").
# Each is computed *from the data* as P(has B | has A); the app warns when the
# conditional is high and B is missing. Marked -> unmarked / voiced -> voiceless.
IMPLICATIONS = [
    ("b", "p", "voiced /b/ usually co-occurs with voiceless /p/"),
    ("d", "t", "voiced /d/ usually co-occurs with voiceless /t/"),
    ("ɡ", "k", "voiced /ɡ/ usually co-occurs with voiceless /k/"),
    ("v", "f", "voiced /v/ usually co-occurs with voiceless /f/"),
    ("z", "s", "voiced /z/ usually co-occurs with voiceless /s/"),
    ("ʒ", "ʃ", "voiced /ʒ/ usually co-occurs with voiceless /ʃ/"),
    ("ɣ", "x", "voiced /ɣ/ usually co-occurs with voiceless /x/"),
    ("ŋ", "n", "velar nasal /ŋ/ usually co-occurs with /n/"),
    ("ɲ", "n", "palatal nasal /ɲ/ usually co-occurs with /n/"),
    ("ŋ", "m", "/ŋ/ usually co-occurs with /m/"),
    ("e", "i", "mid /e/ usually co-occurs with high /i/"),
    ("o", "u", "mid /o/ usually co-occurs with high /u/"),
    ("ɛ", "e", "open-mid /ɛ/ usually co-occurs with close-mid /e/"),
    ("ɔ", "o", "open-mid /ɔ/ usually co-occurs with close-mid /o/"),
    ("e", "a", "mid /e/ usually co-occurs with low /a/"),
    ("o", "a", "mid /o/ usually co-occurs with low /a/"),
    ("iː", "i", "long /iː/ implies short /i/"),
    ("aː", "a", "long /aː/ implies short /a/"),
    ("uː", "u", "long /uː/ implies short /u/"),
    ("ĩ", "i", "nasal /ĩ/ usually co-occurs with oral /i/"),
    ("ã", "a", "nasal /ã/ usually co-occurs with oral /a/"),
    ("ũ", "u", "nasal /ũ/ usually co-occurs with oral /u/"),
    ("y", "i", "front-rounded /y/ usually co-occurs with front-unrounded /i/"),
    ("ø", "e", "front-rounded /ø/ usually co-occurs with front-unrounded /e/"),
    ("œ", "ɛ", "front-rounded /œ/ usually co-occurs with front-unrounded /ɛ/"),
    ("y", "u", "front-rounded /y/ usually co-occurs with back-rounded /u/"),
    ("ø", "o", "front-rounded /ø/ usually co-occurs with back-rounded /o/"),
    ("ɨ", "i", "central /ɨ/ usually co-occurs with front /i/"),
]

MIN_INV = 3  # keep segments attested in >= this many inventories


def main() -> None:
    inv: dict[str, dict[str, set]] = {}
    seg_inv: dict[str, set] = {}
    seg_class: dict[str, str] = {}

    with SRC.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            iid, ph, cls = row["InventoryID"], row["Phoneme"], row["SegmentClass"]
            d = inv.setdefault(iid, {"consonant": set(), "vowel": set(), "tone": set(), "all": set()})
            d[cls].add(ph)
            d["all"].add(ph)
            seg_inv.setdefault(ph, set()).add(iid)
            seg_class[ph] = cls

    N = len(inv)

    def size_stats(key: str) -> dict:
        xs = sorted(len(v[key]) for v in inv.values())
        n = len(xs)
        pct = lambda p: xs[min(n - 1, p * n // 100)]
        return {"mean": round(st.mean(xs), 1), "median": int(st.median(xs)),
                "p10": pct(10), "p25": pct(25), "p75": pct(75), "p90": pct(90),
                "min": xs[0], "max": xs[-1]}

    buckets = {"consonant": {}, "vowel": {}, "tone": {}}
    for ph, invs in seg_inv.items():
        if len(invs) >= MIN_INV:
            buckets[seg_class[ph]][ph] = len(invs)
    for b in buckets.values():  # frequency-sorted for readability
        pass
    buckets = {k: dict(sorted(v.items(), key=lambda kv: -kv[1])) for k, v in buckets.items()}

    implications = []
    for a, b, note in IMPLICATIONS:
        ia = seg_inv.get(a, set())
        if not ia:
            continue
        both = len(ia & seg_inv.get(b, set()))
        implications.append({"a": a, "b": b, "p": round(both / len(ia), 3), "note": note})

    summary = {
        "meta": {
            "source": "PHOIBLE 2.0",
            "citation": "Moran, S. & McCloy, D. (eds.) 2019. PHOIBLE 2.0. Jena: MPI-SHH.",
            "url": "https://phoible.org",
            "repo": "https://github.com/phoible/dev",
            "license": "CC-BY-SA-3.0",
            "n_inventories": N,
            "generated": date.today().isoformat(),
            "note": "Derived frequency summary. Counts are # of PHOIBLE inventories "
                    "containing each segment; divide by n_inventories for the proportion.",
            "sizes": {k: size_stats(k) for k in ("consonant", "vowel", "tone", "all")},
        },
        "consonants": buckets["consonant"],
        "vowels": buckets["vowel"],
        "tones": buckets["tone"],
        "implications": implications,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(summary, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    kb = OUT.stat().st_size / 1024
    print(f"wrote {OUT}  ({kb:.1f} KB)")
    print(f"  inventories: {N}")
    print(f"  consonants kept: {len(summary['consonants'])}, "
          f"vowels: {len(summary['vowels'])}, tones: {len(summary['tones'])}")
    print(f"  implications: {len(implications)}")


if __name__ == "__main__":
    main()
