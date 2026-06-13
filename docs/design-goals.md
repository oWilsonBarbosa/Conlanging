# Design Goals: Proto-Sevelian

## Vision

A naturalistic **proto-language** in the mold of Proto-Indo-European: not a language
meant to be spoken on its own terms so much as a *reconstruction-shaped ancestor*
from which a family of daughter languages will be derived by regular sound change,
analogy, semantic shift, and grammaticalisation.

Working name: **Proto-Sevelian**, from the root *sew- "to flow" (derived noun
*sewél- "the flowing one; river") — the speakers are imagined as a river-valley
people. The name, like everything here, is revisable.

## Why diachronic-first design

Every choice in the proto-language is judged by one question: **what does it give
the daughters?** A proto-language that is too tidy produces boring descendants;
one that is a kitchen sink (see course unit 01a) produces incoherent ones. The
sweet spot is a *moderate inventory with built-in instabilities* — features that
are stable enough to reconstruct but famously prone to divergent development:

| Seeded feature | What daughters can do with it |
|---|---|
| Three stop series (voiceless / voiced / aspirated) | Chain shifts (Grimm-style), mergers, tone-from-voicing |
| Labiovelars /kʷ gʷ kʷʰ/ | Split to /p/-like or /k/-like outcomes (Greek vs. Latin style) |
| Laryngeals *h₁ h₂ h₃* | Vowel coloring + compensatory lengthening on loss; "laryngeal hardening" |
| Syllabic resonants *m̥ n̥ r̥ l̥* | Different epenthetic vowels per branch (am/em/un/...) |
| Ablaut *e ~ o ~ ∅ ~ ē ~ ō* | Fossilises into irregular paradigms (sing/sang/sung) |
| Free mobile pitch accent | Verner-style voicing splits, stress fixation, syncope of unaccented vowels |
| Single fricative /s/ | Room for daughters to *gain* fricatives via lenition/palatalisation |

## Principles

1. **Systematic, not maximal.** Changes and patterns apply to natural classes, not
   single sounds (course unit 11). The inventory stays balanced.
2. **Reconstruction aesthetics.** All forms are cited with `*`. Allophony is kept
   light — a proto-language is an abstraction, and fine phonetic detail is what
   the daughters are for.
3. **Naturalism over novelty.** Typologically attested patterns only; rarities are
   budgeted, not stacked.
4. **Data files drive tools.** `data/phonology.json` is machine-readable so that
   small scripts (root generator now, sound-change applier later) can be grown at
   pain points instead of building a framework up front.

## Roadmap

1. ✅ Phonology & phonotactics (this session) — `proto/01-phonology.md`, `proto/02-phonotactics.md`
2. Morphology sketch: fusional, ablauting; root-and-suffix structure
3. Verb system (TAM + agreement), noun system (case, number, class, alignment)
4. Core lexicon (~200 roots) with conceptual-metaphor flavor (unit 12)
5. Documentation pass: glossed example sentences in context (units 8, 13)
6. Daughter languages: per-branch sound-change sets (unit 11) + a sound-change
   applier tool when hand-derivation becomes the pain point
