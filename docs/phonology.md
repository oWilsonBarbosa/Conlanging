# Phonology — Design Specification

A working phonology for the project conlang. Design philosophy: a **small,
contrast-light inventory**, to be enriched later through allophony and prosody.

> **Status:** baseline inventory only. Allophony, prosody (stress/weight), and
> syllable structure are **not yet decided** — see [§3](#3-next-steps).

> **Notation.** `/…/` phonemes · `[…]` surface phones. Romanization can keep
> ⟨g, y⟩ for /ɡ, j/.

---

## 1. Phoneme inventory (14 C + 3 V)

### Consonants

| | Labial | Coronal | Palatal | Velar | Glottal |
|---|---|---|---|---|---|
| Plosive (vl.) | p | t | | k | |
| Plosive (vd.) | b | d | | ɡ | |
| Nasal | m | n | | | |
| Fricative | | s | | | h |
| Liquid | | l  r | | | |
| Glide | w | | j | | |

### Vowels

| | Front | Central | Back |
|---|---|---|---|
| Close | i | | u |
| Open | | a | |

**Notes**

- Written ⟨g⟩ = /ɡ/ (IPA script-g) and ⟨y⟩ = /j/ — orthography vs. phonemes
  (Phonology 1).
- **/j w/ are phonemes**, distinct from syllabic [i u]; [i u] are nuclei, [j w] are
  margins. (Minimal pairs like /ia/ vs /ja/ carry the contrast.)
- **/l r/** are two contrasting liquid phonemes (the most recent addition).

---

## 2. Typological grounding

Computed from the repo datasets (see `scripts/extract_data.sh`):

- **PHOIBLE** (N = 3,020 inventories) — every segment is high-frequency
  (e.g. /m/ 96 %, /k/ 90 %, /i/ 92 %, /a/ 86 %, /u/ 88 %); a two-liquid **/l r/
  contrast occurs in 39 %** of inventories (the plurality pattern).
- **WALS** — 14 consonants = a *small* inventory (1A); **/i a u/** is the single
  most common vowel system (2A); C/V ratio ≈ 4.7 (3A, moderately high).

The inventory is small but maximally naturalistic — nothing exotic, no marked gaps
now that liquids are present.

---

## 3. Next steps

Open design areas, to be decided from here:

1. **Allophony** — which surface phones are predictable allophones vs. phonemes
   (e.g. nasal place assimilation → [ŋ], intervocalic lenition, palatalization,
   vowel nasalization/laxing).
2. **Syllable structure** — template, clusters, diphthongs, Maximal Onset
   Principle, sonority hierarchy (Phonology 2).
3. **Prosody** — stress, weight/mora, length (Phonology 3–4).
