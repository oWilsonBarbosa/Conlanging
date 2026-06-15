# Phonology — Design Specification

A working phonology for the project conlang, built across the course's Phonology
modules (1–4) and validated against the repo's datasets (PHOIBLE, WALS, PBASE).
Design philosophy: a **small, contrast-light inventory** whose realism comes from
**allophony and prosody** rather than a large phoneme count.

> **Notation.** `/…/` phonemes · `[…]` surface phones · `.` syllable break ·
> `ˈ` primary stress · `ː` long · ` ̃ ` nasalized · rules read `A → B / X _ Y`.

---

## 1. Phoneme inventory (14 C + 3 V)

### Consonants

| | Labial | Coronal | Palatal | Velar | Glottal |
|---|---|---|---|---|---|
| Plosive (vl.) | p | t | | k | |
| Plosive (vd.) | b | d | | ɡ | |
| Nasal | m | n | | | |
| Fricative | | s | | | h |
| Liquid | | l  r | | | |
| Glide | w | | j | | |

### Vowels

| | Front | Central | Back |
|---|---|---|---|
| Close | i | | u |
| Open | | a | |

**Notes**

- Written ⟨g⟩ = /ɡ/ (IPA script-g) and ⟨y⟩ = /j/ — orthography vs. phonemes
  (Phonology 1). Romanization can keep ⟨g, y⟩.
- **Vowel length is *not* contrastive.** Long [Vː] is always derived (stressed-open
  lengthening §4, compensatory lengthening §5). Promoting length to phonemic is an
  easy later step (Phonology 4).
- **/j w/ are phonemes**, distinct from syllabic [i u]; [i u] are nuclei, [j w] are
  margins. (Minimal pairs like /ia/ vs /ja/ carry the contrast.)

---

## 2. Syllable structure & phonotactics

### 2.1 Template
Canonical maximal syllable: **(C)(C) V (V) (C)** — an onset of up to two
consonants, a nucleus that is a short vowel or a diphthong, and a single coda.
Attested shapes: CV, CVC, CCV, CCVC, CVV, CVVC. *(Moderately complex — the
cross-linguistic plurality, WALS 12A; see §10 for the simple↔complex knob.)*

### 2.2 Sonority hierarchy
Clusters are governed by sonority (Phonology 2). Scale, most→least sonorous (as
given in the course deck):

> **vowels > glides /j w/ > liquids /r l/ > nasals /m n/ > fricatives /s h/ > voiced stops /b d ɡ/ > voiceless stops /p t k/**

(within classes: low /a/ > high /i u/; rhotic /r/ > lateral /l/.)

### 2.3 Onsets — Sonority Sequencing Principle (SSP)
Sonority must **rise** from the onset toward the nucleus:
- **Single onset:** any consonant.
- **CC onset:** C₂ must be **more sonorous than C₁** — in practice a **liquid or glide**:
  - obstruent + liquid — /pl pr kl kr bl br ɡl ɡr tr dr/ ( */tl dl/ excluded, marked)
  - obstruent + glide — /pj pw tj tw kj kw bj sj …/
  - nasal + glide — /mj nj mw nw/
  - *(optional /s/-appendix: /sp st sk/ — SSP-violating but common; off by default, §10)*

This is exactly the deck's rule (*"initial stops may only be followed by
approximants or glides"*) and matches Phonotacticon's top onsets — all formable
from this inventory.

### 2.4 Nucleus & diphthongs
- **Nucleus:** a short vowel /i a u/ **or a diphthong** (one branching nucleus —
  per the course, two vocoids in a single syllable count as one unit).
- **Diphthongs:** core /ai̯ au̯/; marginal /ui̯ iu̯/; homorganic */ij uw/ banned.
- A diphthong is **heavy** (2 μ). (Phonemically analyzable as /Vj Vw/; treated as a
  branching nucleus for weight — §10.)
- Long monophthongs [Vː] are **derived only** (§4–5).

### 2.5 Codas
- **Single coda (default):** any consonant — subject to final devoicing (B2) and
  nasal place assimilation (B1).
- **CC coda (optional extension):** sonorant + obstruent, **falling** sonority —
  /rt rk lt lk nt mp ns rs ks st/ (the Phonotacticon coda profile). Off by default (§10).

### 2.6 Maximal Onset Principle (syllabification)
Per the deck: *"if an intervocalic consonant can be assigned to the onset without
breaking other rules … it is."* Maximize the following onset within legality; the
remainder becomes the coda of the preceding syllable:

| Input | Legal onset? | Syllabification | Why |
|---|---|---|---|
| /patra/ | /tr/ ✓ | pa.tra | rising-sonority onset preferred |
| /panta/ | /nt/ ✗ (falling) | pan.ta | /n/ stranded → coda |
| /akra/ | /kr/ ✓ | a.kra | |
| /paila/ | nucleus /ai/ | pai.la | diphthong = one nucleus |
| /aspa/ | /sp/ only with appendix | as.pa (default) · a.spa (appendix) | §2.3 |

