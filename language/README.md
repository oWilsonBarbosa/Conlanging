# Alantian

> **Working name:** Alantian — an a-priori language of a fictional ancient culture.
> Aesthetic: *ancient, elevated, moraic, resonant.*

An original constructed language built by following the
[Conlangs University curriculum](https://sites.google.com/view/conlangs-university/lessons)
and informed by typological databases (WALS, Grambank, PHOIBLE, Concepticon, …).

All design decisions here are **original work** derived from those sources, not copied
from them — see [`../ATTRIBUTION.md`](../ATTRIBUTION.md) for source credits. This
language's own content is licensed under the repo's `LICENSE` (CC BY 4.0).

## How this folder works

| File / folder | Role |
|---|---|
| [`design/`](design/) | **The journey.** One log per CU lesson: goal, decisions, sources consulted, rationale. This is where "strategies and sources used" get recorded. |
| `phonology.md` | **Living reference** — current inventory & phonotactics. |
| `grammar.md` | **Living reference** — current morphology & syntax. |
| `diachrony.md` | **Living reference** — proto-forms & ordered sound changes (the history behind the morphophonology). |
| `lexicon.csv` | **Living reference** — the words (form, IPA, gloss, source). |

**Workflow per lesson:** open the CU lesson → copy `design/_template.md` to the next
numbered file → make decisions, logging which database/feature informed each → fold the
results into `phonology.md` / `grammar.md` / `lexicon.csv` → commit.

## Status

See the progress checklist in [`design/README.md`](design/README.md).
