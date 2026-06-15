# Verbs — Design Specification

The verb system (Verbs 1, module 04), consistent with the morphology profile
(**Bundle A**: agglutinating, suffixing). The verb is the most synthetic word in
the language.

> **Scope note.** Argument **alignment** (nominative-accusative vs. ergative; case
> of S/A/P) is finalized in **Alignment (05d)** — accusative is assumed here.
> Affixes are **illustrative/provisional** and shown as **underlying forms only**;
> morphophonology (seam alternations) is **deferred** until allophony is set
> ([`phonology.md` §3](phonology.md)).

---

## 1. Valency & transitivity

- Verbs are classed by **valency** (total arguments) / **transitivity** (non-subject
  arguments): **intransitive** (S only), **transitive** (+ object), **ditransitive**
  (+ two objects).
- **Valency-changing** morphology (suffixal, near the root):
  - **Causative** `-pa` — adds a causer ("walk" → "make walk"), +1 argument.
  - **Passive** `-wi` — demotes the subject ("X sees Y" → "Y is seen"), −1 core argument.
  - *Antipassive* — **skipped** (rare, 9%; ergative-linked → revisit in 05d).

## 2. Agreement

- The verb agrees with its **subject** in **person + number** (no gender — there is
  no gender system). Alignment: **accusative** (default; see 05d).
- **Pro-drop:** because the subject is indexed on the verb, the subject pronoun may
  be omitted.
- Agreement suffixes (outermost slot):

| | Singular | Plural |
|---|---|---|
| 1 | **-wa** | **-wari** |
| 2 | **-si** | **-siri** |
| 3 | **-∅** | **-ri** |

*(Plural = person suffix + `-ri`; agglutinating. **Polypersonal** agreement —
indexing the object too — is an available richer option, deferred.)*

## 3. Tense — *event relative to "now"*

- **Past** `-ta` vs **non-past** `-∅` (covers present + future).
- **Future** `-su` — optional inflectional future.
- **No remoteness** distinctions (single past).

## 4. Aspect — *internal shape of the event*

- **Perfective** `-∅` (bounded whole) vs **imperfective** `-li` (ongoing/durative).
- Own slot, independent of tense (so past × imperfective = "was V-ing").
- *Habitual* — optional future addition.

## 5. Mood — *speaker's stance on truth*

- **Indicative** `-∅` (factual), **imperative** (command), **irrealis/subjunctive**
  `-ka` (hypothetical/wished/doubted).
- *Prohibitive* (negative command) — optional.

## 6. Negation

**Open choice:** a negative **suffix** (fits the suffixing profile) vs. a standalone
negative **particle** (~50/50 cross-linguistically). Provisionally leaning suffixal;
to be fixed.

---

## 7. Verb template & paradigm

Suffix order, derivation/valency nearest the root, agreement outermost:

```
ROOT - (CAUSATIVE) - (PASSIVE) - (ASPECT) - (TENSE) - (MOOD) - SUBJECT(person·number)
```

Worked forms (underlying), root `kalu` "walk":

```
kalu                 walk.NPST.3SG          "s/he walks"
kalu-wa              walk-1SG               "I walk"
kalu-li-ta-wa        walk-IPFV-PST-1SG      "I was walking"
kalu-su-si           walk-FUT-2SG           "you will walk"
kalu-pa-ta-wa        walk-CAUS-PST-1SG      "I made (someone) walk"
kalu-wi-ta           walk-PASS-PST          "(it) was walked"
kalu-ka-wa           walk-IRR-1SG           "I might/would walk"
```

Non-past perfective indicative conjugation:

| | Singular | Plural |
|---|---|---|
| 1 | kalu-wa | kalu-wari |
| 2 | kalu-si | kalu-siri |
| 3 | kalu | kalu-ri |

A fully loaded verb carries ~5 categories → the WALS "4–5 categories/verb" norm,
each morpheme = one gloss (the agglutinating signature).

---

## 8. Typological grounding

From the repo datasets:

- **Agreement:** subject indexing 66%, object 49%, polypersonal 43% (Grambank);
  alignment **accusative 56%** (WALS 100A). Subject-only person/number = safe default.
- **Tense:** past present in ~58% of languages, mostly **no remoteness** (WALS 66A);
  future ~45–50% (67A/GB084). TAM **suffixal** 59% (69A).
- **Aspect:** perfective/imperfective common (GB086 67%, WALS 65A 45%).
- **Mood:** imperative near-universal (WALS 70A); optative rare 15% (73A); mood
  marking 70% (GB312).
- **Valency:** causative **73%**, transitivizer 70%, passive 43%, antipassive 9% (GB).

## 9. Lessons mapping (Verbs 1) — assignment answers

1. **Agreement:** subject only, in person + number (no gender); stands in for pronouns (pro-drop).
2. **Temporal:** *tense* = past vs non-past (+ optional future); *aspect* = perfective vs imperfective, in a separate slot. They combine freely (past+imperfective = "was V-ing").
3. **Mood:** indicative, imperative, irrealis marked morphologically; other modality via irrealis (+ particles).
4. **Marking:** suffixing, agglutinative, synthetic (~4–5 categories/verb) — per Bundle A.

## 10. Open knobs

1. **Subject-only vs polypersonal** agreement.
2. **2-way (past/non-past) vs 3-way (past/present/future)** tense.
3. **Negation:** suffix vs particle.
4. **Alignment** (nom-acc vs ergative) → module **05d**.
5. Additional **aspects/moods** (habitual, prohibitive, conditional…) and the full
   **valency-operation** set.
