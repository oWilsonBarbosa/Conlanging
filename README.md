# Conlanging

A working repository for a constructed-language (conlang) project. It collects the
**reference datasets** and **learning materials** used while designing the language —
organized so that everything is reproducible and every external source is properly
credited.

## Repository layout

```
.
├── README.md          You are here
├── LICENSE            CC BY 4.0 — covers this repo's own original content only
├── ATTRIBUTION.md     Credits, citations & licenses for every external dataset
├── .gitignore         Keeps large datasets and course PDFs out of git
├── course/
│   └── README.md      Curriculum outline + where to find the course (PDFs not redistributed)
├── data/
│   ├── README.md      What each dataset is and how to get it
│   └── sources.csv    Machine-readable manifest: name, url, version, license, …
└── scripts/
    └── fetch_data.sh  Downloads the datasets from their original sources
```

## Datasets are not committed

The linguistic datasets (WALS, Grambank, Concepticon, CLTS, WOLD, PHOIBLE,
BDPROTO, MorphyNet, Wiktextract, PBase, MorphoLex-en, Phonotacticon) are large
third-party academic resources. Rather than vendoring ~166 MB of ZIP files, this
repo records **where each came from** and downloads them on demand:

```bash
scripts/fetch_data.sh          # fetch everything listed in data/sources.csv
scripts/fetch_data.sh grambank # fetch a single dataset
```

Downloaded archives land in `data/` and are git-ignored.

## Licensing & ethics

- This repository's **own** original content is licensed **CC BY 4.0** (see `LICENSE`).
- Every external dataset keeps its **own** license. Several require attribution and
  ShareAlike; **PBase** and **MorphoLex-en** are **NonCommercial**. Read
  [`ATTRIBUTION.md`](ATTRIBUTION.md) and cite the original authors before reusing or
  redistributing any of them.
- The course PDFs that used to live in `course/` were third-party copyrighted
  materials and have been removed; see [`course/README.md`](course/README.md) for the
  outline and where to obtain them.
