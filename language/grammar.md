# Grammar

> Living reference — current state of morphology & syntax. Updated from the Morphology,
> Nouns, Verbs, and Information Structure lessons. Rationale and sources live in
> [`design/`](design/).

## Typological profile

> Quick summary of the big parameters, each tagged with the WALS/Grambank feature it
> was decided against (provenance, not copied data).

| Parameter | Value | Source ref |
|---|---|---|
| Basic word order | _TBD_ | WALS 81A |
| Morphological type | **Agglutinative** | WALS 20A (fusion) |
| Affix position | **Both** prefixes & suffixes | WALS 26A |
| Alignment | _TBD_ | WALS 98A / Grambank |
| Head/dependent marking | _TBD_ | WALS 23A |

## Morphology

Alantian is **agglutinative at its core** (clean, separable, one-meaning affixes that
stack in ordered slots), with a **non-concatenative layer** — **ablaut** (nucleus
gradation) and **infixation** — layered on top. The mix is Sanskrit/PIE-like: regular
affixation plus root-internal vowel grades. Grammar sits at **both edges** *and inside*
the word.

### Word template (slots)

```
NEG – AGR – ASP/MOOD – [ C ‹INFIX› …root… ]root+ABLAUT – DERIV – NUMBER – CASE
└──────── prefixes ────────┘   └─ infix inside root ─┘            └──── suffixes ────┘
```

- **Prefixes** carry person **agreement**, **negation**, and **aspect/mood**.
- **Infix(es)** sit inside the root (after the first consonant, or before the final
  root consonant), carrying e.g. aspect/plurality — see below.
- **Ablaut** changes the root **nucleus grade** (see ladder) to mark derivation/inflection.
- **Suffixes** carry **derivation**, **number**, and **case**.
- Each affix is recoverable; specific paradigms are set in later lessons (Nouns L05,
  Verbs L04/09).

### Non-concatenative morphology

**Ablaut (nucleus gradation).** A root's nucleus takes one of **four grades**, formed by
**colouring the base vowel** with ∅ / i / u / a and then resolving by the regular hiatus
rules. The four grades regenerate exactly Alantian's 3 plain + 3 long + 6 diphthong
nuclei. Functions per grade are fixed in L04/L05.

| base ＼ grade | plain (∅) | i-grade (+i) | u-grade (+u) | a-grade (+a) |
|---|---|---|---|---|
| **a** | a | ai | au | ā |
| **i** | i | ī | iu | ia |
| **u** | u | ui | ū | ua |

(So i-grade of /a/ = a+i = *ai*; i-grade of /i/ = i+i = *ī*; a-grade of /i/ = i+a = *ia*.
The a-offglide in *ia/ua* may be written with a breve — *iă, uă*.) Ablaut targets the
root vowel in any root shape (CV, CVC, CVRC alike).

> Example: root **kis-** → plain *kis*, i-grade *kīs*, u-grade *kius*, a-grade *kias* —
> one root, four grades doing grammatical work.

**Consonant gradation (3 grades).** A plain voiceless stop **p t k** that heads a
syllable alternates by the shape of that syllable — a Finnic-style system that uses
**both** gemination and lenition (so geminates = strong grade, fricatives = weak grade):

| Grade | p | t | k | Environment |
|---|---|---|---|---|
| **Strong** (geminate) | pp | tt | kk | before a light **open** syllable (adds weight) |
| **Basic** (singleton) | p | t | k | after a heavy nucleus (long V / diphthong); default |
| **Weak** (lenited) | f | s | x | before a **closed** syllable (suffix adds a coda) |

Examples (root *kap-* 'stone'): *kap+a* → **kappa** (open → strong) ·
*kap+an* → **kafan** (closed → weak) · *kāp+a* → **kāpa** (heavy nucleus → basic).
Voiced stops, aspirates, sonorants and /s/ stand outside the productive alternation
(details TBD).

**Infixation.** An infix is inserted **inside the root**. Default model: a **nasal infix
‹-N-›** placed before the final root consonant (PIE-style), surfacing as the coda
sonorant — e.g. root *tak-* → *tank-* (→ *tan.ka* when suffixed). Marks e.g.
imperfective/durative. The full infix inventory is set in the verb/noun lessons.

### Root typology

