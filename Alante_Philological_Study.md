# A Philological Study of the Alante Language Family
## Patterns, Trends, Reconstructions, and Standardization

**Document type:** Comparative philological analysis  
**Corpus:** 12 source files (10 .xlsx, 2 .docx)  
**Method:** Corpus analysis, WALS feature coding, Comparative Method, Wave Model, Feature Geometry  
**Date of analysis:** 2026-06

---

## Abstract

This study presents a systematic philological analysis of the Alante language family, a constructed language (conlang) family designed with reference to Proto-Indo-European morphological architecture and Andean (Quechua/Aymara) phonological typology. The corpus consists of twelve source documents covering five languages — **ProtoAlante**, **Classical Alantian**, **Angélico**, **Pavanam**, and **Pieii** — at varying stages of development. The analysis proceeds in four phases: (1) extraction and comparison of phonological inventories across all sources; (2) construction of a WALS (World Atlas of Language Structures) feature matrix for phonological features 1A–19A; (3) identification and resolution of six design contradictions found in the source material; and (4) philological synthesis using the Comparative Method, Wave Model, Feature Geometry, and Swadesh vocabulary coverage. A central finding is the distinction between **declared inventories** (as stated in phonological descriptions) and **lexicon-derived inventories** (as evidenced by actual word forms). This distinction significantly revises the typological profile of Pavanam and Pieii, reveals internal inconsistencies in the Angélico source documents, and confirms that voicing contrast is a shared retention of the entire family rather than a design innovation. Two competing theories of ProtoAlante's historical origin are evaluated in depth. The study concludes with a set of standardized recommendations for each language and an updated WALS matrix.

---

## 1. Introduction

The Alante language family is a constructed language project designed around two primary typological reference points: the morphological architecture of Proto-Indo-European (PIE) and the phonological profile of Andean high-altitude languages, particularly Quechua and Aymara. This dual influence produces a distinctive family character: PIE-style root morphology (consonantal root categories, ablaut vowel alternation, agglutinative suffixation) paired with an Andean-type phonological target (large consonant inventories, three-way stop contrasts, uvular consonants, small vowel systems).

The family tree as reconstructed from the source documents comprises:

```
PreProtoAlante (hypothetical tonal ancestor)
    │
ProtoAlante
    ├── Angélico (early branch, conservative)
    │       └── [Angélico__Léxico represents developed stage]
    └── Classical Alantian (prestige/literary register)
            └── Pieii (archaic branch)
                    └── Pavanam (innovative/reduced branch)
```

The five languages represent very different stages of development. Classical Alantian has the most elaborated phonological description (40 consonants, full ejective and aspirate series, uvulars) but no vocabulary. Angélico has approximately 160 attested word forms. Pavanam and Pieii share an identical 279-word lexicon. ProtoAlante exists only as root shape templates and PIE etymological source material.

---

## 2. Source Corpus

