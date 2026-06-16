# Morphology — Design Specification

The morphological **type** for the project conlang, set from Morphology 1 and
grounded in WALS/Grambank. This is the high-level profile + word-structure
templates; the detailed **case** and **TAM** inventories are finalized in the
Nouns (05) and Verbs (04/09) modules.

> **Scope note.** Affixes below are **illustrative/provisional** and shown as
> **underlying forms only**. Morphophonology — the alternations at morpheme seams
> (final devoicing, intervocalic lenition, vowel reduction/harmony) — is
> **deferred** until the phonology's allophony is decided (see
> [`phonology.md` §3](phonology.md)).

---

## 1. Typological profile — "Bundle A" (agglutinating-suffixing)

| Axis | Choice | Grounding |
|---|---|---|
| Synthesis | **Moderately synthetic** (≈4–5 categories/word) | WALS 22A modal value |
| Fusion | **Agglutinating** — one category per morpheme (low exponence) | WALS 20A concatenative 76%; mono-exponence common |
| Locus | **Strongly suffixing** | WALS 26A 42%; Grambank verb-suffix 84% (98% in small-inventory langs) |
| Case | **Present, suffixal** (moderate inventory) | case → 74% OV; 62% of case langs use case *suffixes* |
| Word order | **SOV** (falls out of suffixing + case) | suffixing → 74% OV; case → 74% OV |
| Gender | **None** | WALS 30A "none" 56% |
| Reduplication | **Productive** (full + partial) | WALS 27A ~85%; Grambank 73–78% |
| Concatenativity | **Concatenative** | WALS 20A 76% |

These choices are **mutually reinforcing**, not independent: suffixing → OV →
suffixal case → high morpheme-count synthesis. The result is a self-consistent
"Turkic / Dravidian / Quechua-type" language — which is also the statistical
tendency for small-inventory languages like ours.

---

## 2. Word structure

- **Roots** are content morphemes; grammatical relations are carried by **bound
  suffixes** (and, where analytic, by particles). One suffix = one category.
- Affix slots are **ordered** and stack agglutinatively.

### 2.1 Noun template

```
ROOT - (NUMBER) - (CASE)
```

| Slot | Category | Illustrative affix |
|---|---|---|
| NUMBER | SG / PL | -∅ / **-ri** |
| CASE | NOM / ACC / GEN / DAT / LOC / INS | -∅ / **-n** / **-na** / **-ku** / **-ja** / **-mu** |

### 2.2 Verb template

```
ROOT - (ASPECT) - (TENSE) - (MOOD) - (SUBJECT)
```

| Slot | Category | Illustrative affix |
|---|---|---|
| ASPECT | PFV / IPFV | -∅ / **-li** |
| TENSE | NPST / PST / FUT | -∅ / **-ta** / **-su** |
| MOOD | IND / IRR | -∅ / **-ka** |
| SUBJECT | 1SG / 2SG / 3SG / PL | **-wa** / **-si** / -∅ / **-ri** |

*(Slot order is the canonical agglutinating order; the full category sets are
finalized in modules 04–05.)*

---

## 3. Glossing

The project adopts the **Leipzig Glossing Rules**. Because the language is
agglutinating, glosses are clean **one-morpheme : one-label** strings (contrast
the portmanteau glosses of fusional languages).

---

## 4. Worked examples (underlying forms)

Roots `tapa` "house", `kalu` "walk" (illustrative):

**Nouns**

```
tapa            house.NOM.SG     "a house"
tapa-n          house-ACC        "a house (object)"
tapa-ri-na      house-PL-GEN     "of the houses"
tapa-ri-ja      house-PL-LOC     "at the houses"
```

**Verbs**

```
kalu            walk.3SG          "s/he walks"
kalu-li-ta-wa   walk-IPFV-PST-1SG "I was walking"      (4 categories)
kalu-su-si      walk-FUT-2SG      "you will walk"
kalu-li-ta-ri   walk-IPFV-PST-PL  "they were walking"
```

Each morpheme maps to exactly one gloss — the agglutinating signature. (Surface
forms will differ once seam morphophonology is added.)

---

## 5. Reduplication

A productive, phonologically-defined process (set fully once syllable structure
is fixed):

- **Partial:** copy the first syllable (CV-) — e.g. *kalu* → *ka-kalu*.
- **Full:** copy the whole stem — e.g. *kalu* → *kalu-kalu*.
- Typical functions: plurality/distributivity (nouns), iteration/intensity (verbs).

---

## 6. Typological grounding

From the repo datasets (`scripts/extract_data.sh`):

- **WALS** — default profile: concatenative (20A 76%), strongly suffixing (26A 42%),
  4–5 cats/verb (22A 36%), suffixal case & TAM (51A/69A), no gender (30A 56%),
  productive reduplication (27A ~85%). Suffixing → **74% OV**; case → **74% OV**.
- **Grambank** (n≈2,300) — verb suffixes 84% (vs prefixes 68%), reduplication 73–78%,
  core-argument case 34%, plural marking 56%, aspect 67%, mood 70%.
- **Small-inventory check** — inventory size vs bound-morphology score: Pearson
  r = −0.11 (no complexity trade-off). Languages like ours (15–20 segments):
  verb suffixes **98%**, reduplication 78%, case 46%.

---

## 7. Lessons mapping (Morphology 1)

| Concept | Applied here |
|---|---|
| Inflection vs derivation | inflectional slots above; derivation (deverbal nouns etc.) → module 07 |
| Productivity | affixes are productive by default |
| Glossing | Leipzig rules adopted (§3) |
| Typology axes | analytic↔synthetic, fusional↔agglutinating fixed in §1 |
| Concatenativity | concatenative/suffixing; reduplication §5 |

---

## 8. Design decisions & open knobs

1. **Case inventory** (members + exact suffixes) — finalized in **Nouns (05a Case)**.
2. **TAM + agreement** categories and alignment — finalized in **Verbs (04/09)** and
   **Alignment (05d)**.
3. **Agglutinating now vs. fusional drift** — a *diachronic* choice (let sound change
   erode/​fuse suffixes later); not a conflict.
4. **Reduplication functions** — to be pinned down.
5. **Derivation** processes (deverbal nouns, compounding) — module 07 (Lexicon).
6. **Morphophonology** (seam alternations) — **deferred** until allophony is set.
