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

**Ablaut (nucleus gradation).** The vowels, diphthongs, and syllabic sonorants form a
graded ladder; shifting a root's nucleus grade marks grammatical categories
(Sanskrit *guṇa/vṛddhi*, PIE-style). Functions per grade are fixed in L04/L05.

| Grade | i-root | u-root | a-root | CVRC root |
|---|---|---|---|---|
| **Zero** (weak) | ∅ / i̯ | ∅ / u̯ | ∅ | syllabic R (*tarn* → *tṛn*) |
| **Full** (basic) | i | u | a | a (*tarn*) |
| **Strong** (guṇa) | ai | au | ā | ā (*tārn*) |
| **Long** (vṛddhi) | āi | āu | ā | — |

> Example schema (functions placeholder): *kis-* (zero *ks-*, full *kis-*, strong
> *kais-*, long *kāis-*) — one root, four grades doing grammatical work.

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
- **Vowel harmony** and **consonant gradation** — *under decision* (see design/03b);
  options being weighed for how affix vowels / stem consonants alternate.

## Nouns

_Case, number, class/gender — TBD (Lesson 05)._

## Verbs

_TAM, agreement, valency — TBD (Lessons 04, 09)._

## Syntax

_Phrase structure, clause combining — TBD._

## Information structure

_Topic/focus, word-order flexibility — TBD (Lesson 13)._
