# Lesson 03 — Morphology 1

- **CU lesson:** <https://sites.google.com/view/conlangs-university/lessons> (Morphology 1)
- **Date:** 2026-06-14
- **Goal:** set Alantian's morphological type, word-building template, and root shapes.

## Decisions

- **Type: agglutinative** — low fusion, one meaning per affix, transparent ordered slots.
- **Affixation: both prefixes and suffixes ("grammar on both ends").**
  - Prefix slots: **negation, person agreement, aspect/mood.**
  - Suffix slots: **derivation, number, case.**
- **Word template:** `NEG – AGR – ASP/MOOD – ROOT – DERIV – NUMBER – CASE`.
- **Root typology:**
  - **CV** — rare, archaic/"primitive" layer (*ta, ku, si*).
  - **CVC** — default, most frequent (*tʰar, sal, men, kus*).
  - **CVRC** — sonorant + final C (*tarn, kʰuls, mirk*); final cluster splits under
    suffixation and resolves word-finally via syllabic sonorant/epenthesis.
- **Vowel harmony:** left **open** for a later morphophonology pass.

## Why these fit the aesthetic

- **Agglutination** gives the regular, transparent, "carved" feel of an ancient
  administrative/liturgical language — every ending legible, fitting "elevated".
- **Grammar on both ends** makes words visibly built-up (prefix + root + suffix),
  maximizing morphological richness without fusion.
- **CV/CVC/CVRC roots** tie morphology to the phonology: CVRC's splitting cluster
  reuses the syllabic sonorants and hiatus rules from Lesson 06, so morphology and
  phonology reinforce one another.

## Characterization vs. real languages

| Trait | Real-world parallel |
|---|---|
| Agglutinative, both prefixes & suffixes | **Georgian, Swahili (Bantu), Nahuatl** |
| Person/negation/aspect prefixes + case/number suffixes | **Bantu**, Kartvelian |
| CV/CVC/CVRC roots with cluster-splitting | **Sanskrit / Proto-Indo-European** roots |
| Ordered templatic slots | **Athabaskan, Bantu** verb templates |

## Sources consulted

| Source | What I looked at | How it informed the decision |
|---|---|---|
| WALS 20A (Fusion of Inflection) | Agglutinative = "exclusively concatenative" | Confirms the low-fusion, separable-affix design |
| WALS 26A (Prefixing vs Suffixing) | "Equal prefixing & suffixing" languages | Grounds the "both ends" choice as attested (a minority but real type) |
| Grambank | Presence of person prefixes, case/number suffixes | Validates splitting grammar across both edges |
| MorphyNet | Real morpheme-segmentation / affix-stacking across languages | Model for transparent, recoverable affix stacks |

> Provenance only — no paradigms or morphemes copied; the system is original.

## Outputs

- [x] `grammar.md` — Typological profile (type, affix position) + new **Morphology**
      section (template, root typology, morphophonology)
- [ ] `lexicon.csv`

## Open questions / revisit later

- **Vowel harmony** (rounding/other) yes/no? → morphophonology pass.
- Exact prefix vs suffix ordering when multiple stack; any circumfixes?
- Which root shape dominates the core lexicon (seed in Lexicon 1, L07).
- Inflectional categories themselves come in Nouns 1 (L05) and Verbs (L04/09).

## License note

Nothing reproduced from external sources. WALS/Grambank/MorphyNet used for typological
comparison only.
