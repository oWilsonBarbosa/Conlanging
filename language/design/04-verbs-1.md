# Lesson 04 — Verbs 1 (Tense & Aspect)

- **CU lesson:** <https://sites.google.com/view/conlangs-university/lessons> (Verbs 1)
- **Date:** 2026-06-14
- **Goal:** set Alantian's tense and aspect systems (mood/voice/agreement come later).

## Decisions (settled)

- **Tense — absolute: past / non-past** (binary), **plus relative tense** on non-finite
  forms (anterior / simultaneous / posterior, anchored to the matrix clause).
- **Aspect — perfective / imperfective / perfect** (three Greek/Sanskrit-style stems).
- **Stem building (reuses existing machinery):**
  - Imperfective ← **nasal infix ‹-N-›** (*tap* → *tanpa*)
  - Perfective ← **plain/ablaut grade** (*tappa*)
  - Perfect ← **reduplication + ā-grade** (*tatāpa*) — adopts reduplication (the one new tool)
- **Finite TAM grid** = past/non-past × pfv/ipfv/perfect (2 × 3, six cells).

## Tense realisation — reduplicative & diachronic (revised)

Tense is built by **reduplicating one edge** of the stem, with regular sound change
applying (see `../diachrony.md`):

- **Non-past = final-syllable reduplication** → medial geminate (*tapa* → **tappa**).
- **Past = initial-syllable reduplication** → initial cluster/diphthong (*tapa* →
  **taipa**).

Replaces the *‑pa/‑ta* suffix and augment ideas. Coda resolution = place vocalization
(labial→u, velar→u, coronal→i; identical→geminate; sonorant/s = legal coda).

- **Future = non-past perfective** (Slavic-style emergent future). **Open.**
- Open: reduplication now marks **tense**, so the **perfect** aspect needs another
  exponent (ablaut?); tense × aspect interaction generally.

## Worked paradigm — root *tap‑* "to strike"

| | Perfective | Imperfective | Perfect |
|---|---|---|---|
| Past (*a‑*) | a-tappa | a-tanpa | a-tatāpa |
| Non-past | tappa "will strike" | tanpa "strikes" | tatāpa "has struck" |

Consonant gradation surfaces automatically: tappa (geminate/strong), tanpa (singleton —
infix fills coda), tatāpa (singleton — heavy nucleus). All forms phonotactically legal.

## Characterization vs. real languages

| Trait | Parallel |
|---|---|
| Three aspect stems (ipfv/pfv/perfect) | **Ancient Greek, Sanskrit** |
| Past augment prefix | **Greek** é-, Vedic a- |
| Reduplicated perfect | **Greek, Sanskrit, Latin** |
| Future from non-past perfective | **Slavic** |
| Relative tense on participles | **Greek/Sanskrit** participle systems |

## Sources consulted

| Source | What | How it informed |
|---|---|---|
| WALS 65A (perfective/imperfective), 66A (past tense) | Distribution of aspect & past marking | Grounds the pfv/ipfv + past/non-past design |
| WALS 68A (the perfect) | Perfect as a cross-linguistic category | Supports treating perfect as its own stem |
| Grambank | Presence of aspect stems, augments, reduplication | Validates the stem-based, reduplicating design |

> Provenance only — no paradigms copied; system is original.

## Outputs

- [x] `grammar.md` — Verbs: tense, aspect stems, TAM grid, relative tense
- [ ] mood, voice, agreement, valency (rest of L04 / L09)

## Open questions

- Future: emergent (non-past pfv) vs dedicated prospective?
- Exact augment form; behaviour before vowel-initial roots (hiatus → coalescence/ʔ).
- Reduplication shape (full CV- copy? fixed vowel?).
- Mood / voice / agreement (next).

## License note

Nothing reproduced from external sources; typological comparison only.
