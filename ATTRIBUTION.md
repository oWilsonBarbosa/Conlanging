# Attribution & Data Licenses

This project builds on third-party academic linguistic datasets. They are **not**
redistributed in this repository — `scripts/fetch_data.sh` downloads them from
their original sources (see `data/sources.csv`). Each dataset is the work of its
authors and is governed by its own license. Please **cite the original sources**
in any work derived from them, and honour the obligations summarized below.

## Quick license summary

| Dataset | License | Commercial use | ShareAlike |
|---|---|---|---|
| WALS | CC-BY 4.0 | ✅ | — |
| Grambank | CC-BY 4.0 | ✅ | — |
| Concepticon | CC-BY 4.0 | ✅ | — |
| CLTS | CC-BY 4.0 | ✅ | — |
| WOLD | CC-BY 4.0 | ✅ | — |
| Phonotacticon | CC-BY 4.0 | ✅ | — |
| BDPROTO | CC-BY-SA 4.0 | ✅ | ⚠️ yes |
| MorphyNet | CC-BY-SA 4.0 | ✅ | ⚠️ yes |
| PHOIBLE | GPL-3.0 (code) / CC-BY-SA (data) | ✅ | ⚠️ yes |
| Wiktextract | MIT (code) / CC-BY-SA·GFDL (data) | ✅ | ⚠️ yes |
| **PBase** | CC-BY-NC-SA 4.0 | ❌ **no** | ⚠️ yes |
| **MorphoLex-en** | CC-BY-NC-SA 4.0 | ❌ **no** | ⚠️ yes |

### ⚠️ NonCommercial datasets
**PBase** and **MorphoLex-en** are licensed **CC-BY-NC-SA 4.0**. They may **not** be
used for commercial purposes, and any derivative must keep the same license and
credit the authors.

### ⚠️ ShareAlike datasets
**BDPROTO, MorphyNet, PHOIBLE (data), Wiktextract (data), PBase, MorphoLex-en** are
ShareAlike. If you redistribute them or adaptations of them, you must do so under the
same (or a compatible) license and preserve attribution.

## Sources & citations

- **WALS — World Atlas of Language Structures** · CC-BY 4.0 · <https://wals.info> · <https://github.com/cldf-datasets/wals>
  Dryer, Matthew S. & Haspelmath, Martin (eds.) (2013). *WALS Online.* Leipzig: Max Planck Institute for Evolutionary Anthropology.
- **Grambank** · CC-BY 4.0 · <https://grambank.clld.org> · <https://github.com/grambank/grambank>
  Skirgård, Hedvig et al. (2023). *Grambank v1.0.*
- **Concepticon** · CC-BY 4.0 · <https://concepticon.clld.org> · <https://github.com/concepticon/concepticon-data>
  List, J.-M., Tjuka, A. et al. (eds.) *Concepticon* (v3.4.0). Max Planck Institute for Evolutionary Anthropology.
- **CLTS — Cross-Linguistic Transcription Systems** · CC-BY 4.0 · <https://clts.clld.org> · <https://github.com/cldf-clts/clts>
  List, J.-M., Anderson, C., Tresoldi, T., Forkel, R. *CLTS.*
- **WOLD — World Loanword Database** · CC-BY 4.0 · <https://wold.clld.org> · <https://github.com/lexibank/wold>
  Haspelmath, M. & Tadmor, U. (eds.) (2009). *WOLD.* Leipzig: MPI-EVA.
- **Phonotacticon** · CC-BY 4.0 · <https://github.com/ianjoo/phonotacticon>
  Joo, Ian (2023). *Phonotacticon: A cross-linguistic database of phonotactic patterns.* Linguistic Typology. <https://doi.org/10.1515/lingty-2023-0094>
- **BDPROTO** · CC-BY-SA 4.0 · <https://github.com/bdproto/bdproto>
  Marsico, E., Flavier, S., Verkerk, A., Moran, S. (2018). *BDPROTO.*
- **MorphyNet** · CC-BY-SA 4.0 · <https://github.com/kbatsuren/MorphyNet>
  Batsuren, K., Bella, G., Giunchiglia, F. (2021). *MorphyNet.*
- **PHOIBLE** · code GPL-3.0 / data CC-BY-SA · <https://phoible.org> · <https://github.com/phoible/dev>
  Moran, S. & McCloy, D. (eds.) (2019). *PHOIBLE 2.0.* Jena: MPI for the Science of Human History.
- **Wiktextract** · code MIT / data CC-BY-SA·GFDL (from Wiktionary) · <https://github.com/tatuylonen/wiktextract>
  Ylönen, T. (2022). *Wiktextract.*
- **PBase** · CC-BY-NC-SA 4.0 · <https://pbase.phon.chass.ncsu.edu/>
  Mielke, J. *PBase: A database of phonological patterns.* (Manual download.)
- **MorphoLex-en** · CC-BY-NC-SA 4.0 · <https://github.com/hugomailhot/MorphoLex-en>
  Sánchez-Gutiérrez, C. H., Mailhot, H., Deacon, S. H., Wilson, M. A. (2018). *MorphoLex.*

## Derived data committed in this repo

Unlike the raw datasets above (which are fetched, not committed), one **derived**
file is checked in:

- **`app/data/phoible-summary.json`** — segment frequencies, inventory-size
  statistics, and co-occurrence conditionals computed from **PHOIBLE 2.0** by
  `scripts/build_phoible_summary.py`, for the Phonological Inventory Builder app.
  As an adaptation of PHOIBLE data it is **CC-BY-SA 3.0** with attribution to
  Moran & McCloy (2019); see `app/data/phoible-summary.LICENSE`. This obligation
  applies to that file only — the app's own code is CC-BY 4.0.

- **`app/data/wals-phonology.json`** — per-category language counts for nine WALS
  phonology features, computed from **WALS Online** by
  `scripts/build_wals_phonology.py`, used as the app's typological cross-check.
  As an adaptation of WALS data it is **CC-BY 4.0** with attribution to Dryer &
  Haspelmath (2013); see `app/data/wals-phonology.LICENSE`.

> If you spot an out-of-date citation, version, or license, please open an issue or
> correct `data/sources.csv` and this file together.
