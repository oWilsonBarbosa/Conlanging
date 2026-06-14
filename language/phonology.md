# Phonology

> Living reference — current state of the sound system. Updated from the Phonology
> lessons (CU 02, 06, 10, 11). Rationale and sources live in [`design/`](design/).
>
> Status: **inventory (L02) + phonotactics (L06) set; revised in the morphophonology
> pass (see [`design/03b-morphophonology.md`](design/03b-morphophonology.md)).**
> Suprasegmentals & processes still TBD (L10/11).

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
- **Fricatives f s x h** span labial→glottal; all voiceless.
- All segments validated as well-formed BIPA against CLTS.

## Vowels

A minimal **/a i u/** triangle, contrasting in **length** only.
(Nasal vowels were **removed** in the morphophonology revision.)

| | Front | Central | Back |
|---|---|---|---|
| Close | i · iː | | u · uː |
| Open | | a · aː | |

**Diphthongs (6, all falling / head-initial** — first element is the moraic nucleus,
second is an offglide):

> ai · au · ia · iu · ua · ui

> Note: cross-linguistically *ia/ua* are usually *rising*; Alantian deliberately treats
> all six as falling (prominence on the first mora) for a uniform, chant-like cadence.
> The vowels, diphthongs, and syllabic sonorants form the **ablaut grade ladder** used
> in derivation/inflection — see `grammar.md` → Morphology.

## Syllable nuclei & the moraic system

Alantian is **mora-timed**; weight is phonemic and comes from several sources:

| Nucleus / structure | Moras |
|---|---|
| Short vowel (a i u) | 1 |
| **Syllabic sonorant** (m̩ n̩ l̩ r̩) | 1 |
| Long vowel (aː iː uː) | 2 |
| Diphthong (ai, au, …) | 2 |
| Coda consonant, or **geminate** (any C: pp tt kk … mm ll ss) | +1 |

**Syllabic sonorants** (Sanskrit/PIE-style *ṛ ḷ ṃ ṇ*) can head a syllable on their own,
adding a ringing, vowel-like resonance. Geminates add weight on the consonant side, and
**any consonant may geminate** (see Phonotactics).

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
> **sonorant** coda (an.ka), or an **/s/** coda (as.ka) are all fine. This is the
> Japanese-style "coda = moraic sonorant / sibilant / geminate-half" pattern.

> **Roots vs. syllables:** a **root** may be **CVRC** (L03), but that is a *morpheme*
> shape, not a syllable. A CVRC root's final C surfaces as an **onset** under suffixation
> (*tarn-a* → *tar.na*) and resolves word-finally via a syllabic sonorant / epenthesis.

### Medial clusters (coda + onset)

Across a syllable boundary: **{m n l r s} + C**, plus geminates **C₁C₁** —
*an.ta, as.pa, al.ma, at.ta, ak.kʰa*.

### Geminates

**Any consonant may geminate** (coda-half + identical onset):
pp tt kk · bb dd gg · ff ss xx · mm nn ll rr. The glides **/w j/**, **/h/**, and **/ʔ/**
do **not** geminate. A geminate adds one mora (heavy syllable). An aspirated geminate
surfaces as unaspirated hold + aspirated release [p.pʰ] (written *pph, tth, kkh*).

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

### Revised from earlier lessons (morphophonology pass)

- **Nasal vowels removed** — vowels contrast in length only.
- **Geminates generalized** — *any* consonant may geminate (not just sonorants + s).
- **Coda licensing** restated as CV(R) + /s/ + geminate-half.

## Suprasegmentals

_Stress vs. pitch accent — **deferred** to Lessons 10/11. Given the moraic design and
the Greek/Vedic model, weight-sensitive **pitch accent** is a strong candidate._

## Phonological processes

_Allophony (e.g. /n/ → [ŋ] before velars), assimilation — TBD. **Consonant gradation**
and **vowel harmony** are under decision (see `grammar.md` → Morphology)._

## Romanization (provisional)

- Aspirated stops → digraphs **ph th kh**; plain **p t k**, voiced **b d g**;
  glottal stop /ʔ/ → **ʼ**.
- Fricatives **f s x h** (x = velar [x]).
- Long vowels → macron **ā ī ū**.
- Syllabic sonorants → under-dot **ṃ ṇ ḷ ṛ**.
- Geminates → doubled letters (aspirated geminates → *pph tth kkh*); diphthongs written
  as the vowel pair (*ai, au, …*).
- Examples: /tʰaː.ras/ → *thāras* · /al.la/ → *alla* · /at.ti/ → *atti* ·
  /ta.r̩n/ → *taṛn* (syllabic *ṛ*) · /pʰai.tu/ → *phaitu* (diphthong).
