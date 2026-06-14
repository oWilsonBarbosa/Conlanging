# Lesson 06 — Phonology 2 (Phonotactics)

- **CU lesson:** <https://sites.google.com/view/conlangs-university/lessons> (Phonology 2)
- **Date:** 2026-06-14
- **Goal:** define how Alantian's inventory combines into syllables and words, and pin
  down the moraic weight rules.

## Decisions

- **Syllable template: (C)V(C)** — one optional onset, one optional coda, no
  tautosyllabic clusters.
- **Coda inventory: {m n l r s}** (sonorants + /s/). All obstruents are therefore
  onset-only.
- **Medial clusters:** only across a boundary, {m n l r s} + C (e.g. *as.pa, an.ta*).
- **Geminates:** limited to **mm nn ll rr ss** (coda + identical onset).
- **Hiatus: resolved** — identical vowels → long; distinct vowels → diphthong;
  epenthetic **/ʔ/** keeps vowels apart across morpheme boundaries.
- **Nasal vowels: short only** (no long-nasal) — settles the Lesson 02 open question.

## Why these fit the aesthetic

- **(C)V(C) + sonorant/s codas** keeps syllables opening cleanly and closing on a
  *ringing* (m n l r) or *crisp* (s) sound — directly serving "resonant" while the
  permitted coda gives the weight contrast that "moraic" needs.
- **Onset-only obstruents** fall out automatically and give an "ancient/clean" surface:
  no harsh stop-final syllables, aspirates always syllable-initial (as in Greek).
- **Hiatus resolution into our six diphthongs** makes the vowel system self-contained
  and flowing — vowel runs always coalesce, reinforcing the elevated, sung quality, and
  gives the glottal stop a clear morphophonological role.

## Characterization vs. real languages

| Trait | Real-world parallel |
|---|---|
| (C)V(C), no onset clusters, restricted codas | Classical **Arabic**, **Japanese**, Greek (at the simple end) |
| Codas mostly sonorant + /s/ | **Ancient Greek** (native words end in -n -r -s) |
| Geminates only in sonorants/s | **Finnish**/Italian-style geminates, narrowed to resonants |
| Hiatus → coalescence/diphthong | **Greek** crasis/contraction; Polynesian vowel flow |
| Epenthetic glottal stop on hiatus | **Arabic**, **German** onset ʔ |

## Sources consulted

| Source | What I looked at | How it informed the decision |
|---|---|---|
| Phonotacticon (Joo 2023) | Cross-linguistic syllable-structure types (max onset/coda, cluster inventories) | Confirmed (C)V(C) with restricted codas is a well-attested, "moderately complex/simple" type; positioned Alantian on that scale |
| WALS 12A (Syllable Structure) | Simple / Moderately complex / Complex classification | Alantian classes as *moderately complex* (codas, no onset clusters) — the intended "simple but not bare" profile |
| PBase | Attested hiatus-resolution & cluster alternations (coalescence, glide/glottal epenthesis) | Modeled the hiatus rules on real alternation patterns |
| CLTS | — | (segments already validated in Lesson 02) |

> Provenance only — rules are original, guided by typological comparison.

## Outputs

- [x] `phonology.md` — Phonotactics section (template, clusters, geminates, hiatus, weight)
- [ ] `grammar.md`
- [ ] `lexicon.csv`

## Open questions / revisit later

- Is there a **minimum word size** (e.g. bimoraic)? — decide with prosody (Lessons 10/11).
- Are word-initial **vowel-initial** syllables allowed, or does a default /ʔ/ appear?
  (Currently allowed; revisit with prosody.)
- Exact syllabification of syllabic sonorants in long consonant strings.

## License note

Nothing reproduced from external sources. Phonotacticon/WALS/PBase used for typological
comparison only.
