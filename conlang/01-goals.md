# Lesson 1 — Goals

Course sources: `01 Introduction to Conlanging.pdf`, `01a The Greatest Conlang Ever.pdf`

Lesson 01a's whole argument is that a conlang is "good" when it is *as it should
be* — so before anything else, decide what it should be. This document is that
decision. Everything in Lessons 2–13 gets evaluated against it.

---

## The language

**Kelunta** — the lake tongue. Spoken by the **Keluri**, a lakeland people of
northwestern Meridia on Planet #06cy8vf7zvurfgpbrgnm4l. Full setting notes:
[`world/speakers.md`](world/speakers.md).

The name is provisional-but-committed: *kelu* "standing water, lake" + *-nta*.
Lesson 3 has to make that suffix real or the name changes.

---

## Classification (Lesson 01's taxonomy)

| Axis | This conlang |
|---|---|
| Inspiration | **A priori.** No lexicon or morphology derived from any real language. Typological *patterns* are borrowed freely — that is research, not derivation. |
| Means of expression | **Spoken**, with a writing system deferred (reed and clay surfaces are available in-world if I want one later). |
| Design goal | **Artlang**, specifically a fictional language supporting a worldbuilding project. |
| Naturalism | **Naturalistic.** Human speakers, human vocal tract, no feature that could not occur in a real language. |

---

## Goals

Lesson 01a asks for at least one goal in each of four categories.

### Naturalism
> Every feature must be attested somewhere in the world's languages, and the
> *combination* must be typologically coherent.

Concretely: I check features against WALS, Grambank, and PHOIBLE/BDPROTO before
committing them. The `data/` directory in this repo has all of them. Rare features
are allowed — one or two are what give a language character — but each one must
be paid for by being ordinary everywhere else. No feature enters because it is
cool.

### The speakers
> The grammar must reflect what the Keluri actually do all day.

The load-bearing commitment: **obligatory evidential marking on the verb**, because
Keluri water-rights reckoning is settled by testimony and the culture cares
intensely about how you know what you claim. Second commitment: the
**standing/leaving** contrast that organises their relationship to water should
surface somewhere in the grammar, not only in the dictionary.

### The medium
> Worldbuilding + personal enjoyment. No performers have to pronounce it, but a
> reader must be able to.

So: it needs enough depth to survive scrutiny from someone who reads the grammar,
and enough restraint that names and phrases in prose are readable at a glance. No
phonemes that require a diacritic key to interpret. Romanisation stays ASCII-safe
where possible.

### Aesthetics
> **Crisp and clean.** Finnish and Quechua as reference points, not as sources.

Clear vowel qualities, no voicing contrast to blur the consonants, modest
clusters, transparent syllable boundaries. The target is a language that *looks
spellable* — where hearing a word tells you how to write it and vice versa.

---

## Creative restraints

Lesson 01a counts self-imposed restraints as goals. Mine:

1. **Agglutinative.** One morpheme, one meaning, cleanly segmentable. Fusion is
   only allowed where sound change (Lesson 11) *produces* it — never by design.
2. **Suffixing.** Consistently. A language that suffixes its verbs and prefixes
   its nouns is a common enough natlang situation, but a single dominant affix
   position is what makes agglutination legible.
3. **No voicing contrast** in the consonant inventory. This is the single
   strongest constraint on the phonology and it is what will make the aesthetic
   goal achievable rather than aspirational.
4. **Non-accusative alignment.** Decided properly in Lesson 5 after reading the
   alignment material, but SAE-style nominative–accusative is off the table
   before I start, so that the choice gets made rather than defaulted into.

## Anti-goals

Named explicitly so I can be caught violating them:

- **Not a relex.** No morpheme-for-morpheme correspondence with English. If a
  Kelunta sentence glosses word-for-word into English, something has gone wrong.
- **Not a kitchen sink.** Every feature must justify itself against the goals
  above. When in doubt, cut.
- **Not SAE.** Specifically avoiding: definite/indefinite articles, a *have*-
  perfect, obligatory overt subject pronouns, do-support, comparative particles,
  and a nominative–accusative + dative case frame.

---

## Evaluation criteria

Lesson 01a's step 4 is "evaluate your goals," so here is what I will check
against at Lesson 8 (Documentation) and again at Lesson 13:

- [ ] Can I translate a paragraph of connected prose without inventing new
      grammar to do it?
- [ ] Does every feature trace back to a goal above?
- [ ] Would a linguist reading the grammar find the feature combination plausible?
- [ ] Do Keluri place names and personal names read cleanly in English prose?
- [ ] Is the evidential system actually used in every example sentence, or did it
      quietly become optional?

---

## Lesson 01a's questions, answered

**1. Scared puppy or bouncy puppy?**
Bouncy, structurally — the failure mode here is generating a lot of confident
material fast and only later noticing it does not cohere. The correction is the
evaluation checklist above and the discipline of checking features against the
typological databases in `data/` rather than against intuition.

**2. One goal from each category.** Above.

**3. Which BEATS step gets skipped?**
*Experiment.* The temptation is to go straight from Brainstorm to Apply — to
decide a feature is in before testing whether it collides with anything. The
mitigation: every new feature gets test-driven on example sentences in the same
lesson that introduces it, before it is written up as settled.

**4. When's the celebration party?**
Lesson 13, and the puppies are invited.

---

## Status

| Lesson | Topic | State |
|---|---|---|
| 01 / 01a | Introduction, goals | **done** |
| 02 | Phonology 1 — IPA | next |
| 03 | Morphology 1 | |
| 04 | Verbs 1 | |
| 05 | Nouns 1 — case, number, class, alignment | |
| 06 | Phonology 2 — designing a phonology | |
| 07 | Lexicon 1 | |
| 08 | Documentation 1 | |
| 09 | Verbs 2 | |
| 10 | Phonology 3 | |
| 11 | Phonology 4 — sound change | |
| 12 | Lexicon 2 | |
| 13 | Information structure | |
