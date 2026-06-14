# Lesson 03b — Morphophonology revision (ablaut, infixation, inventory tweaks)

- **Context:** a revision pass after reviewing the whole system. Adjusts the inventory
  and enriches morphology with non-concatenative machinery.
- **Date:** 2026-06-14

## Decisions (settled)

1. **Nasal vowels removed.** Vowels now contrast in **length only** (a i u + ā ī ū).
2. **Geminates generalized.** *Any* consonant may geminate (pp tt kk, bb dd gg, ff ss xx,
   mm nn ll rr), not just sonorants + s. Geminate-half is a licensed coda; glides/h/ʔ
   do not geminate. Syllable stays **CV(R)** (coda = sonorant, /s/, or geminate-half).
3. **Infixation added.** Morphology is now prefix + infix + suffix + ablaut. Default
   infix: nasal **‹-N-›** before the final root consonant (PIE-style), e.g. *tak- → tank-*.
4. **Ablaut system added.** Vowels, diphthongs, and syllabic sonorants form a grade
   ladder (Sanskrit *guṇa/vṛddhi* / PIE-style) used for derivation & inflection:

   | Grade | i | u | a | CVRC |
   |---|---|---|---|---|
   | Zero | ∅/i̯ | ∅/u̯ | ∅ | syllabic R (*tṛn*) |
   | Full | i | u | a | a (*tarn*) |
   | Strong (guṇa) | ai | au | ā | ā (*tārn*) |
   | Long (vṛddhi) | āi | āu | ā | — |

5. **Affix labour reaffirmed** (from L03): prefixes = NEG / AGR / ASP·MOOD; suffixes =
   DERIV / NUMBER / CASE; **infix** inside root; **ablaut** on the root nucleus. Concrete
   morpheme→category mappings are still set in Nouns L05 / Verbs L04·L09.

## Why this fits the aesthetic

- Ablaut + infixation pull the morphology back toward the **Sanskrit/PIE** pole, so it
  now *rhymes* with the Greek/Sanskrit phonology — resolving the earlier coherence flag.
- Generalized geminates give the moraic weight system far more to work with, and pair
  naturally with a possible **consonant gradation** (geminate ↔ singleton).
- Dropping nasal vowels keeps the vowel system lean so the **ablaut ladder** stays clean.

## Open — to decide now: vowel harmony &/or consonant gradation

See the menu in chat / below. Both interact with ablaut and affixation.

- **Vowel harmony** candidates: none · rounding (i↔u) · frontness (i vs u, a neutral).
- **Consonant gradation** candidates: none · quantitative (geminate↔singleton) ·
  lenition (p→f, k→x, t→s/r) · both.

## Characterization vs. real languages

| Trait | Parallel |
|---|---|
| Ablaut grades (zero/full/guṇa/vṛddhi) | **Sanskrit, PIE, Germanic** (sing/sang/sung) |
| Nasal infix | **Latin** *vincō/vīcī*, PIE present infix |
| Generalized geminates + (possible) gradation | **Finnish/Italian** geminates; **Finnic/Sámi** gradation |

## Sources consulted

| Source | What | How it informed |
|---|---|---|
| WALS 20A/21A (fusion, exponence) | Non-concatenative / cumulative exponence types | Grounds ablaut + infixation as attested morphology |
| MorphyNet | Morphological alternations / stem changes | Model for grade- and gradation-based stem variation |
| PBase | Consonant/vowel alternations (lenition, gradation) | Menu of realistic gradation patterns |

## Outputs

- [x] `phonology.md` — nasal vowels removed; geminates generalized; CV(R) coda licensing
- [x] `grammar.md` — infixation + ablaut ladder + non-concatenative section
- [ ] (pending) vowel harmony / consonant gradation once chosen

## License note

Nothing reproduced from external sources; typological comparison only.
