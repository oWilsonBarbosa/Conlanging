# Datasets

This directory holds third-party linguistic datasets used by the project. The data
itself is **not committed** to git — it is downloaded from the original sources.

## How to get the data

```bash
../scripts/fetch_data.sh          # download everything
../scripts/fetch_data.sh wals     # download only matching datasets
```

Archives are written here as `<name>.zip` and ignored by git (see `.gitignore`).

## Manifest

[`sources.csv`](sources.csv) is the source of truth: each row gives a dataset's
`name`, download `url`, `version`, `license`, whether commercial use is allowed, and
notes. Edit it to add or pin datasets.

## Licenses — read before reusing

Full credits and citations are in [`../ATTRIBUTION.md`](../ATTRIBUTION.md). Highlights:

- **Most datasets are CC-BY 4.0** — attribution required (WALS, Grambank, Concepticon,
  CLTS, WOLD, Phonotacticon).
- **ShareAlike** — BDPROTO, MorphyNet, PHOIBLE (data), Wiktextract (data): keep the
  same license on any redistribution.
- **NonCommercial** — ⚠️ **PBase** and **MorphoLex-en** (CC-BY-NC-SA 4.0): not for
  commercial use.
- **PBase** has no downloadable archive; fetch it manually from
  <https://pbase.phon.chass.ncsu.edu/>.