MOP feeds the prosody: a stranded coda (pan.ta) makes the syllable **heavy**,
which drives weight-sensitive stress (§3).

---

## 3. Prosody: weight, mora & stress

- **Mora (μ):** short V = 1μ; a coda consonant adds 1μ; a diphthong or derived long V = 2μ.
- **Weight:** a syllable is **heavy** if its rhyme branches — i.e. it has a coda
  **or** a branching nucleus (diphthong / long V, 2μ); otherwise **light** (CV, 1μ).
  - Underlyingly, **codas and diphthongs** make a syllable heavy (no underlying long monophthongs).
- **Stress — weight-sensitive, right-edge moraic trochee** ("Latin Stress Rule"):
  1. The **final** syllable is extrametrical (skipped).
  2. Stress the **penult** if it is **heavy**; otherwise stress the **antepenult**.
  3. Disyllables: stress the penult (= initial). Monosyllables: stressed.
- **Rhythm:** trochaic (left-headed feet).

*Stress is computed on underlying (coda-based) weight, before the lengthening and
lenition rules — so those rules cannot disturb stress placement.*

---

## 4. Phonological rules (ordered)

Applied top-to-bottom. Grouping follows the "weak-position vs. strong-position"
logic (Phonology 3 formalism).

### Block A — Prosody
- **A1 Syllabify** into `(C)V(C)`; assign weight (§3).
- **A2 Stress** (weight-sensitive Latin rule, §3).

### Block B — Coda / syllable-position effects *(weak position)*
- **B1 Nasal place assimilation** (coda, regressive):
  `n → ŋ / _]σ {k, ɡ}` · `n → m / _]σ {p, b}` · `n → ɲ / _ j`
- **B2 Final devoicing:** `{b, d, ɡ} → {p, t, k} / _#`
- **B3 Compensatory lengthening** *(optional / diachronic):*
  `{s, h} → ∅ / V _ C` with `V → Vː` ·  coda `N → ∅ / _#` with `V → Ṽː`
  (mora-preserving — see §5).

### Block C — Onset / pre-front segmental effects
- **C1 Palatalization** (before /i, j/):
  `{k, ɡ} → [tʃ, dʒ]` · `{t, d} → [tʃ, dʒ]` · `s → ʃ` · `n → ɲ` · `l → ʎ`  `/ _ {i, j}`
  *(kept segmental; ordered before laxing so it stays opaque, §5)*

### Block D — Vowel quality *(stress / length / weight)*
- **D1 Stressed-open lengthening:** `V → Vː / ˈσ[ _ ]` (in a **stressed open** syllable)
- **D2 Laxing / reduction** (short vowels only; long/tense vowels exempt):
  `{i, u} → [ɪ, ʊ] / closed σ` · `{i, a, u} → [ɪ, ə, ʊ] / unstressed`

### Block E — Weak-position lenition & nasalization
- **E1 Intervocalic spirantization:** `{b, d, ɡ} → [β, ð, ɣ] / V _ V`
  (stronger in **unstressed** feet; geminates, if added, resist)
- **E2 Vowel nasalization:** `{i, a, u} → [ĩ, ã, ũ] / _ N` (tautosyllabic;
  enhanced under stress) — N includes assimilated [ŋ ɲ] from B1.

---

## 5. Rule ordering & interactions

The order above is engineered for these feeding/bleeding/opacity effects:

- **A2 → D1/D2** *(feeding):* stress is assigned before the vowel rules that
  reference it.
- **C1 → D2** *(counterbleeding = opacity):* /i/ triggers palatalization, then may
  lax/reduce — so you get **[tʃ] before surface [ɪ]/[ə]**, with no visible trigger.
- **B1 → E2** *(feeding):* coda /n/ → [ŋ] first, then the vowel nasalizes before it
  (e.g. /anka/ → [ãŋ.ka]).
- **D1 → D2** *(bleeding):* a stressed open vowel lengthens (→ tense long) and is
  then exempt from laxing — this **is** the *tense-long ↔ lax-short* split.
- **B3 is mora-preserving:** a coda deletes but its μ re-docks on the vowel
  (CVC 2μ → CVː 2μ), so weight — and therefore stress — is unchanged whether B3
  precedes or follows A2.
- **Weight ≠ tenseness:** a closed syllable is *heavy* but its short nucleus still
  *laxes* (B/D operate on different units — syllable vs. segment).

---

## 6. Worked derivations

