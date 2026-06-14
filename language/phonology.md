# Phonology

> Living reference — current state of the sound system. Updated from the Phonology
> lessons (CU 02, 06, 10, 11). Rationale and sources live in [`design/`](design/).
>
> Status: **inventory (Lesson 02) and phonotactics (Lesson 06) set.** Suprasegmentals
> and processes still TBD (Lessons 10/11).

## Consonants (20)

| Manner | Labial | Alveolar | Palatal | Velar | Glottal |
|---|---|---|---|---|---|
| Plosive, aspirated | pʰ | tʰ | | kʰ | |
| Plosive, voiceless | p | t | | k | ʔ |
| Plosive, voiced | b | d | | g | |
| Fricative | f | s | | x | h |
| Nasal | m | n | | (ŋ) | |
| Liquid | | l r | | | |
| Glide | w¹ | | j | w¹ | |

¹ /w/ is labial–velar. /ŋ/ is **not phonemic** — it is an allophone of /n/ before velars.

- **Three-way laryngeal contrast** (aspirated / voiceless / voiced) on the stops —
  the Classical Greek system (φ π β, θ τ δ, χ κ γ), plus a glottal stop /ʔ/.
- **Fricatives f s x h** span labial→glottal; all voiceless (no voiced fricatives),
  keeping an archaic, "breathy" texture.
- All segments validated as well-formed BIPA against CLTS.

## Vowels

A minimal **/a i u/** triangle, contrasting in **length** and **nasality**.

| | Front | Central | Back |
|---|---|---|---|
| Close | i  iː  ĩ | | u  uː  ũ |
| Open | | a  aː  ã | |

**Diphthongs (6, all falling / head-initial** — first element is the moraic nucleus,
second is an offglide):

> ai · au · ia · iu · ua · ui

> Note: cross-linguistically *ia/ua* are usually *rising*; Alantian deliberately treats
> all six as falling (prominence on the first mora) for a uniform, chant-like cadence.

## Syllable nuclei & the moraic system

Alantian is **mora-timed**; weight is phonemic and comes from several sources:

| Nucleus / structure | Moras |
|---|---|
| Short vowel (a i u) or short nasal vowel | 1 |
| **Syllabic sonorant** (m̩ n̩ l̩ r̩) | 1 |
| Long vowel (aː iː uː) | 2 |
| Diphthong (ai, au, …) | 2 |
| Coda consonant, or **geminate** (mm nn ll rr ss) | +1 |

**Syllabic sonorants** (Sanskrit/PIE-style *ṛ ḷ ṃ ṇ*) can head a syllable on their own,
adding a ringing, vowel-like resonance. Geminates add weight on the consonant side but
are limited to the coda-legal set (see Phonotactics).

## Phonotactics

### Syllable template — (C)V(C)

Optional single onset, obligatory nucleus, optional single coda. **No tautosyllabic
clusters.** (WALS 12A: *moderately complex*, at the simple end — codas allowed, onset
clusters not.)

- **Onset:** any single consonant (optional).
- **Nucleus:** short / long / nasal vowel, a falling diphthong, or a syllabic sonorant.
- **Coda:** at most one of **{m n l r s}** — sonorants + /s/ (realized [ŋ] before a velar).

> **Automatic consequence:** since only {m n l r s} may close a syllable, **every
> obstruent (stops, f x h, ʔ) is onset-only.** Aspirates and voiced stops never end a
> syllable — so syllables open clean and close on a ringing or sibilant sound.

### Medial clusters (coda + onset)

Clusters occur only across a syllable boundary — a legal coda + any onset:
*an.ta, ar.kʰa, as.pa, al.ma, is.tʰu*. Permitted shape: **{m n l r s} + C**.

### Geminates

A geminate = coda + identical onset, so geminates are limited to the coda-legal set:
**mm nn ll rr ss** (*amma, anna, alla, arra, assa*). Geminate stops are impossible
(no stop coda) — reinforcing the resonant aesthetic.

### Hiatus resolution

Vowel + vowel never surfaces as two open syllables; it resolves:

1. **Identical → long vowel:** a+a → ā, i+i → ī, u+u → ū.
2. **Distinct → falling diphthong:** a+i → ai, a+u → au, i+a → ia, i+u → iu,
   u+a → ua, u+i → ui. (The six distinct vowel pairs *are* Alantian's six diphthongs.)
3. **To keep vowels apart** across a morpheme boundary, an epenthetic **/ʔ/** is
   inserted instead: a+a → aʔa. (This is the glottal stop's primary job.)

### Weight (moras)

- **Light (1 mora):** (C)V, or a syllabic sonorant (C̩).
- **Heavy (2 moras):** (C)Vː, (C)+diphthong, or a closed syllable (C)VC.
- Syllabic sonorants surface where a sonorant has no adjacent vowel (PIE/Sanskrit-style).

### Settled from Lesson 02

- **Nasal vowels are short only** — long-nasal vowels (ãː ĩː ũː) do **not** occur.

## Suprasegmentals

_Stress vs. pitch accent — **deferred** to Lessons 10/11. Given the moraic design and
the Greek/Vedic model, weight-sensitive **pitch accent** is a strong candidate._

## Phonological processes

_Allophony (e.g. /n/ → [ŋ] before velars), assimilation — TBD._

## Romanization (provisional)

- Aspirated stops → digraphs **ph th kh**; plain **p t k**, voiced **b d g**;
  glottal stop /ʔ/ → **ʼ**.
- Fricatives **f s x h** (x = velar [x]).
- Long vowels → macron **ā ī ū**; nasal vowels → tilde **ã ĩ ũ**.
- Syllabic sonorants → under-dot **ṃ ṇ ḷ ṛ**.
- Geminates → doubled letters; diphthongs written as the vowel pair (*ai, au, …*).
- Examples: /tʰaː.ras/ → *thāras* · /al.la/ → *alla* · /mi.ʔũ/ → *miʼũ* (hiatus break) ·
  /ta.r̩n/ → *taṛn* (syllabic *ṛ*) · /pʰai.tu/ → *phaitu* (diphthong).
