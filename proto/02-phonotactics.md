# Proto-Sevelian Phonotactics

*(Course unit 6 — syllable structure, root canon, clusters, plus the ablaut
system that the morphology will build on.)*

## Syllable structure

**(C)(R)V(R)(C)** — where C is any consonant, R is a resonant (*m n r l y w*),
and V is a vowel or a syllabic resonant.

- No geminates.
- No vowel hiatus: adjacent vowels are broken by a glide or a laryngeal.
- Word-initially, **s + voiceless stop** onsets are additionally allowed
  (*st-, *sp-, *sk-, *skʷ-), including before R: *strew-.

## Root canon

Lexical roots take the shape **C₁(R)e(R)C₂ — minimally C₁eC₂**, cited in
e-grade with no accent mark. Examples: *sew- "flow", *deh₃- "give",
*pʰerkʷ- "ask".

Constraints (checked by `tools/wordgen.py`):

1. **No identical C₁ and C₂** (*ses- disallowed).
2. **No two voiced stops in one root** (*deg- disallowed; cf. the PIE root
   constraint). Voiceless and aspirated stops co-occur freely.
3. **Onset clusters rise in sonority**: C₁R- requires C₁ to be a non-resonant
   (stop, *s, or laryngeal). *mr-, *lw- are not legal onsets.
4. **Coda clusters fall in sonority**: -RC₂ with R a resonant and C₂ any
   non-resonant.
5. **No glide + matching vowel sequences** within the root nucleus (*yey-,
   *wow- disfavored; the generator rejects them).

## Legal clusters at a glance

| Position | Pattern | Examples |
|---|---|---|
| Onset | T R (stop + resonant) | *pr-, *kʷy-, *dʰ… → *tʰr-, *gl- |
| Onset | s T (word-initial) | *st-, *skʷ- |
| Onset | H R (laryngeal + resonant) | *h₂r-, *h₃w- |
| Coda | R T | *-rk, *-nt, *-ws |
| Coda | R H | *-rh₂, *-lh₁ |

Across morpheme boundaries larger clusters arise and are resolved by the
syllabic-resonant rule (e.g. */ph₂tr-su/ → [ph₂tr̥su]).

## Ablaut

Every root and many suffixes alternate through five grades; which grade appears
is determined by morphology and accent placement:

| Grade | Shape of *sew- "flow" | Shape of *pʰerkʷ- "ask" |
|---|---|---|
| **e-grade** (full) | *sew- | *pʰerkʷ- |
| **o-grade** | *sow- | *pʰorkʷ- |
| **zero-grade** | *su- | *pʰr̥kʷ- |
| **ē-grade** | *sēw- | *pʰērkʷ- |
| **ō-grade** | *sōw- | *pʰōrkʷ- |

- Zero-grade is only possible when a resonant (or laryngeal-colored nucleus) can
  carry the syllable; roots like *tek- have no usable zero-grade, which is fine —
  gaps like this breed analogy in the daughters.
- Accent generally sits on the full-grade syllable; zero-grade syllables are
  unaccented (*sewél- vs. *suléw-, hypothetical).

## Word shape

Words are root + (derivational suffix) + (inflection), each slot subject to the
syllable canon. Typical citation forms in documentation are root + thematic
vowel: *séwo- "flowing", *sewél- "river".

## Worked examples (generator output, curated)

| Root | Gloss placeholder | Zero-grade |
|---|---|---|
| *sew- | flow | *su- |
| *pʰerkʷ- | ask | *pʰr̥kʷ- |
| *deh₃- | give | *dh₃- |
| *kʷʰel- | turn | *kʷʰl̥- |
| *h₂ent- | front | *h₂n̥t- |
