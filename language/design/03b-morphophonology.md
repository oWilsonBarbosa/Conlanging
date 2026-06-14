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
4. **Ablaut system (4 grades).** A root nucleus is **coloured** by ∅/i/u/a, resolved by
   the hiatus rules. The four grades regenerate the entire vowel inventory (3 plain +
   3 long + 6 diphthongs):

   | base ＼ grade | plain | i-grade | u-grade | a-grade |
   |---|---|---|---|---|
   | **a** | a | ai | au | ā |
   | **i** | i | ī | iu | ia |
   | **u** | u | ui | ū | ua |

   Applies to any root shape (CV/CVC/CVRC). Example: *kis-* → kis / kīs / kius / kias.

5. **Affix labour reaffirmed** (from L03): prefixes = NEG / AGR / ASP·MOOD; suffixes =
   DERIV / NUMBER / CASE; **infix** inside root; **ablaut** on the root nucleus. Concrete
   morpheme→category mappings are still set in Nouns L05 / Verbs L04·L09.

6. **Vowel harmony: none.** Suffix vowels are fixed (ablaut covers vowel play).
7. **Consonant gradation: both (3-grade).** p t k → strong **geminate** (pp tt kk)
   before an open syllable / **weak** **fricative** (f s x) before a closed syllable /
   **basic** singleton after a heavy nucleus. E.g. *kap+a → kappa*, *kap+an → kafan*,
   *kāp+a → kāpa*. Geminates = strong grade; f s x = weak grade — both inventory
   features become load-bearing.

## Why this fits the aesthetic

- Ablaut + infixation pull the morphology back toward the **Sanskrit/PIE** pole, so it
  now *rhymes* with the Greek/Sanskrit phonology — resolving the earlier coherence flag.
- Generalized geminates give the moraic weight system far more to work with, and pair
  naturally with a possible **consonant gradation** (geminate ↔ singleton).
- Dropping nasal vowels keeps the vowel system lean so the **ablaut ladder** stays clean.

## Decided: harmony & gradation

- **Vowel harmony — none.**
- **Consonant gradation — both** (3-grade geminate ↔ singleton ↔ fricative; see #7).

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
- [x] `grammar.md` — infixation + 4-grade ablaut matrix + 3-grade consonant gradation;
      vowel harmony set to none

## License note

Nothing reproduced from external sources; typological comparison only.
