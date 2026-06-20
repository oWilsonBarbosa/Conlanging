# Phonological Inventory Builder

A small, dependency-free web app for assembling a **phonological inventory** by
toggling IPA "blocks" on the consonant and vowel charts. As you build, it scores
the inventory for **naturalness** against real-language typology, with the data
coming from **PHOIBLE 2.0** (3,020 inventories).

Complexity is gated by **level**, mirroring the Conlangs University course:

| Level | Course | Status | What it covers |
|------:|--------|--------|----------------|
| **1** | Phonology 1 | ✅ implemented | Segments, in four tabs mirroring the IPA chart: **Pulmonic** · **Non-pulmonic** (clicks, implosives, ejectives) · **Other / co-articulated** (w, ʍ, ɥ, k͡p, ɡ͡b, affricates, ɕ ʑ, epiglottals…) · **Vowels** |
| 2 | Phonology 2 | 🚧 scaffolded | Length & gemination, nasal vowels, diphthongs, syllable templates, cluster/coda rules |
| 3 | Phonology 3 | 🚧 scaffolded | Stress, mora weight, vowel harmony |
| 4 | Phonology 4 | 🚧 scaffolded | Register/contour tone, pitch accent, sandhi |

This is **v1**: Level 1 is fully interactive; Levels 2–4 are defined in the level
framework (`LEVELS` in `main.js`) and shown as roadmap cards, ready to fill in.

## Run it

It's a static page, but it `fetch`es a JSON data file, so open it over HTTP
(not `file://`):

```bash
cd app
python3 -m http.server 8000
# then open http://localhost:8000/
```

It also works as-is on **GitHub Pages** (point Pages at `/app`).

## What the feedback is based on

Two complementary sources are crossed:

**PHOIBLE 2.0** → `data/phoible-summary.json`, distilled by
[`../scripts/build_phoible_summary.py`](../scripts/build_phoible_summary.py):

- **Segment frequency** — % of 3,020 inventories containing each sound (shown on
  every block, and used to praise/nudge).
- **Inventory-size stats** — mean/median/percentiles for consonants & vowels.
- **Implicational co-occurrence** — e.g. *91% of languages with /ɡ/ also have /k/*;
  drives the "you have X but not Y" warnings (computed from the data, not hard-coded).

**WALS** → `data/wals-phonology.json`, distilled by
[`../scripts/build_wals_phonology.py`](../scripts/build_wals_phonology.py), adds the
*typological* view (its ~567-language phonology sample) as a labelled **WALS**
cross-check in the feedback panel:

- **Inventory-size class** (1A/2A) — "16 consonants → an *average* inventory (35% of WALS)".
- **Voicing contrast** (4A) — in plosives, fricatives, both, or neither.
- **Uncommon consonants** (19A) — clicks, labial-velars, pharyngeals, 'th' sounds.
- **Absence of common consonants** (18A) — no nasals / fricatives / bilabials.
- **Uvulars** (6A), **velar nasal** (9A), **front rounded vowels** (11A).

To refresh after pinning new releases:

```bash
scripts/fetch_data.sh phoible          # or grab data/phoible.csv directly
python3 scripts/build_phoible_summary.py /path/to/phoible.csv
scripts/fetch_data.sh wals             # then point at the unzipped cldf/ dir
python3 scripts/build_wals_phonology.py /path/to/wals/cldf
```

## Features

- Four tabs (Pulmonic / Non-pulmonic / Other / Vowels) with live per-tab counts;
  click blocks to add/remove sounds; commonness is shaded into each block.
- The pulmonic grid is the **complete** IPA chart: impossible articulations are
  shaded, and a **“Show derived ⟨t̪ m̥⟩”** toggle reveals cells written with a
  diacritic (dental/labiodental stops, dental nasal, voiceless sonorants…),
  hidden by default to keep the base chart clean.
- Live **naturalness** gauge + a transparent, itemised feedback list (no black box).
- **Presets**: 9 starting points spanning the typological space — a
  cross-linguistic core and five-vowel workhorse, plus profiles modelled on real
  language types (Australian with no fricatives, minimal Polynesian, back-heavy
  Arabic, ejective Caucasian/Andean, labial-velar West African, vowel-rich
  Turkic) and this repo's Alantian inventory.
- **Export**: Markdown tables matching `language/phonology.md`, or JSON; **Import**
  JSON / a space-separated IPA list. Work auto-saves to `localStorage`.

## Files

```
app/
├── index.html      markup/shell
├── style.css       dark "blocks" UI
├── main.js         charts, level framework, naturalness engine, export
├── data/
│   ├── phoible-summary.json     derived PHOIBLE summary (CC-BY-SA 3.0)
│   ├── phoible-summary.LICENSE  attribution + license for that file
│   ├── wals-phonology.json      derived WALS summary (CC-BY 4.0)
│   └── wals-phonology.LICENSE   attribution + license for that file
└── README.md       you are here
```

## Licensing

- App code (`index.html`, `style.css`, `main.js`) — the repository's own work,
  **CC-BY 4.0** (see [`../LICENSE`](../LICENSE)).
- `data/phoible-summary.json` — a **derivative of PHOIBLE**, so **CC-BY-SA 3.0**
  with attribution; see [`data/phoible-summary.LICENSE`](data/phoible-summary.LICENSE)
  and [`../ATTRIBUTION.md`](../ATTRIBUTION.md). Please cite Moran & McCloy (2019).
