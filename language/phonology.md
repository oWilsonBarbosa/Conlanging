# Phonology

> Living reference — current state of the sound system. Updated from the Phonology
> lessons (CU 02, 06, 10, 11). Rationale and sources live in [`design/`](design/).
>
> Status: **inventory + phonotactics set; revised** (morphophonology pass, then an
> inventory revision removing aspirates, /ʔ/, and syllabic sonorants). Suprasegmentals
> & processes still TBD (L10/11).

## Consonants (16)

| Manner | Labial | Alveolar | Palatal | Velar | Glottal |
|---|---|---|---|---|---|
| Plosive, voiceless | p | t | | k | |
| Plosive, voiced | b | d | | g | |
| Fricative | f | s | | x | h |
| Nasal | m | n | | (ŋ) | |
| Liquid | | l r | | | |
| Glide | w¹ | | j | | |

¹ /w/ is labial–velar. /ŋ/ is **not phonemic** — an allophone of /n/ before velars.

- **Two-way laryngeal contrast** (voiceless / voiced) on the stops — p b, t d, k g
  (a Latin-like system; the old aspirated series and /ʔ/ are removed).
- **Fricatives f s x h** span labial→glottal; all voiceless.
- All segments validated as well-formed BIPA against CLTS.

## Vowels

A minimal **/a i u/** triangle, contrasting in **length** only (no nasal vowels).

| | Front | Central | Back |
|---|---|---|---|
| Close | i · iː | | u · uː |
| Open | | a · aː | |

**Diphthongs (6, all falling / head-initial):** ai · au · ia · iu · ua · ui.

> The vowels, long vowels, and diphthongs form the **ablaut grade ladder** used in
> derivation/inflection — see `grammar.md` → Morphology.

## Syllable nuclei & the moraic system

Alantian is **mora-timed**; weight is phonemic:

| Nucleus / structure | Moras |
|---|---|
| Short vowel (a i u) | 1 |
| Long vowel (aː iː uː) | 2 |
| Diphthong (ai, au, …) | 2 |
| Coda consonant, or **geminate** (any C: pp tt kk … mm ll ss) | +1 |

Nuclei are vowels only (short, long, diphthong) — **sonorants are no longer syllabic**.
Any consonant may geminate (see Phonotactics).

## Phonotactics

### Syllable template — (C)V(C₁), basically CV(R)

Optional single onset, obligatory nucleus, optional single coda. **No tautosyllabic
clusters.** The coda **C₁** is licensed only if it is:

1. a **sonorant R {m n l r}** — the basic, unmarked coda (so the core shape is **CV(R)**;
   realized [ŋ] before a velar); **or**
2. **/s/** — the one plain obstruent that may close a syllable; **or**
3. the **first half of a geminate** — *any* consonant, when the following onset is
   identical (C₁C₁).

> So a plain obstruent coda is illegal (\*at.ka), but a **geminate** (at.ta), a
> **sonorant** coda (an.ka), or an **/s/** coda (as.ka) are all fine.

> **Roots vs. syllables:** a **root** may be **CVRC** (L03), but that is a *morpheme*
> shape. Its final C surfaces as an **onset** under suffixation (*tarn-a* → *tar.na*) and
> resolves word-finally via **epenthesis** (*tarn* → *ta.ran*).

### Medial clusters (coda + onset)

Across a syllable boundary: **{m n l r s} + C**, plus geminates **C₁C₁** —
*an.ta, as.pa, al.ma, at.ta, ak.ka*.

### Geminates

**Any consonant may geminate** (coda-half + identical onset):
pp tt kk · bb dd gg · ff ss xx · mm nn ll rr. The glides **/w j/** and **/h/** do **not**
geminate. A geminate adds one mora (heavy syllable).

### Hiatus resolution

Vowel + vowel never surfaces as two open syllables; it **coalesces**:

1. **Identical → long vowel:** a+a → ā, i+i → ī, u+u → ū.
2. **Distinct → falling diphthong:** a+i → ai, a+u → au, i+a → ia, i+u → iu,
   u+a → ua, u+i → ui.

> With /ʔ/ removed, there is no epenthetic break — sequences simply coalesce. *(Whether a
> homorganic glide /j w/ may instead surface to keep vowels apart is **open**.)*

### Weight (moras)

- **Light (1 mora):** (C)V.
- **Heavy (2 moras):** (C)Vː, (C)+diphthong, or a closed syllable (C)VC.

### Revised from earlier lessons

- **Nasal vowels removed**; vowels contrast in length only.
- **Geminates generalized** — any consonant may geminate.
- **Coda licensing** = CV(R) + /s/ + geminate-half.
- **Inventory revision:** aspirated stops, /ʔ/, and **syllabic sonorants removed**.

## Suprasegmentals

_Stress vs. pitch accent — **deferred** to Lessons 10/11. The diachrony assumes
**initial stress** in the proto-stage (see `diachrony.md`)._

## Phonological processes

_Allophony (e.g. /n/ → [ŋ] before velars), assimilation — TBD. **Consonant gradation**
is active (see `grammar.md` → Morphology); no vowel harmony._

## Romanization (provisional)

- Voiceless **p t k**, voiced **b d g**; fricatives **f s x h** (x = velar [x]).
- Long vowels → macron **ā ī ū**.
- Geminates → doubled letters; diphthongs written as the vowel pair (*ai, au, …*).
- Examples: /taː.ras/ → *tāras* · /al.la/ → *alla* · /at.ti/ → *atti* ·
  /pai.tu/ → *paitu* (diphthong) · /ta.ran/ → *taran*.