| File | Language | Key contents |
|---|---|---|
| `Língua_Alante.docx` | Classical Alantian | Full phonetic inventory (40 consonants, 3 vowels), no vocabulary |
| `Alante__Vocab.docx` | Transitional / ProtoAlante | PIE reconstructions, early vocabulary (bʱ/dʱ/gʱ forms), verb paradigms, pronouns |
| `Alante.xlsx` | Early Alante | Phonotactic root catalogues (Roots¹: 779 entries, no meanings; Roots²: 7 roots) |
| `Línguas_Alantes_2.0.xlsx` | Classical Alantian | Phonology, sound change periods, morphology, lexicon (concept labels only) |
| `ProtoAlante_OLD.xlsx` | ProtoAlante | Root shape templates, PIE-derived etymologies (Página3), ablaut paradigms |
| `Angélico.xlsx` | Angélico | Phonological framework (VGLNFP), Dictionary (~100 words, romanized) |
| `Angélico__Léxico.xlsx` | Angélico | Swadesh-type list (Página1, ~200 concepts), confirmed IPA forms (Página3, ~60 words) |
| `Pavanam.xlsx` | Pavanam | 279 words (column 5), WALS profile, consonant inventory |
| `Pieii.xlsx` | Pieii | 279 words (identical to Pavanam), WALS profile, consonant inventory (34C declared) |
| `HighAltitude_Languages_and_Phonologies.xlsx` | Reference | Quechua, Aymara, Ethiopian phonological data |
| `Phonology.xlsx` | Reference | WALS feature values for Aymara, Tibetan, Quechua, Pashto, Georgian, Nepali |
| `Fonologia_Alante_Compilado.xlsx` | Classical Alantian | Sound change rules ([d]>[l]/e_#, [d]>[ɾ]/[o,a]_#) |

---

## 3. Phonological Inventories

### 3.1 Declared inventories

**ProtoAlante** (two conflicting versions in the same file):

*Info sheet (21 consonants):*  
p/t/k/b/d/g/ɸ/θ\|s/x/h/ps/ts/ks/ʔs/j/w/l\|r/m/n/ŋ

*Sounds sheet (25 consonants):*  
Adds ʋ/ɾ/ɰ/v/z/ɦ/bʱ/dʱ/gʱ to a subset of the above

The 21-consonant system is PIE-inspired (plain/voiced stop pairs, fricatives, affricates). The 25-consonant system adds breathy voiced stops (bʱ/dʱ/gʱ) and additional approximants.

**Classical Alantian** (40 consonants, 3 vowels):  
m/n/ɲ / p/b/t/d/k/ɡ/kʷ/ɡʷ/q/ʔ / pʼ/tʼ/kʼ/kʷʼ/qʼ / pʰ/tʰ/kʰ/qʰ / ts/dz/t̠ʃ/d̠ʒ/tsʼ/t̠ʃʼ / s/z/ʃ/ʒ/ɸ/χ/h / j/w/ɾ/l/ʎ  
Vowels: a/i/u

**Angélico** (VGLNFP framework, 17 consonants, 3 vowels):  
b/d/g/p/t/k / m/n/ŋ / f/s/h / ɰ/ɹ/ʋ/l/ɾ  
Vowels: ä/e/o  
*(Note: This framework, found in Angélico.xlsx, is inconsistent with the Léxico IPA forms — see §3.2)*

**Pavanam** (16 consonants declared, 5 vowels):  
p/t/k/b/d/g/f/s/h/m/n/ɲ\|ŋ/l/r/w/j  
Vowels: a/e/i/o/u

**Pieii** (34 consonants declared, 5 vowels):  
Pavanam inventory + bʰ/dʰ/gʰ/kʷ/gʷ/ŋ/ŋʷ + additional stops  
Vowels: a/e/i/o/u

### 3.2 Lexicon-derived inventories

Analysis of actual word forms in each language's vocabulary reveals systematic discrepancies from declared inventories.

**Angélico (Léxico-derived, 17 consonants, 3 vowels):**

| Class | Phonemes | Notes |
|---|---|---|
| Voiceless stops | p / t / k | p is rare (3 tokens) |
| Voiced stops | b / d / g | |
| Breathy voiced stops | bʱ / dʱ / gʱ | High frequency |
| Fricatives | ɸ / s / x | ɸ not f |
| Approximants | ɰ / ɹ / ʋ | ɰ romanized as "h", ɹ as "r" |
| Nasals | m / n | No ŋ, no l |
| Vowels | a / e / o | 3-vowel system |

The VGLNFP framework in Angélico.xlsx is an earlier version: it has f (not ɸ), ɾ (not ɹ), h (not ɰ), l and ŋ (both absent from Léxico), and lacks bʱ/dʱ/gʱ entirely. The Léxico represents the current design state and should be treated as authoritative.

**Pavanam (lexicon-derived, 14 consonants, 5 vowels):**

| Class | Phonemes | Notes |
|---|---|---|
| Voiceless stops | p / t / k | |
| Voiced stops | b / d / g | ɡ (U+0261) ≡ g (U+0067) — Unicode variant only |
| Fricatives | f / s / h | |
| Nasals | m / n / ŋ | ŋ is word-initial in 10+ words |
| Liquids | l / r | |
| Vowels | a / e / i / o / u | 5 vowels; ā in one word only (*spār*) |
| Absent from lexicon | j, w, ɲ | Declared but unattested |

Additionally, the lexicon attests **th** in three words (*fathaŋ*, *athaŋ*, *thakon*), which may represent: (A) a /t.h/ consonant cluster, (B) an undeclared phoneme /θ/, or (C) an aspirated /tʰ/.

**Pieii (lexicon-derived):** Identical to Pavanam — all 279 words are shared. The 20 consonants that distinguish the declared Pieii inventory (bʰ/dʰ/gʰ, kʷ/gʷ, ŋʷ, etc.) have zero attestation in the lexicon.

### 3.3 Declared vs. lexicon-derived: summary table

| Language | Declared C | Lexicon C | Declared V | Lexicon V | Major discrepancies |
|---|---|---|---|---|---|
| ProtoAlante | 21 or 25 | — | 3 | — | Two conflicting versions |
| Classical Alantian | 40 | — | 3 | — | No vocabulary to check |
| Angélico | 17 (VGLNFP) | 17 (Léxico) | 3 | 3 | f→ɸ; ɾ→ɹ; h→ɰ; l/ŋ absent; bʱ/dʱ/gʱ absent from VGLNFP |
| Pavanam | 16 | **14** | 5 | 5 | j/w/ɲ unattested; 12A wrong; ŋ word-initial |
| Pieii | 34 | **14** | 5 | 5 | 20 consonants with zero lexical attestation |

---

## 4. WALS Feature Matrix (1A–19A)

### 4.1 Reference language values

The following real-language values are drawn from the Phonology.xlsx database (Planilha3) and standard WALS data:

| Feature | Quechua | Aymara | Tibetan | Pashto | Georgian | Nepali |
|---|---|---|---|---|---|---|
| 1A Consonant inv. | Average | Average | Large | Average | Large | Average |
| 2A Vowel quality | Small (3) | Small (3) | Small (5) | Average (5-6) | Average | Average |
| 3A C/V ratio | High | High | High | Mod. high | High | Mod. high |
| 4A Voicing | Plosives only | Plosives only | None | Both | Both | Both |
| 5A Plosive gaps | No gaps | No gaps | No gaps | No gaps | No gaps | No gaps |
| 6A Uvulars | Uvular stops | Uvular stops | None | Uvular fricative | None | None |
| 7A Glottalized | Ejectives | Ejectives | None | None | None | Breathy voice |
| 8A Laterals | L no obstruent | L no obstruent | L no obstruent | L no obstruent | L no obstruent | L no obstruent |
| 9A Velar nasal | No initial | No initial | Velar nasal | No velar nasal | No velar nasal | Velar nasal |
| 12A Syllable | Simple | Simple | Complex | Complex | Complex | Mod. complex |
| 13A Tone | No tones | No tones | Complex | No tones | No tones | No tones |
| 14A Fixed stress | (varies) | (varies) | (varies) | (varies) | (varies) | (varies) |
| 17A Rhythm | Trochaic | Trochaic | — | — | — | — |

### 4.2 Alante family WALS matrix

*(Values marked with † are revised from declared inventories based on lexical evidence; values marked with * are design decisions made in this study — see §5)*

| Feature | ProtoAlante | Classical Alantian | Angélico | Pavanam | Pieii |
|---|---|---|---|---|---|
| **1A** Consonant inv. | Average (21-25) | Very large (40) | Average (17) | Small (14)† | Small (14)† |
| **2A** Vowel quality | Small (3: a/e/o) | Small (3: a/i/u) | Small (3: a/e/o) | Large (5) | Large (5) |
| **3A** C/V ratio | High (7.0) | Very high (13.3) | High (5.7) | Low (2.8)† | Low (2.8)† |
| **4A** Voicing | In plosives alone* | In plosives alone* | In plosives alone* | In plosives alone† | In plosives alone† |
| **5A** Plosive gaps | No gaps | No gaps | No gaps | No gaps | No gaps |
| **6A** Uvulars | None | Uvular stops+frict. | None | None | None |
| **7A** Glottalized | None | Ejectives+aspiration | Breathy voice | None | None |
| **8A** Laterals | L no obstruent | L no obstruent | No laterals† | L no obstruent | L no obstruent |
| **9A** Velar nasal | Velar nasal | No initial velar ŋ* | No velar nasal† | Velar nasal† | Velar nasal† |
| **10A** Vowel nasal. | No nasalized | No nasalized | No nasalized | No nasalized | No nasalized |
| **11A** Front rounded | None | None | None | None | None |
| **12A** Syllable | Mod. complex | Unknown | Mod. complex | Complex† | Complex† |
| **13A** Tone | No tones | No tones | No tones | No tones | No tones |
| **14A** Fixed stress | No fixed stress* | Penultimate* | No fixed stress* | Penultimate* | Penultimate* |
| **15A** Weight stress | Unbounded* | Fixed stress* | Quantity-sensitive* | Fixed stress* | Fixed stress* |
| **16A** Weight factors | — | No weight* | Long vowels* | No weight* | No weight* |
| **17A** Rhythm | Iambic | Trochaic* | Iambic | Trochaic* | Trochaic* |
| **18A** Absent cons. | No p | None | No p (rare) | None | None |
| **19A** Uncommon cons. | — | Ejectives + uvulars | Breathy stops | Eng (ŋ) initial | Eng (ŋ) initial |

---

## 5. Design Questions and Resolutions

Six design contradictions were identified in the source corpus. The following records each question, the available evidence paths, and the recommended resolution.

### Q1 — Stress systems across the family

**Evidence:** The source documents show conflicting or underspecified stress systems. ProtoAlante's ablaut system implies variable root-level stress. Angélico's root morphology suggests quantity sensitivity. Classical Alantian and Pavanam/Pieii have WALS profiles with simultaneous contradictory stress values.

**Resolution (accepted):**

| Language | 14A | 15A | 16A | 17A | Rationale |
|---|---|---|---|---|---|
| ProtoAlante | No fixed stress | Unbounded | — | Iambic | PIE-style lexical accent |
| Angélico | No fixed stress | Quantity-sensitive | Long vowels | Iambic | Root morphology implies weight sensitivity |
| Classical Alantian | Penultimate | Fixed stress | No weight | Trochaic | Literary register standardization |
| Pavanam | Penultimate | Fixed stress | No weight | Trochaic | Consistent with Andean target |
| Pieii | Penultimate | Fixed stress | No weight | Trochaic | Sister of Pavanam |

### Q2 — Pavanam/Pieii 14A/15A contradiction

**Evidence:** Both languages had simultaneous WALS values of 14A="No fixed stress" AND 15A="Fixed stress," which are mutually exclusive. The Página7 WALS profiles in both files were copy-pasted without differentiation.

**Resolution (accepted):** Set 14A = "Penultimate" for both languages (consistent with 15A = "Fixed stress" and 17A = "Trochaic"). This resolves the contradiction and aligns with the Andean typological target.

### Q3 — Classical Alantian /ŋ/: phonemic or allophonic?

**Evidence conflict:** `Língua_Alante.docx` lists nasals as m/n/ɲ only (no /ŋ/). `Línguas_Alantes_2.0.xlsx` Phonology sheet lists m/n/ɲ/ŋ.

**Path A:** /ŋ/ is phonemic — keep it; WALS 9A = "Velar nasal." Gives symmetrical nasal series (bilabial/alveolar/palatal/velar). Requires minimal pairs.  
**Path B:** /ŋ/ is allophonic — remove it; WALS 9A = "No initial velar nasal." The docx is the authoritative narrative document. Aligns with Quechua/Aymara.

**Resolution (accepted):** Path B. The docx is the final decision document; the xlsx is an exploratory draft. Add allophony rule: n → [ŋ] / _{k, kʷ, q}. Classical Alantian 9A = "No initial velar nasal."

### Q4 — Classical Alantian voiced fricatives: phonemic or allophonic?

**Evidence conflict:** The inventory includes z/ʒ/β/ʁ alongside voiced stops b/d/g/gʷ. If voiced fricatives are phonemic, 4A = "Both plosives and fricatives" (45 consonant system). If allophonic, 4A = "In plosives alone" (40 consonant system matching the docx count).

**Path A:** Voiced fricatives are phonemic. Gives richest system but pushes inventory to 45 consonants — far beyond Andean typological targets.  
**Path B:** Voiced fricatives are conditioned allophones. Rules: ɸ→β, χ→ʁ, s→z, ʃ→ʒ in V_V environments. Docx count of 40 consonants represents phonemes; xlsx count of 45 represents phones including allophones.

**Resolution (accepted):** Path B. Allophonic voiced fricatives. 4A = "In plosives alone." This reconciles the docx/xlsx consonant count discrepancy and aligns Classical Alantian closer to Andean norms.

### Q5 — Pavanam/Pieii: 16 vs. 34 consonants

**Evidence:** Pavanam's Sounds sheet has 16 consonants; WALS target says "Average (19-25)." Pieii has 34 consonants; same WALS target. Both share identical vocabulary. Neither's vocabulary supports their respective WALS coding.

**Path A:** Fix WALS targets to match actual inventories (Pavanam = Moderately small; Pieii = Large).  
**Path B:** Expand Pavanam / reduce Pieii to reach "Average."  
**Path C:** Redesign the relationship as diachronic — Pieii is the archaic ancestor, Pavanam the reduced descendant.

**Resolution (accepted):** Path C. Pieii represents an older, more conservative stage; Pavanam represents a phonologically reduced descendant. The identical vocabulary reflects shared inheritance before differentiation. Sound change rules Pieii→Pavanam: (1) bʰ/dʰ/gʰ → b/d/g (loss of breathy/aspirate); (2) kʷ/gʷ → k/g (loss of labialization); (3) ŋʷ → ŋ (loss of labialization on nasal). WALS 1A Pieii = "Large" (26-33); Pavanam = "Small" (6-14) or "Moderately small" (15-18). Pieii requires new vocabulary using bʰ/dʰ/gʰ/kʷ/gʷ/ŋʷ to differentiate the two languages.

### Q6 — ProtoAlante canonical version: 21C or 25C?

**Evidence:** Two sheets in `ProtoAlante_OLD.xlsx` represent different analyses of the same proto-language. Neither matches the requirements of all daughter languages simultaneously.

**Path A:** 21-consonant Info sheet is canonical. Breathy stops in daughters are independent innovations.  
**Path B:** 25-consonant Sounds sheet is canonical. Breathy stops are inherited.  
**Path C:** Reconstruct from daughters using Comparative Method.

**Resolution (accepted):** Path C. Key reconstruction anchors:
- Voicing contrast (p/t/k vs. b/d/g): required by all daughter lexicons → proto-language had voiced stops
- Breathy stops bʱ/dʱ/gʱ: retained in Angélico (bʱ/dʱ/gʱ), shifted in Classical Alantian (→ pʰ/tʰ/kʰ), lost in Pavanam (→ b/d/g) → proto-language had breathy stops; parallel evolution hypothesis is ruled out
- Uvular *q: required by Classical Alantian but absent from all daughter lexicons → likely a Classical Alantian innovation (contact influence), not a proto-language feature
- Affricates ps/ks from Info sheet: no daughter language preserves them intact; likely notation for *ts + *ʔ as separate phonemes
- Reconstructed ProtoAlante: ~27–30 consonants, including plain/voiced/breathy three-way stop contrast, velar fricative *x, bilabial fricative *ɸ, sonorants m/n/ŋ/l/r/w/j

---

## 6. Proto-Language Theories

Two theories of ProtoAlante's historical origin are compatible with the lexical and phonological evidence. They are not mutually exclusive.

### Theory 2: The Breathy-Voice Proto-Language

ProtoAlante had a three-way stop contrast at its core: plain (p/t/k), voiced (b/d/g), and breathy-voiced (bʱ/dʱ/gʱ). The breathy series descended from earlier laryngeal segments — functionally analogous to PIE laryngeals (h₁/h₂/h₃) but realized as breathy stops rather than abstract segments. The e/o/Ø ablaut alternation was originally conditioned by these laryngeals before they were reinterpreted as a productive morphological system.

**Evidence from the corpus:**
- `Alante__Vocab.docx` uses bʱ/dʱ/gʱ throughout its early vocabulary (bʱebʱon "one", gʱobʱon "black", bʱefon "red")
- The same document shows ablaut in early paradigms (bʱēbʱo / bʱebʱon / bʱedʱon)
- Angélico's Léxico retains bʱ/dʱ/gʱ as productive phonemes
- Pavanam vocabulary shows b/d/g where Angélico has bʱ/dʱ/gʱ — exactly the pattern expected if Pavanam merged breathy into plain voiced

**Sample correspondences under Theory 2:**

*ProtoAlante *bʱan "to carry, bear a burden":*

| Language | Form | Change |
|---|---|---|
| ProtoAlante | *bʱan | — |
| Classical Alantian | pʰan | bʱ → pʰ (breathy voiced → voiceless aspirated) |
| Angélico | bʱan | retained |
| Pieii | bʰan | retained (notation variant) |
| Pavanam | ban | bʱ → b (breathy lost) |

*Ablaut paradigm for root *gʱ- "to move, travel":*

| Grade | ProtoAlante | Classical Al. | Angélico | Pavanam |
|---|---|---|---|---|
| e-grade (active) | *gʱel | kʰil | gʱel | gel |
| o-grade (stative) | *gʱol | kʰul | gʱol | gol |
| ∅-grade (nominal) | *gʱl- → *gʱal | kʰal | gʱal | gal |

### Theory 4: The Tonal Ancestor

The ProtoAlante ablaut system (e/o/∅ grades) is not an inherited morphological mechanism but a residue of an earlier tonal system. The ancestor of ProtoAlante — **PreProtoAlante** — had lexical tone: high tone (˥) conditioned both fortis/aspirated consonants and a front vowel reflex (e); low tone (˩) conditioned lenis/voiced consonants and a back vowel reflex (o); mid/neutral tone (˧) conditioned zero grade (vowel loss).

**Tonal collapse rules:**

| Pre-PA tone | → PA consonant class | → PA default vowel |
|---|---|---|
| ˥ high | H (aspirated stop) | e-grade |
| ˩ low | C (voiced/breathy stop) | o-grade |
| ˧ mid/neutral | P (plain stop) | ∅-grade (→ a by epenthesis) |

**The root categorization system as tonal fossil:**

The H/P/F/N/G/V/C root categories found throughout the source documents are not arbitrary phonological labels — under Theory 4, they encode the original **tonal class** of the root:

| Category | Consonants | Pre-PA tonal origin | Semantic tendency |
|---|---|---|---|
| H (aspirated/heavy) | pʰ/tʰ/kʰ/qʰ | High-tone class ˥ | light, sharp, clear, perceived |
| P (plain stop) | p/t/k/q | Mid-tone class ˧ | basic, concrete, unmarked |
| C (voiced stop) | b/d/g | Low-tone class ˩ | heavy, dark, large, hidden |
| F (fricative) | ɸ/s/x/χ | High-tone spirantization | movement, transition, change |
| N (nasal) | m/n/ɲ/ŋ | Tonally neutral | animate, human, relational |
| G (glide) | j/w | Tonally transparent | spatial, directional |
| V (vowel-initial) | — | Tone on nucleus alone | qualities, states |

**Evidence for Theory 4:**

The morphology sheet in `Línguas_Alantes_2.0.xlsx` assigns semantic values to vowels: /i/ = small/light things, /u/ = larger/heavier things. Under Theory 4, this is the direct reflex of the tonal system: high-tone vowel → /e/ → Classical Alantian /i/ (small, light); low-tone vowel → /o/ → Classical Alantian /u/ (large, heavy). The semantic polarity of i/u in Classical Alantian is the fossilized tonal opposition of the ancestor.

**Sample: tonal minimal pair evolving to lexical contrast:**

*Pre-PA *kal "eye/vision/perception" — two tonal realizations:*

| Stage | High-tone form | Low-tone form |
|---|---|---|
| Pre-PA | *kal˥ "clear, visible, sharp" | *kal˩ "dark, dim, obscured" |
| ProtoAlante | *kʰel (H-root, e-grade) | *gʱol (C-root, o-grade) |
| Classical Al. | kʰil "to perceive" | gul "darkness, night" |
| Angélico | kʰel "to see" | gʱol "shadow" |
| Pavanam | kel "to see" | gol "dark" |

### Combined reading

Theories 2 and 4 are mutually reinforcing. The Pre-ProtoAlante tonal system generated breathy voiced stops as the phonetic realization of low-tone consonant onset: low tone + voiced stop onset → breathy phonation as prosodic residue. When tone was lost as a phonemic feature (possibly due to increasing consonant cluster complexity making tone acoustically unstable), the breathy phonation was reanalyzed as a segmental feature (bʱ/dʱ/gʱ), and the vowel coloring was reanalyzed as ablaut morphology. ProtoAlante is thus the immediate post-tonal stage of this language.

---

## 7. Sound Correspondences (Comparative Method)

The following correspondence table is derived from attested lexical forms wherever possible, and from declared inventories supplemented by the Q3/Q4 design decisions otherwise.

| ProtoAlante | Classical Alantian | Angélico | Pavanam/Pieii | Notes |
|---|---|---|---|---|
| *p | p | p | p | Stable across family |
| *t | t | t | t | Stable |
| *k | k | k | k | Stable |
| *b | b | b | b | Stable |
| *d | d | d | d | Stable |
| *g | g | g | g | Stable |
| *bʱ | pʰ | bʱ | b | Breathy: aspirated / retained / lost |
| *dʱ | tʰ | dʱ | d | Breathy: aspirated / retained / lost |
| *gʱ | kʰ | gʱ | g | Breathy: aspirated / retained / lost |
| *ɸ | ɸ | ɸ | f | Pavanam shift: bilabial → labiodental |
| *s | s | s | s | Most stable segment in family |
| *x | χ (backed) | x (retained) | h (fronted) | Three-way dorsal split |
| *m | m | m | m | Stable |
| *n | n | n | n | Stable |
| *ŋ | [ŋ] allophone | — | ŋ phoneme (initial) | Three-way nasal split |
| *l | l | — (lost → ɹ) | l | Angélico innovation: lateral loss |
| *r | ɾ | ɹ | r | Rhotic variant |
| *j | j | — | — (unattested) | Unstable |
| *w | w | ʋ | — (unattested) | Angélico: w → labiodental approx. |
| *q | q/qʼ/qʰ | — | — | Classical Alantian innovation (contact) |
| *ʔ | ʔ | — | — | Retained in Classical Alantian only |

**The s-invariance principle:** /s/ is the only segment to appear unchanged in every language with a lexicon. It is therefore the most reliable reconstructed ProtoAlante phoneme and the most useful anchor for comparative analysis.

**The dorsal fricative split:** The most typologically interesting correspondence. ProtoAlante *x went in opposite directions: Classical Alantian backed it to uvular χ (Andean contact influence), Pavanam fronted it to laryngeal h (reduction/simplification), Angélico retained the velar x. This three-way split confirms the branching structure: Angélico branches first (retaining the proto-form), then Classical Alantian and Pavanam diverge in opposite directions.

---

## 8. Wave Model Analysis

The Wave Model identifies features that spread across the family regardless of genealogical position, representing contact-induced diffusion rather than inheritance. The following isoglosses are identified:

### Shared retentions (proto-language features preserved everywhere)

- Six-stop system: p/t/k vs. b/d/g
- Alveolar sibilant: /s/
- Bilabial and alveolar nasals: m/n
- CVC root template (with ablaut)
- H/P/F/N/G/V/C root categorization

### Isogloss 1 — Angélico branch

Features present in Angélico and absent (or differently realized) elsewhere:
- Breathy stops bʱ/dʱ/gʱ as **distinct phonemes** (not merged or shifted)
- Loss of lateral /l/ (completely absent from Léxico)
- Use of ɹ (approximant rhotic) vs. family-wide r/ɾ
- Use of ɰ for laryngeal (rather than h)
- Use of ɸ retained (not shifted to f or χ)

### Isogloss 2 — Pavanam/Pieii branch

Features present in Pavanam/Pieii and absent elsewhere:
- Phonemic word-initial ŋ (9A = "Velar nasal")
- Complex phonotactics: onset clusters (kr/br/tr/gr/sp), geminates (-tt-/-kk-/-mm-/-ss-/-ll-)
- Five-vowel system a/e/i/o/u (vs. three-vowel elsewhere)
- Shift ɸ → f (labiodental)
- Shift x → h (fronting of dorsal fricative)
- Loss of breathy voiced stops (merged into b/d/g)

### Isogloss 3 — Classical Alantian

Features unique to Classical Alantian:
- Uvular stop series q/qʼ/qʰ (contact innovation)
- Full ejective series pʼ/tʼ/kʼ/kʷʼ/qʼ (Andean contact)
- Backing of dorsal fricative: x → χ
- Affricate elaboration: ts/dz/t̠ʃ/d̠ʒ/tsʼ/t̠ʃʼ
- Palatal lateral ʎ
- Labialized velars kʷ/ɡʷ

```
ProtoAlante
    │
    ├── [Isogloss 1] ── Angélico
    │                    (bʱ/dʱ/gʱ; -l; ɹ; ɰ; ɸ)
    │
    └── Common node
            ├── [Isogloss 3] ── Classical Alantian
            │                    (uvulars; ejectives; χ; affricates; ʎ; kʷ/gʷ)
            │
            └── [Isogloss 2] ── Pieii → Pavanam
                                 (ŋ initial; clusters; 5V; f; h; -bʱ/dʱ/gʱ)
```

---

## 9. Feature Geometry

Feature Geometry organizes phonological features in a hierarchical tree structure. The Alante family evidence supports the following articulation:

### [±laryngeal] node

The most family-diagnostic node. Three distinct specifications:

- **Classical Alantian:** [+constricted glottis] (ejectives) + [+spread glottis] (aspirates). Both present, from two different sources (ejectives = contact innovation; aspirates = inherited *bʱ→pʰ shift).
- **Angélico:** [+spread glottis] (breathy stops bʱ/dʱ/gʱ). Inherited from ProtoAlante. No ejectives.
- **Pavanam/Pieii:** Neither [±constricted] nor [±spread glottis] for stops. Laryngeal node absent from the stop series. The breathy distinction was lost (merged into plain voiced).

### [dorsal] place node

Three-way split in the fricative column:
- Classical Alantian: [uvular] (χ) — backed under Andean contact
- Angélico: [velar] (x) — retained proto-form
- Pavanam: [laryngeal/glottal] (h) — fronted/reduced

### [nasal] + [dorsal] intersection

The velar nasal ŋ is the most variable feature across the family:
- ProtoAlante: phonemic (Info sheet)
- Angélico: lost (0 attestations)
- Classical Alantian: allophonic [n→ŋ/__{k,kʷ,q}]
- Pavanam: phonemic AND word-initial (WALS 9A = "Velar nasal")

This means ŋ underwent three different fates across three branches, making it the family's most typologically active segment.

---

## 10. Vocabulary Analysis

### 10.1 Lexicon status by language

| Language | Word count | Coverage type | Development stage |
|---|---|---|---|
| ProtoAlante | 0 (assigned) | Root templates only | Pre-lexical |
| Alante (early) | 0 (meanings) | Phonotactic catalogue | Pre-lexical |
| Vocab.docx | ~20 | Numbers, colors, fire paradigm, pronouns | Seed lexicon |
| Classical Alantian | 0 (word forms) | Concept labels only | Pre-lexical |
| Angélico (Dictionary) | ~100 | Basic + cultural vocabulary | Partial |
| Angélico (Léxico) | ~60 (IPA-confirmed) | Swadesh-oriented | Partial |
| Pavanam | 279 | Multi-domain cultural vocabulary | Substantial |
| Pieii | 279 (identical to Pavanam) | Same as Pavanam | Undifferentiated |

### 10.2 The transitional Vocab.docx vocabulary

The earliest attested word forms in the family. Phonological system: bʱ/dʱ/gʱ dominant; long vowels ē/ō present; syllabic m̩ attested (*gʱogʱōbʱm̩* "total darkness").

| Form | Gloss | Category |
|---|---|---|
| bʱebʱon | one, a unit | Number |
| bʱedʱon | two | Number |
| bʱefon | red | Color |
| gʱenon | yellow | Color |
| gʱobʱon | black | Color |
| kofon | green | Color |
| badar | fire, flame | Element |
| badron | conflagration | Element |
| vom / óm | I | Pronoun |
| ren / én | you | Pronoun |
| ha / á | he/she | Pronoun |

The long vowels and syllabic consonant in this earliest layer support Theory 4: these are pre-ablaut-collapse forms still showing tonal vowel conditioning (ē = high-tone retained length, ō = low-tone retained length).

### 10.3 Angélico core vocabulary (confirmed IPA)

Selected entries from Léxico Página3:

| IPA | Gloss | Notes |
|---|---|---|
| eʋes | water | Core Swadesh |
| neʋem | waters, sea, rain | Derived |
| eʋoɹ | year | Cultural |
| gasaʋ | animal | Core |
| ʋeɹka | yellow | Color |
| exes | strong, sharp, hard | Polysemous |
| okeɰ | what, who, that | Interrogative/relative |
| nan | some, any | Quantifier |
| dʱemem | animal (adj.), brutal | C-root (low-tone) |
| bʱeʋata | shower (bathing vessel) | H-root (high-tone) |

### 10.4 Pavanam semantic domains

The 279-word Pavanam lexicon covers:

| Domain | Count | Sample entries |
|---|---|---|
| Adjectives | 32 | talka (high), kroŋe (big), kalue (cold), soireŋ (beautiful) |
| Animals | 20+ | arkai (eagle), danaŋ (fish), ɡaudro (dog), ossoŋ (snake) |
| Body parts | 15+ | arɡol (finger), miaŋɡo (nose), nauɡa (face), ahram (eye) |
| Architecture | 12 | malka (house), halɡa (city/fortress), tanna (roof), raufa (tower) |
| Numbers | 12 | aste (1), auɡe (2), anka (4), mensa (6), ŋuasta (7), ŋelɡen (9) |
| Weather | 7 | uessua (rain), autam (wind), moho (cloud), peura (mist) |
| Food | 8 | kerla (food), peiko (honey), eŋŋan (maize), nohor (bread) |
| War/weapons | 10+ | farpa (battle), oksa (spear), aɡlioŋ (to kill), ottau (war) |
| Colors | 8+ | apra (green), ardel (black), sahho (red), omisko (blue) |
| Geography | 8+ | kestam (mountain), serse (forest), aruɡom (west), ŋelke (east) |
| Kinship | 6+ | ɡeol (father), spār (husband), ellan (family), hepte (sister) |
| Time | 8+ | ehhe (day), ranta (night), asta (dusk), arken (sun) |
| Titles | 6+ | malɡon (prince), ɡratal (builder), nelke (lord) |

**Notable:** The Pavanam lexicon goes significantly beyond a Swadesh core. The presence of war vocabulary, architectural vocabulary, musical vocabulary (moilmo "harp", odraŋ "narrative", iofres "bell"), and professional titles (malɡon "prince", nelke "lord", thakon "narrator") suggests a culturally developed society with literary and political institutions. The number system reaches at least 12 (kolko), suggesting a counting system.

---

## 11. Phonotactic Analysis

### 11.1 Pavanam phonotactics (lexicon-derived)

The Pavanam lexicon contradicts the declared WALS 12A = "Simple syllable structure." Attested patterns:

**Onset clusters:**  
kr- (kroŋe), br- (bramma, ebron), tr- (tralon, atres), gr- (ɡratal, ɡratal), sp- (spār), pr- (apra, kapra, iepren), fr- (iofres), gl- (aɡlioŋ)

**Medial clusters (sample):**  
-nt- (iente, aminto), -lk- (talka, malka, olka, nelke), -rk- (orko, arkai, arken), -st- (oste, astol, iasta), -mp- (uempe, ampa, olimpa), -dr- (ɡaudro, edroi, bodrau, uedro), -nd- (iondor, nande), -rd- (uardo, ardel, diorde), -mb- (mambe), -ld- (pelda), -lɡ- (halɡa, malɡon, ŋelɡen), -rɡ- (erɡes, arɡol, herɡo, harɡen), -ks- (heksa, naksa), -sk- (omisko, masken), -rm- (ŋarma, perme, korme), -lf- (salfa, talfa), -ps- (apse), -pt- (hepte), -bd- (abdon), -lm- (ailmar, moilmo), -sp- (aspen)

**Geminates:**  
-tt- (patte, etto, rakkia, ottes, ottau, ŋottor, auttem, ettio, ŋetta, pettes), -kk- (ossoŋ, oikko, rakkia), -mm- (bramma, arumme), -nn- (tanna, onnas, ennai), -ll- (nallon, ellan, ŋalla), -ss- (uessua, ossoŋ, serse), -pp- (oppo, meppa, euppa), -ff- (affen, affa), -rr- (parron), -hh- (ehhas, sahho, ehhe, ahram)

**Revised WALS 12A:** "Complex" (allows CC onsets, geminate consonants, complex medial and coda clusters).

### 11.2 Geminates as weight

The prevalence of geminates (-tt-, -kk-, -mm- etc.) has implications for stress. If geminates count as heavy (consonant weight for stress), then Pavanam's stress system may not be purely penultimate but weight-sensitive in environments with geminates. This would revise 15A from "Fixed stress (penultimate)" toward "Quantity-sensitive" — or suggest that penultimate stress applies globally but geminates are phonetically longer without triggering weight sensitivity. A design decision is needed.

---

## 12. Standardization Recommendations

### 12.1 Immediate corrections required

| Language | Issue | Correction |
|---|---|---|
| Angélico.xlsx | VGLNFP table uses outdated inventory | Replace with Léxico-derived inventory: bʱ/dʱ/gʱ, ɸ (not f), ɰ (not h), ɹ (not ɾ); remove l/ŋ |
| Pavanam.xlsx | WALS 1A declared "Average (19-25)" | Correct to "Small (6-14)" or "Moderately small (15-18)" |
| Pavanam.xlsx | WALS 12A declared "Simple" | Correct to "Complex" |
| Pavanam.xlsx | j/w/ɲ in declared inventory | Remove (unattested in lexicon) or populate vocabulary using them |
| Pavanam.xlsx | Unicode inconsistency g vs. ɡ | Standardize to ɡ (U+0261) throughout |
| Pieii.xlsx | All vocabulary identical to Pavanam | Write distinct Pieii vocabulary using bʰ/dʰ/gʰ/kʷ/gʷ/ŋʷ to differentiate the archaic branch |
| Línguas_Alantes_2.0.xlsx | Lexicon sheet has concepts only | Write IPA word forms for all 30 concept entries |
| ProtoAlante_OLD.xlsx | Two conflicting consonant counts | Adopt reconstructed inventory (~27-30C per §5 Q6) and annotate Info/Sounds sheets as drafts |

### 12.2 ProtoAlante reconstruction target

Based on the Comparative Method analysis, the canonical ProtoAlante inventory should contain:

**Consonants (~28):**
- Stops: p/t/k (plain voiceless) + b/d/g (voiced) + bʱ/dʱ/gʱ (breathy voiced)
- Fricatives: ɸ/s/x (bilabial/alveolar/velar)
- Glottal: ʔ/h
- Affricates: *ts (from which daughters develop differently)
- Nasals: m/n/ŋ
- Liquids: l/r
- Glides: j/w

**Vowels (3 quality + length):** a/e/o + ā/ē/ō (long; attested in Vocab.docx)

**Root template:** (C₁)eC₂ / (C₁)oC₂ / (C₁)C₂ (ablaut grades), where C₁ ∈ {H, P, C, F, N, G, V}

### 12.3 Recommended allophony rules (to be formalized per language)

**Classical Alantian:**
- n → [ŋ] / __{k, kʷ, q} (velar nasal allophony — Q3 resolution)
- ɸ → [β] / V_V
- χ → [ʁ] / V_V
- s → [z] / V_V
- ʃ → [ʒ] / V_V
(Q4 resolution — voiced fricatives are surface allophones)

**ProtoAlante (Vocab.docx):**
- [m] → [n] / _{dʱ, t, d, s}
- [n] → [m] / _{bʱ, p, b, ɸ}
(Documented in the source file)

### 12.4 WALS coding checklist (final recommended values)

| Feature | ProtoAlante | Classical Alantian | Angélico | Pavanam | Pieii |
|---|---|---|---|---|---|
| 1A | Average | Very large | Average | Small | Large (target) |
| 2A | Small (3) | Small (3) | Small (3) | Average (5) | Average (5) |
| 3A | High | Very high | High | Low | Low (current) |
| 4A | Plosives alone | Plosives alone | Plosives alone | Plosives alone | Plosives alone |
| 6A | None | Uvular stops+frict. | None | None | None |
| 7A | Breathy | Ejectives+aspiration | Breathy | None | Breathy (target) |
| 8A | L no obstruent | L no obstruent | **No laterals** | L no obstruent | L no obstruent |
| 9A | Velar nasal | No initial velar ŋ | **No velar nasal** | **Velar nasal** | Velar nasal |
| 12A | Mod. complex | Unknown | Mod. complex | **Complex** | **Complex** |
| 14A | No fixed | Penultimate | No fixed | Penultimate | Penultimate |
| 15A | Unbounded | Fixed | Qty-sensitive | Fixed | Fixed |
| 17A | Iambic | Trochaic | Iambic | Trochaic | Trochaic |
| 19A | — | Ejectives+uvulars | Breathy stops | ŋ initial | ŋ initial |

*Bold = revised from declared value based on lexical evidence*

---

## 13. Open Issues

The following questions remain unresolved and require design decisions:

1. **Classical Alantian vocabulary:** The Lexicon sheet in `Línguas_Alantes_2.0.xlsx` has 30 semantic concept targets (GROW, FLOW, SHINE, etc.) across three domains (earth/water/sun) but no IPA word forms. This is the family's most urgent lexical gap — the most phonologically developed language has zero vocabulary.

2. **Pavanam/Pieii th-words:** The status of /th/ in *fathaŋ*, *athaŋ*, *thakon* requires a formal decision: Is it a consonant cluster /t+h/, a phoneme /θ/, or an aspirate /tʰ/? Each choice has downstream consequences for 1A, 18A, and the ProtoAlante correspondence table.

3. **Pavanam geminates and stress:** Whether Pavanam's geminates constitute a weight distinction affecting stress (revising 15A) or are purely phonotactic is undecided. The current recommendation (14A = Penultimate, 15A = Fixed) is safe but may be too simple for a language with this geminate density.

4. **Angélico /p/ status:** The voiceless bilabial stop appears only 3 times in the entire Léxico — vanishingly rare for a presumably basic phoneme. Is /p/ a genuine phoneme in Angélico or is it marginal/borrowed? If marginal, WALS 18A should flag "Absence of common consonants: p."

5. **PreProtoAlante design:** Theory 4 implies a tonal ancestor language whose design is currently absent from the project. Whether to develop PreProtoAlante as a sixth language or leave it as a theoretical construct is a creative decision.

6. **Pieii vocabulary differentiation:** Under the Q5 resolution, Pieii requires a set of vocabulary forms using bʰ/dʰ/gʰ/kʷ/gʷ/ŋʷ that are not present in Pavanam. These must be derived via Pieii→Pavanam sound change rules (currently only partially specified).

---

## Appendix A: Attested ProtoAlante/Transitional Vocabulary (Vocab.docx)

| Form | Long form | Gloss | Category |
|---|---|---|---|
| bʱebbʱo | — | having the character of a unit | Adjective |
| bʱebʱēdʱo | — | eminent beyond comparison | Adjective |
| bʱēbʱo | — | single, not two or more | Adjective |
| bʱebʱon | — | a unit, single person/thing | Noun |
| bʱēbʱon | — | one; unity | Noun/Number |
| bʱēdʱo | — | being one more than one | Adjective |
| bʱedʱon | — | two | Number |
| bʱefon | — | red (color/pigment) | Noun |
| bʱegʱon | — | number; quantity | Noun |
| bʱembʱo | — | of the same kind/quality | Adjective |
| bʱerbʱo | — | combined into one entity | Adjective |
| gʱenon | — | yellow (color/pigment) | Noun |
| gʱōbʱo | — | black (adjective) | Adjective |
| gʱobʱon | — | black; blackness | Noun |
| gʱogʱōbʱm̩ | — | total darkness | Noun |
| gʱogʱōbʱo | — | extremely dark | Adjective |
| kofon | — | green (color/pigment) | Noun |
| badar | *bātăr | fire, flame | Noun |
| badron | *bātăr.nō | conflagration | Noun |
| maddar | *mā.bătār | to burn (transitive) | Verb |
| ammadar | *ām.bătār | to burn; be on fire | Verb |
| vom / óm | *vom | I | Pronoun |
| ren / én | *ren | you | Pronoun |
| ha / á | *ha | he/she | Pronoun |

---

## Appendix B: Angélico Dictionary (selected, romanized)

| Root | Form | POS | Gloss |
|---|---|---|---|
| badh- | badha | adj | hot |
| bedd- | beddes | n | dog |
| bokk- | bokkan | n | nail |
| chak- | chakkan | n | egg |
| dach- | dachtan | n | neck |
| dagh- | daghan | n | belly |
| dahh- | dahha | adj | small |
| damm- | damman | n | mouth |
| dard- | darda | adj | red |
| dars- | darsos / darses | n | man / woman |
| devn- | devna | adj | good |
| dohn- | dohnon | n | cloud |
| donm- | donmas | n | person, human |
| fagg- | faggon | n | smoke |
| gahm- | gahm- | v | to sleep |
| gand- | gandan | n | mountain |
| godr- | godr- | v | to see |
| gohr- | gohr- | v | to eat |
| gott- | gottan | n | night |
| horv- | horvas | pron | I |
| host- | hostan | n | skin |
| kahn- | kahn- | v | to walk |
| kakhan | kakhan | n | sun |
| kohnon | kohnon | n | water |
| kokkos | kokkos | n | fish |
| mavr- | mavr- | v | to die |
| monf- | monfon | n | star |
| naph- | naphan / naphe | n/num | moon / one |
| parran | parran | n | stone |
| pavkon | pavkon | n | fire |
| raddan | raddan | n | tooth |
| sathon | sathon | n | eye |
| sorgon | sorgon | n | bone |
| tarron | tarron | n | liver |
| tavnan | tavnan | n | head |
| tefren | tefren | n | heart |
| tennen | tennen | n | tree |
| tesbon | tesbon | n | earth |
| tetten | tetten | n | foot |
| vakk- | vakk- | v | to say |
| verden | verden | n | rain |

---

## Appendix C: Pavanam Numerals

| Number | Form |
|---|---|
| 1 | aste |
| 2 | auɡe |
| 3 | (unattested) |
| 4 | anka |
| 5 | (unattested) |
| 6 | mensa |
| 7 | ŋuasta |
| 8 | ɡuapan |
| 9 | ŋelɡen |
| 10 | iempo |
| 11 | oikko |
| 12 | kolko |

Note: 3 and 5 are unattested in the current lexicon. The presence of 7–12 suggests a counting system that extends beyond the basic Swadesh numerals. The ŋ-initial forms ŋuasta (7) and ŋelɡen (9) confirm word-initial ŋ in the numeral domain specifically.

---

*End of document. Version 1.0 — based on corpus analysis of 12 source files, June 2026.*
