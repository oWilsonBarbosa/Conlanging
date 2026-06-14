# Lesson 02 — Phonology 1

- **CU lesson:** <https://sites.google.com/view/conlangs-university/lessons> (Phonology 1)
- **Date:** 2026-06-14
- **Goal:** fix Alantian's phoneme inventory (segments + length), grounded in PHOIBLE/CLTS.

## Decisions

- **Inventory size:** small–medium, classic.
- **Consonants (15):** p b t d k g · s h · m n ŋ · l r · w j.
- **Vowels (5 + length):** i e a o u, each short and long (iː eː aː oː uː).
- **Length on both tiers:** phonemic **vowel length** *and* **geminate consonants** →
  maximally moraic.
- **Suprasegmentals:** deferred to Lessons 10/11.

## Sources consulted

| Source | What I looked at | How it informed the decision |
|---|---|---|
| PHOIBLE | Cross-linguistic frequency of segments & the 5-vowel /i e a o u/ system | Picked the single most common vowel system and high-frequency consonants → typologically natural, "classic" base |
| PHOIBLE | Prevalence of /p t k (b d g)/, /m n ŋ/, /s h/, /l r/, /w j/ | Chose a sonorant-rich but unmarked consonant set; avoided rare/marked segments to keep it smooth/elevated |
| CLTS (BIPA) | Validity of every chosen symbol | Confirmed all 15 consonants + 10 vowels are well-formed BIPA; romanization maps cleanly |

> Provenance only — no inventory was copied from any language in PHOIBLE; segment
> *choices* were guided by cross-linguistic frequency.

## Rationale

A 5-vowel system with length plus a 15-consonant set whose sonorants (m n ŋ l r w j)
outnumber its fricatives gives the **resonant, ringing** quality. Contrastive vowel
length and geminates make **weight** phonemic, delivering the **moraic** rhythm. Keeping
everything to high-frequency, unmarked segments reads as **classic / ancient** rather
than exotic.

## Outputs

- [x] `phonology.md` — consonant table, vowel table, length/mora section, provisional
      romanization
- [ ] `grammar.md`
- [ ] `lexicon.csv`

## Open questions / revisit later

- Do glides /w j/ and /h/ truly never geminate? (Lesson 06)
- Stress-by-weight vs. pitch accent? (Lessons 10/11)
- Are there vowel-sequence (hiatus) or diphthong restrictions? (Lesson 06)

## License note

Nothing reproduced from external sources. PHOIBLE used for frequency guidance, CLTS for
symbol validation; the inventory is original/derived.
