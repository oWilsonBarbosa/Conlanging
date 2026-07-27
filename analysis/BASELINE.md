# Typological baseline

The modal (most common) value for every phonology parameter in the shipped
datasets. Use it as the reference point a design is measured against — being
modal is not a goal, but you should know which departures you are making.

Generated from `data/`: WALS v2020.4, PHOIBLE (dev-master), BDPROTO,
Phonotacticon 1.0.

## WALS phonology chapters — global sample

| # | parameter | modal value | share | n |
|---|---|---|---|---|
| 1A | Consonant inventories | Average | 36% | 563 |
| 2A | Vowel quality inventories | Average (5–6) | 51% | 564 |
| 3A | Consonant-vowel ratio | Average | 41% | 564 |
| 4A | Voicing in plosives and fricatives | In plosives alone | 33% | 567 |
| 5A | Voicing and gaps in plosive systems | None missing in /p t k b d g/ | 45% | 567 |
| 6A | Uvular consonants | None | 83% | 567 |
| 7A | Glottalized consonants | None | 72% | 567 |
| 8A | Lateral consonants | /l/, no obstruent laterals | 68% | 567 |
| 9A | The velar nasal | **No velar nasal** | 50% | 469 |
| 10A | Vowel nasalization | Contrast absent | 74% | 244 |
| 11A | Front rounded vowels | None | 93% | 562 |
| 12A | Syllable structure | Moderately complex | 56% | 486 |
| 13A | Tone | No tones | 58% | 527 |
| 14A | Fixed stress locations | No fixed stress | 44% | 502 |
| 15A | Weight-sensitive stress | Fixed stress (no weight-sensitivity) | 56% | 500 |
| 16A | Weight factors | No weight | 52% | 500 |
| 17A | Rhythm types | Trochaic | 47% | 323 |
| 18A | Absence of common consonants | All present | 89% | 567 |
| 19A | Presence of uncommon consonants | None | 79% | 567 |

Runners-up worth knowing, because they are where most non-modal languages go:

- **4A** is nearly a three-way tie — no voicing contrast 32%, both plosives and
  fricatives 28%. Voicing is genuinely open.
- **12A** Complex 31%, Simple (CV only) **13%**.
- **14A** Penultimate 22%, Initial 18%, Ultimate 10%, Second 3%,
  **Antepenultimate 2%**, Third 0.2%.
- **13A** Simple tone 25%, complex tone 17% — so 42% of languages have tone.

WALS does not ship the numeric ranges behind "Average" for 1A and 3A, so use
the PHOIBLE figures below for anything quantitative.

## Quantitative modals

### PHOIBLE — 2,176 languages (one inventory per Glottocode)

| measure | median | mean | IQR | range |
|---|---|---|---|---|
| total segments | 32 | 34.5 | 25–41 | 11–161 |
| consonants | 21.5 | 23.7 | 17–27 | 6–130 |
| vowels | 9 | 10.1 | 6–12 | 2–50 |
| C/V ratio | 2.57 | 3.05 | 1.69–3.83 | — |

Modal vowel count 6 (291 languages), then 5 (258). Modal consonant count 20
(154), then 17 (150).

Note the vowel median of 9 counts every vowel *segment*, including length and
nasalization contrasts — it is not comparable to WALS 2A, which counts vowel
*qualities* and puts the mode at 5–6.

### BDPROTO — 268 reconstructed proto-languages

| measure | median | mean | IQR | range |
|---|---|---|---|---|
| total segments | 28 | 29.0 | 21–35 | 4–90 |

Reconstructed proto-languages are only slightly smaller than modern ones. A
minimal inventory is not what a proto-language typically looks like.

### Phonotacticon 1.0 — 457 lects

**Eurasia only.** The published database covers 516 lects spoken in Eurasia, so
every figure here is areal, not global. For syllable structure globally, use
WALS 12A instead.

| measure | median | IQR | range |
|---|---|---|---|
| simple (single-segment) onsets | 24 | 20–30 | 1–65 |
| simple codas | 13 | 8–22 | 1–49 |
| max onset length | 2 | 1–3 | 0–58 |
| max coda length | 1 | 1–2 | 0–53 |

Modal max onset 2 segments (170 lects), then 1 (144). Modal max coda 1 (226),
then 2 (134).

Codas: 391 of 457 lects (85.6%) have real segmental codas; 20 (4.4%) explicitly
have none. In this dataset `#` is the null marker meaning the position may be
empty — it is not a segment, and counting it inflates both inventory sizes and
the share of languages "having codas".

## Reading these numbers

- **Modal is not a target.** Half of WALS's parameters have a modal value under
  55%, meaning most languages depart from the majority on something.
- **Independence is not guaranteed.** These are marginal distributions. Being
  modal on fifteen parameters separately does not make a combination common,
  and some parameters interact strongly (codas create syllable weight, which
  interacts with stress).
- **Samples differ.** WALS is global but coarse; PHOIBLE is large but not
  areally balanced; Phonotacticon is fine-grained but Eurasian; BDPROTO is
  reconstructions, with the biases reconstruction carries.
