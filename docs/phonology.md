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

## 2. Phonotactics

- **Syllable template:** `(C) V (C)` — optional onset, short vowel nucleus,
  optional coda. *(Design choice — see §10. No underlying clusters or long vowels.)*
- **Onset:** any single consonant.
- **Coda:** any single consonant (subject to the coda rules in §5).
- **Surface CVV / CVC** both occur; CVV arises only from lengthening (§4–5).

---

## 3. Prosody: weight, mora & stress

- **Mora (μ):** short V = 1μ; a coda consonant adds 1μ; a derived long V = 2μ.
- **Weight:** a syllable is **heavy** if its rhyme branches — i.e. it has a coda
  **or** a long nucleus (2μ); otherwise **light** (CV, 1μ).
  - Underlyingly, only **codas** make a syllable heavy (no underlying long vowels).
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

Each shows the system working: palatalization + lengthening + spirantization +
final-vowel reduction (*sibi*); nasal assimilation + nasalization + reduction
(*tanka*); lengthening + spirantization + final devoicing + reduction (*lubad*);
compensatory lengthening preserving weight (*kasma*).

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

1. **Syllable template `(C)V(C)`** — simple/moderate. Could add onset clusters or a
   coda sonority hierarchy (Phonology 2).
2. **Stress = Latin weight-sensitive rule** — one of several attested weight-sensitive
   systems; could instead be fixed initial/penult (WALS 14A) or unbounded.
3. **Length & nasal vowels allophonic** (not phonemic) — promotable later.
4. **Compensatory lengthening (B3) is optional/diachronic** and scoped to coda
   /s h/ pre-C and word-final coda nasals — scope can widen or narrow.
5. **/l/ vs /r/ kept as two phonemes** (the 39 % pattern); could collapse to one
   liquid with [l]~[ɾ] allophony instead.

Questions worth deciding next: stress-rule variant, whether to add geminates
(referenced by E1), and whether to allow tautosyllabic diphthongs.
