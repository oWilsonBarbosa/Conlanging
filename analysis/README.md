# Inventory checker

Checks a draft phonological inventory against the typological datasets in
`../data/`. Written to support the Phonology 2 stage of the course, where you
actually choose an inventory — Phonology 1 is IPA literacy and its assignment is
deliberately not naturalistic, so don't point this at it.

No dependencies beyond the Python standard library, and nothing needs
unzipping — the datasets are read straight out of the shipped `.zip` files.

## Use

```sh
cd analysis
python3 inventory_check.py examples/starter.txt
python3 inventory_check.py my_lang.txt --allophony
python3 inventory_check.py my_lang.txt --json > report.json
```

An inventory file is one segment per line, or space/comma separated. `#` starts
a comment:

```
p t k b
m n ŋ
i e a o u    # five-vowel triangle
```

## What it reports

1. **Cross-linguistic frequency** — how many of PHOIBLE's languages have each of
   your segments, tiered core / common / uncommon / rare / unattested, with the
   CLTS name of each sound.
2. **Implicational check** — segments whose usual unmarked partner you left out
   (`/z/` without `/s/`, `/ẽ/` without `/e/`, `/tʼ/` without `/kʼ/`), with the
   count of real languages that do the same thing.
3. **Shape** — inventory size against the attested range, consonant/vowel split,
   C/V ratio, and any core segments you're missing.
4. **Allophony** (`--allophony`) — attested rules targeting your segments, from
   PBase. Use this to source realistic allophony instead of inventing it.

Nothing here says your conlang is wrong. Real inventories are lopsided, and a
perfectly symmetric chart is the main thing that reads as artificial. Every flag
means "here is what you're departing from" — departing on purpose is the point.

## Method, and where it can mislead

- **PHOIBLE ships 3,020 inventories for ~2,176 distinct Glottocodes.** Well
  described languages appear several times, so the tool keeps one inventory per
  Glottocode. Percentages are shares of those 2,176.
- **PHOIBLE is not areally or genealogically balanced.** Australian and Sinitic
  transcription traditions are visible in the raw counts. Treat percentages as
  rough guides, not population parameters.
- **Transcription conventions split segments.** `/t/` reads as 72% and `/t̪/` as
  22%, but that is substantially one decision recorded two ways rather than two
  facts about languages. Pick a convention and hold it.
- **All comparison is NFD-normalized.** IPA has precomposed and decomposed forms
  for anything with a diacritic; without normalization `ĩ` silently fails to
  match `ĩ`. Note also that IPA `ɡ` is U+0261, not keyboard `g`.
- **Implications are filtered two ways.** A raw P(B|A) ≥ 0.90 scan mostly
  returns "everything implies /m/", since /m/ is in 96.6% of languages. So a
  pair must either clear a lift bar (P(B|A) beating B's own base rate) or be a
  case where A is B plus an added feature — `/ẽ/` over `/e/`, `/iː/` over `/i/`.
  That second lane matters: `/ĩ/` implies `/i/` with zero exceptions but only 6
  points of lift, so a lift bar alone would discard it.
- **Counterpart vs co-occurrence** is decided by distance between CLTS feature
  names. `/z/` and `/s/` differ by one word; `/z/` and `/b/` by five. Only close
  pairs are reported as markedness gaps; the rest are available behind
  `--all-implications`.
- **PBase covers 306 languages.** It is a plausibility sampler for allophony,
  not a frequency estimate.

## Files

| file | purpose |
|---|---|
| `inventory_check.py` | CLI and report formatting |
| `phoible_db.py` | dataset loaders (PHOIBLE, CLTS, PBase) and the featural helpers |
| `test_inventory_check.py` | self-checks against known figures — `python3 test_inventory_check.py` |
| `examples/starter.txt` | the unmarked core, as a baseline to modify |
| `examples/marked.txt` | a deliberately marked draft that trips the checker |

Parsed PHOIBLE is cached in `analysis/.cache/` (gitignored). Delete it or pass
`--no-cache` to re-parse.

## Data sources

PHOIBLE (`data/dev-master.zip`), CLTS 2.3.0 (`data/clts-2.3.0.zip`), PBase
(`data/pbasefiles.zip`). Each carries its own license; see the archives.
