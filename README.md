# Conlanging

A workbench for **constructed-language (conlang) design**: a structured course
that walks through building a language end to end, plus a curated library of
real-world linguistic reference datasets to ground design decisions in how
natural languages actually behave.

This repo is currently a **resource collection** (learning material + data), not
a code pipeline. The one helper provided is a script to unzip the datasets into a
local working folder.

## Repository layout

```
.
├── course/   # 24 PDF lessons + assignments — the conlang design curriculum
├── data/     # 14 zipped linguistic reference datasets (~166 MB)
├── docs/     # the conlang's own design specs
└── scripts/  # helper scripts (data extraction)
```

## Design

The language being built is documented in [`docs/`](docs/):

- [`docs/phonology.md`](docs/phonology.md) — phoneme inventory (14 consonants +
  3 vowels), grounded in PHOIBLE/WALS. Allophony, syllable structure, and prosody
  are still to be designed.
- [`docs/morphology.md`](docs/morphology.md) — morphological type: agglutinating,
  suffixing, SOV, suffixal case, no gender ("Bundle A"), grounded in WALS/Grambank.
  Detailed case/TAM inventories and morphophonology still to come.
- [`docs/verbs.md`](docs/verbs.md) — verb system (Verbs 1): valency, subject
  agreement, tense/aspect/mood, valency-changing morphology, with a verb template
  and paradigm. Alignment (05d) and morphophonology still to come.

## `course/` — design curriculum

A complete, numbered course (assignments carry an `a`/`b`/… suffix). Suggested
order is the numeric order:

| Topic | Lessons |
|---|---|
| **Intro** | `01 Introduction to Conlanging` · `01a The Greatest Conlang Ever` |
| **Phonology** | `02 Phonology 1` (+assignment) · `06 Phonology 2` (+assignment) · `10 Phonology 3` · `11 Phonology 4` (+assignment) |
| **Morphology** | `03 Morphology 1` (+assignment) |
| **Verbs** | `04 Verbs 1` (+assignment) · `09 Verbs 2` |
| **Nouns** | `05a Case` · `05b Number` · `05c Class` · `05d Intro to Alignment` · `05e Assignment` |
| **Lexicon** | `07 Lexicon 1` (+assignment) · `12 Lexicon 2` |
| **Discourse / docs** | `08 Documentation 1` · `13 Information Structure` |

## `data/` — reference datasets

All datasets are stored zipped. Run the extraction script (below) to unpack them.
Grouped by the part of language design they support:

### Phonology & sound systems

| Dataset | What it is | Useful for | Format |
|---|---|---|---|
| **PHOIBLE** (`dev-master.zip`) | 3,000+ phoneme inventories across 2,100+ languages | Choosing a realistic phoneme inventory | CSV |
| **CLTS** (`clts-master.zip`, `clts-2.3.0.zip`) | Cross-Linguistic Transcription Systems: IPA segments + distinctive features | Standardizing/validating transcription & features | CSV/JS |
| **PBASE** (`pbasefiles.zip`) | Phonological alternations, distributional restrictions, IPA→feature maps | Designing allophony & sound rules | CSV |
| **BDPROTO** (`bdproto-master.zip`) | Phoneme inventories of reconstructed **proto-languages** | Diachronic conlangs / proto-language design | CSV |
| **Phonotacticon** (`phonotacticon-main.zip`) | Phonotactics (syllable structure) of 516 Eurasian lects | Defining syllable shape & phonotactics | CSV (CLDF) |

### Grammar & typology

| Dataset | What it is | Useful for | Format |
|---|---|---|---|
| **WALS** (`wals-master.zip`, `wals-v2020.4.zip`) | World Atlas of Language Structures — ~192 typological features | Picking internally-consistent grammar | CSV (CLDF) |
| **Grambank** (`grambank-master.zip`) | 195-feature grammatical typology database | Cross-checking grammatical choices | CSV (CLDF) |

### Lexicon, semantics & morphology

| Dataset | What it is | Useful for | Format |
|---|---|---|---|
| **Concepticon** (`concepticon-data-3.4.0.zip`) | Standardized concept sets / Swadesh-style lists | Seeding core vocabulary | CSV |
| **WOLD** (`wold_dataset.cldf.zip`) | World Loanword Database (borrowing patterns) | Modeling loanwords & contact | CSV (CLDF) |
| **Wiktextract** (`wiktextract-master.zip`) | Tooling/data extracted from Wiktionary | Mining lexical/etymological data | code + data |
| **MorphoLex-en** (`MorphoLex-en-master.zip`) | English morphological decomposition (roots/affixes) | Studying derivational structure | XLSX |
| **MorphyNet** (`MorphyNet-main.zip`) | Derivational + inflectional morphology, 15 languages* | Designing inflection & derivation | TSV |

\* MorphyNet languages: cat, ces, deu, eng, fin, fra, hbs, hun, ita, mon, pol, por, rus, spa, swe.

## Getting started

Unzip all datasets into `data/extracted/` (git-ignored):

```bash
./scripts/extract_data.sh           # extract everything (skips already-extracted)
./scripts/extract_data.sh --force   # re-extract, overwriting
./scripts/extract_data.sh --list    # list zips without extracting
```

Extracted data lives in `data/extracted/<dataset>/` and is **not** committed
(see `.gitignore`) — keep the zips as the source of truth.

## Notes

- **Duplicate archives:** `clts-master.zip` ≈ `clts-2.3.0.zip`, and
  `wals-master.zip` ≈ `wals-v2020.4.zip` (same upstream commit). You can drop one
  of each pair to save ~17 MB.
- **Formats:** most datasets follow the [CLDF](https://cldf.clld.org) standard
  (CSV + JSON metadata); a few are plain CSV/TSV, plus one XLSX.

## Sources & citations

Each dataset retains its upstream `README`/`LICENSE` inside its archive — consult
those for citation and license terms before redistributing. Project homepages:

- PHOIBLE — <https://phoible.org>
- CLTS — <https://clts.clld.org>
- WALS — <https://wals.info>
- Grambank — <https://grambank.clld.org>
- Concepticon — <https://concepticon.clld.org>
- WOLD — <https://wold.clld.org>
- Wiktextract — <https://github.com/tatuylonen/wiktextract>
- MorphyNet — <https://github.com/kbatsuren/MorphyNet>
- Phonotacticon — Joo, Ian & Yu-Yin Hsu (2025), *Phonotacticon: a cross-linguistic phonotactic database*, Linguistic Typology 29.2, 405–431.
