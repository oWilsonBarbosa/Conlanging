# Lesson 02 — Phonology 1

- **CU lesson:** <https://sites.google.com/view/conlangs-university/lessons> (Phonology 1)
- **Date:** 2026-06-14
- **Goal:** fix Alantian's phoneme inventory by deciding each contrast on
  **place / manner / feature** grounds, and characterize the result against real
  languages. (Supersedes the earlier frequency-only draft.)

## Method

Rather than picking "common" segments, each dimension was chosen for the effect it has
on Alantian's character (ancient · elevated · moraic · resonant), then sanity-checked
against cross-linguistic typology (PHOIBLE) and validated symbol-by-symbol (CLTS).

## Decisions (by feature)

- **Laryngeal (stops):** three-way **aspirated / voiceless / voiced** —
  pʰ p b · tʰ t d · kʰ k g — plus **glottal stop ʔ**.
  Active features: [±spread glottis] (aspiration) and [±voice] both contrastive.
- **Continuant obstruents:** fricatives **f s x h** (labial, coronal, dorsal, glottal);
  all [−voice]. No affricates ([−delayed release] throughout).
- **Sonorants:** nasals **m n** ([ŋ] allophonic); liquids **l r**; glides **w j**.
  Sonorants may be **syllabic** (m̩ n̩ l̩ r̩) and serve as moraic nuclei.
- **Vowels:** minimal **/a i u/**; contrasts in **length** (aː iː uː) and **nasality**
  (ã ĩ ũ). Six **falling diphthongs**: ai au ia iu ua ui.
- **Weight:** moras from long vowels, diphthongs, geminates, codas, and syllabic
  sonorants (carried from the moraic design).

Inventory size: **20 consonants** (≈ PHOIBLE mean) + a small, heavily-inflected vowel
core → "medium, distinctive" rather than minimal.

## Characterization vs. real languages

| Feature chosen | Closest real-world model | Character it lends Alantian |
|---|---|---|
| pʰ/p/b · tʰ/t/d · kʰ/k/g three-way stops | **Classical Greek** (φ π β …) | the core "ancient/elevated" signature |
| Glottal stop ʔ, velar fricative x, glottal h | Greek χ, Semitic | a throaty, sacral edge |
| Syllabic sonorants (m̩ n̩ l̩ r̩) | **Sanskrit / Proto-Indo-European** (ṛ ḷ) | humming, chantable resonance |
| Nasal vowels ã ĩ ũ | Sanskrit anusvāra, French/Portuguese | added resonance ("resonant" pillar) |
| /a i u/ + length only | **Classical Arabic, Quechua, PIE** | austere, archaic vocalism |
| Mora-timing + length + pitch (likely) | **Ancient Greek, Vedic Sanskrit, Japanese** | the "moraic" rhythm; liturgical cadence |

Net identity: an **ancient liturgical language** — Greek bones, Indic resonance, Arabic
vowels. Distinct from a generic "Latin-lite" conlang.

## Sources consulted

| Source | What I looked at | How it informed the decision |
|---|---|---|
| PHOIBLE | Frequency/typology of three-way laryngeal systems, /a i u/ triangles, syllabic sonorants, nasal vowels | Confirmed each contrast is attested and natural; placed Alantian's size at ≈ the cross-linguistic mean (20 C) |
| CLTS (BIPA) | Validity of every symbol (pʰ tʰ kʰ … ʔ, x, m̩ n̩ l̩ r̩, ã ĩ ũ) | All well-formed BIPA; romanization maps cleanly |
| BDPROTO | Reconstructed proto-language inventories (for the "ancient" feel) | Cross-check that the profile resembles plausible *old/reconstructed* systems, not just modern ones |

> Provenance only — no inventory copied from any source; the feature *choices* were
> guided by typological comparison.

## Outputs

- [x] `phonology.md` — full consonant/vowel tables, mora system, romanization
- [ ] `grammar.md`
- [ ] `lexicon.csv`

## Open questions / revisit later

- Do long **and** nasal combine (ãː ĩː ũː)? (Lesson 06)
- Inventory of permitted geminates and codas; cluster rules. (Lesson 06)
- Pitch accent vs. weight-stress. (Lessons 10/11)
- Phonetic realization of the "falling" *ia/ua* diphthongs.

## License note

Nothing reproduced from external sources. PHOIBLE/BDPROTO used for typological
comparison, CLTS for validation; the inventory is original.
