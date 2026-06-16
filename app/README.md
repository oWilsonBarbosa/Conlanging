# Phonological Inventory Builder

A small, dependency-free web app for assembling a **phonological inventory** by
toggling IPA "blocks" on the consonant and vowel charts. As you build, it scores
the inventory for **naturalness** against real-language typology, with the data
coming from **PHOIBLE 2.0** (3,020 inventories).

Complexity is gated by **level**, mirroring the Conlangs University course:

| Level | Course | Status | What it covers |
|------:|--------|--------|----------------|
| **1** | Phonology 1 | ✅ implemented | Segments: consonant grid, vowel quadrilateral, common affricates/labial-velars |
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

`data/phoible-summary.json` is a compact summary distilled from PHOIBLE by
[`../scripts/build_phoible_summary.py`](../scripts/build_phoible_summary.py):

- **Segment frequency** — % of PHOIBLE inventories containing each sound (shown
  on every block, and used to praise/nudge).
- **Inventory-size stats** — mean/median/percentiles for consonants & vowels, so
  "16 consonants" can be judged *typical / small / large*.
- **Implicational co-occurrence** — e.g. *91% of languages with /ɡ/ also have /k/*;
  drives the "you have X but not Y" warnings (computed from the data, not hard-coded).

To refresh after pinning a new PHOIBLE release:

```bash
scripts/fetch_data.sh phoible          # or grab data/phoible.csv directly
python3 scripts/build_phoible_summary.py /path/to/phoible.csv
```

## Features

- Click blocks to add/remove sounds; commonness is shaded into each block.
- Live **naturalness** gauge + a transparent, itemised feedback list (no black box).
- **Presets**: cross-linguistic core, a five-vowel workhorse, and this repo's
  Alantian inventory.
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
│   └── phoible-summary.LICENSE  attribution + license for that file
└── README.md       you are here
```

## Licensing

- App code (`index.html`, `style.css`, `main.js`) — the repository's own work,
  **CC-BY 4.0** (see [`../LICENSE`](../LICENSE)).
- `data/phoible-summary.json` — a **derivative of PHOIBLE**, so **CC-BY-SA 3.0**
  with attribution; see [`data/phoible-summary.LICENSE`](data/phoible-summary.LICENSE)
  and [`../ATTRIBUTION.md`](../ATTRIBUTION.md). Please cite Moran & McCloy (2019).