| Shape | Frequency | Example | Notes |
|---|---|---|---|
| **CV** | rare, archaic ("primitive" layer) | *ta, ku, si* | oldest roots; light (1 mora) |
| **CVC** | default / most common | *tʰar, sal, men, kus* | the workhorse root |
| **CVRC** | sonorant + final C | *tarn, kʰuls, mirk* | final cluster is **split by suffixation** |

R = a sonorant {m n l r}. A **CVRC** root shows its final consonant before vowel-initial
material (*tarn-a* → *tar.na*) and resolves word-finally via a **syllabic sonorant** or
epenthesis (*tarn* → *tar.ṇ* / *ta.ran*) — Sanskrit/PIE-style root behaviour. (Root shape
≠ syllable shape, which is CV(R); see `phonology.md`.)

### Morphophonology

Agglutination feeds the Lesson 06 rules automatically:

- Vowel-initial suffix after a vowel-final root → **coalescence** (long V / diphthong)
  or an epenthetic **/ʔ/** across a morpheme boundary.
- Boundary consonant sequences are syllabified as legal `{m n l r s} + C` clusters,
  geminates, or repaired; CVRC roots split as above.
- **Vowel harmony:** none — suffix vowels are fixed (ablaut already supplies the
  root-internal vowel play). **Consonant gradation:** active, 3-grade (geminate ↔
  singleton ↔ fricative); see above.

## Nouns

_Case, number, class/gender — TBD (Lesson 05)._

## Verbs

> Tense + aspect are set (L04); **mood, voice, agreement, valency** still TBD.

### Tense — absolute: past / non-past

Binary, built by **reduplicating one edge of the stem** (regular sound change then
applies — see [`diachrony.md`](diachrony.md)):

- **Non-past = final-syllable reduplication** → a **medial geminate**: *tapa* → **tappa**.
- **Past = initial-syllable reduplication** → an **initial cluster / diphthong**:
  *tapa* → *tatpa* → **taipa**.

(This replaces the earlier *‑pa/‑ta* suffix and augment ideas — tense is **reduplicative**.)

### Aspect — perfective / imperfective / perfect (three stems)

Greek/Sanskrit-style aspect stems, built from the existing machinery:

| Aspect | Built with | *tap‑* "strike" |
|---|---|---|
| **Imperfective** (ongoing/habitual) | nasal infix ‹-N-› | *tanpa* |
| **Perfective** (whole/packaged) | plain/ablaut grade | *tappa* |
| **Perfect** (prior + relevant) | **reduplication** + ā-grade | *tatāpa* |

Consonant gradation falls out automatically: *tappa* (geminate, strong) · *tanpa*
(singleton — infix fills the coda) · *tatāpa* (singleton — after a heavy nucleus).

### Finite TAM grid (2 × 3)

| | Perfective | Imperfective | Perfect |
|---|---|---|---|
| **Past** (initial redup) | aorist "struck" | imperfect "was striking" | pluperfect "had struck" |
| **Non-past** (final redup) | **future** "will strike" | present "strikes" | pres. perfect "has struck" |

> **Future is emergent:** non-past + perfective reads as future (Slavic-style); no
> dedicated future tense needed. *(Alternative: a separate prospective marker — open.)*

> **Realisation note:** tense = **edge reduplication** (diachronic — see `diachrony.md`):
> N.PST *tap‑* = **tappa**, PST = **taipa**. Since reduplication now marks tense, the
> **perfect** aspect needs another exponent (ablaut grade?) — open, with the rest of the
> tense × aspect interaction.

### Relative tense — non-finite forms

Participles/converbs encode time **relative to the matrix clause** (not to "now"):

| Relative | Meaning | Aspect pairing |
|---|---|---|
| **Anterior** | before the main event ("having struck") | perfect / perfective |
| **Simultaneous** | during ("while striking") | imperfective |
| **Posterior** | after / about to ("about to strike") | prospective |

### Still TBD

Mood (indic / subjunctive / optative / imperative), voice (active / middle / …),
person agreement (mono- vs polypersonal), valency/derivation. → rest of L04 + L09.

## Syntax

_Phrase structure, clause combining — TBD._

## Information structure

_Topic/focus, word-order flexibility — TBD (Lesson 13)._