| Underlying | A2 stress | B (coda) | C (palat.) | D (vowels) | E (lenition/nasal) | **Surface** |
|---|---|---|---|---|---|---|
| /sibi/ | ˈsi.bi | — | ˈʃi.bi | ˈʃiː.bɪ | ˈʃiː.βɪ | **[ˈʃiːβɪ]** |
| /tanka/ | ˈtan.ka | ˈtaŋ.ka | — | ˈtaŋ.kə | ˈtãŋ.kə | **[ˈtãŋkə]** |
| /lubad/ | ˈlu.bad | ˈlu.bat | — | ˈluː.bət | ˈluː.βət | **[ˈluːβət]** |
| /kasma/ (B3 on) | ˈkas.ma | ˈkaː.ma | — | ˈkaː.mə | — | **[ˈkaːmə]** |
| /trapi/ | ˈtra.pi (MOP: tra.pi) | — | — | ˈtraː.pɪ | — | **[ˈtraːpɪ]** |
| /paila/ | ˈpai.la (diphthong) | — | — | ˈpai.lə | — | **[ˈpailə]** |

Each shows the system working: palatalization + lengthening + spirantization +
final-vowel reduction (*sibi*); nasal assimilation + nasalization + reduction
(*tanka*); lengthening + spirantization + final devoicing + reduction (*lubad*);
compensatory lengthening preserving weight (*kasma*); MOP onset-cluster
syllabification + lengthening (*trapi*); and a heavy diphthong nucleus attracting
stress (*paila*).

---

## 7. Diachronic outlook (Phonology 4)

Every allophonic split here is a **phonemicization waiting to happen** — the way
daughter languages would be derived from this proto-system:

- Lose the conditioning vowel and **[ʃ tʃ dʒ ɲ ʎ]** (palatals), **[ŋ]** (velar
  nasal), and **[β ð ɣ]** (voiced fricatives) become contrastive.
- Coda-nasal deletion (B3) phonemicizes **nasal vowels /ĩ ã ũ/** (French path;
  cross-linguistically the endpoint in ~26% of languages, WALS 10A).
- Stressed-open lengthening + CL phonemicize a **vowel-length contrast**.

---

## 8. Typological grounding

Computed from the repo datasets (see `scripts/extract_data.sh`):

- **PHOIBLE** (N = 3,020 inventories) — every phoneme is high-frequency; the chosen
  allophones are the common ones: /n/→[ŋ] 9 %, /s/→[ʃ] 9 %, /ɡ/→[ɣ] 7 %, /b/→[β] 5 %,
  /i/→[ɪ] 7 %, /a/→[ã] 5 %, /i/→[ĩ] 4 %. A two-liquid /l r/ contrast occurs in 39 %.
- **WALS** — weight-sensitive stress ≈ 44 % of languages; when weight matters it is
  defined by **long vowels (13 %) and/or codas** (16A) — i.e. the mora; trochaic
  rhythm 47 % (17A); 87 % of languages allow codas (12A); contrastive nasal vowels
  26 % (10A).
- **PBASE** (7,319 rules) — process frequency **assimilation ≫ deletion ≳ lenition**;
  prosodic conditioning is common: syllable-position 7.5 %, length 6.4 %, stress
  4.0 % (e.g. *"stressed short /i/ → [ɛ]"*, *"unstressed → ∅"*).
- **Phonotacticon** (457 lects) — CC onsets are modal (41 %; 34 % single-C, 21 %
  CCC); single codas modal (53 %; 34 % CC). Top onsets are obstruent + liquid/glide
  (/pl kl pr kr bl br tr · pj kj kw mj nj/), top codas sonorant + obstruent
  (/nt nd rt rk mp lt lk · st ks/) — every one formable from this inventory.

---

## 9. Lessons mapping

| Module | Applied here |
|---|---|
| Phonology 1 | inventory, IPA, phoneme/allophone, complementary distribution |
| Phonology 2 | symmetry & gaps, syllable structure, sonority, naturalism (PHOIBLE/WALS) |
| Phonology 3 | distinctive features, natural classes, ordered rule notation; [±stress],[±long] |
| Phonology 4 | sound change: lenition, compensatory lengthening, phonemicization |

---

## 10. Design decisions & open knobs

Choices made to instantiate the system — all adjustable:

1. **Syllable template `(C)(C)V(V)(C)`** (§2) — moderately complex. Toggles: the
   **/s/-appendix onset** (/sp st sk/) and the **CC coda** (sonorant+obstruent) are
   off by default; turning both on makes it "complex," dropping CC onsets makes it
   "simple" (WALS 12A).
2. **Stress = Latin weight-sensitive rule** — one of several attested weight-sensitive
   systems; could instead be fixed initial/penult (WALS 14A) or unbounded.
3. **Length & nasal vowels allophonic** (not phonemic) — promotable later.
4. **Compensatory lengthening (B3) is optional/diachronic** and scoped to coda
   /s h/ pre-C and word-final coda nasals — scope can widen or narrow.
5. **/l/ vs /r/ kept as two phonemes** (the 39 % pattern); could collapse to one
   liquid with [l]~[ɾ] allophony instead.
6. **Diphthongs** analyzed as branching nuclei /ai̯ au̯/ (core); could instead be
   /Vj Vw/ coda-glide sequences, or be dropped entirely.

Questions worth deciding next: the /s/-appendix and CC-coda toggles, whether to add
geminates (referenced by E1), and which marginal diphthongs (/ui̯ iu̯/) to admit.
