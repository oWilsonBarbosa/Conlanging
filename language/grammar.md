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

Alantian is **agglutinative**: affixes are clean and separable, carry **one meaning
each**, and **stack in ordered slots** with minimal fusion. Grammar sits at **both
edges** of the word.

### Word template (slots)

```
NEG – AGR – ASP/MOOD – [ ROOT ] – DERIV – NUMBER – CASE
└──────── prefixes ────────┘        └──────── suffixes ────────┘
```

- **Prefixes** carry person **agreement**, **negation**, and **aspect/mood**.
- **Suffixes** carry **derivation**, **number**, and **case**.
- Each affix is recoverable; specific paradigms are set in later lessons (Nouns L05,
  Verbs L04/09).

### Root typology

| Shape | Frequency | Example | Notes |
|---|---|---|---|
| **CV** | rare, archaic ("primitive" layer) | *ta, ku, si* | oldest roots; light (1 mora) |
| **CVC** | default / most common | *tʰar, sal, men, kus* | the workhorse root |
| **CVRC** | sonorant + final C | *tarn, kʰuls, mirk* | final cluster is **split by suffixation** |

R = a sonorant {m n l r}. A **CVRC** root shows its final consonant before vowel-initial
material (*tarn-a* → *tar.na*) and resolves word-finally via a **syllabic sonorant** or
epenthesis (*tarn* → *tar.ṇ* / *ta.ran*) — Sanskrit/PIE-style root behaviour.

### Morphophonology

Agglutination feeds the Lesson 06 rules automatically:

- Vowel-initial suffix after a vowel-final root → **coalescence** (long V / diphthong)
  or an epenthetic **/ʔ/** across a morpheme boundary.
- Boundary consonant sequences are syllabified as legal `{m n l r s} + C` clusters or
  repaired; CVRC roots split as above.
- **Vowel harmony:** _open question_ — whether suffix vowels assimilate to the root
  (e.g. rounding harmony) is deferred to a morphophonology pass.

## Nouns

_Case, number, class/gender — TBD (Lesson 05)._

## Verbs

_TAM, agreement, valency — TBD (Lessons 04, 09)._

## Syntax

_Phrase structure, clause combining — TBD._

## Information structure

_Topic/focus, word-order flexibility — TBD (Lesson 13)._
