# Lesson 05 — Nouns 1 (Alignment, Case, Number, Class)

- **CU lesson:** <https://sites.google.com/view/conlangs-university/lessons> (Nouns 1)
- **Date:** 2026-06-14
- **Goal:** set Alantian's noun system — starting with alignment.

## Decisions (settled)

- **Alignment: split-ergative by aspect.**
  - **Imperfective** → nominative–accusative (S = A unmarked, P = accusative).
  - **Perfective / perfect** → ergative–absolutive (S = P unmarked, A = ergative).
- **Core case system:** unmarked **DIRECT** + **ERGATIVE** + **ACCUSATIVE**.
  - S always DIRECT; A is ERG only in pfv/perfect; P is ACC only in impfv.

| role | Imperfective | Perfective / Perfect |
|---|---|---|
| S | DIRECT | DIRECT |
| A | DIRECT | ERGATIVE |
| P | ACCUSATIVE | DIRECT |

## Why it fits

- Ties the **noun** system to the **aspect** system already built (Hindi/Georgian-type
  TAM split) — distinctive, naturalistic, and "ancient" (cf. old ergative languages).
- In the perfective the **agent** is marked (ergative), foregrounding the result — a
  natural semantic match to perfective aspect.

## Characterization vs. real languages

| Trait | Parallel |
|---|---|
| Aspect-based split ergativity | **Hindi/Urdu, Georgian, Kurdish** |
| Ergativity as the "ancient" flavour | **Sumerian, Hurrian** |

## Sources consulted

| Source | What | How it informed |
|---|---|---|
| WALS 98A (alignment of case marking), 99A (of pronouns) | Distribution of erg/acc/split systems | Confirms aspect-based split ergativity is well-attested |
| WALS 100A (alignment of verbal person marking) | Agreement alignment | Flags that agreement may split too (TBD) |
| Grambank | Ergative/accusative case features | Validates the split design |

## Case marking = reduplication (established by worked examples)

Core case reuses the **reduplicative morphology** (like verb TAM):

| case | marking | dog | man |
|---|---|---|---|
| DIRECT | bare + echo vowel | kutu | kara |
| ERGATIVE | final redup → geminate (= verbal N.PST) | kuttu | karra |
| ACCUSATIVE | initial redup (= verbal PST) | kuitu | kagar/kair |

Also established: **word order SOV** (verb-final); **echo-vowel epenthesis** for C-final
roots (kut → kutu).

### Worked sentences (lexicon: kut- dog, kar- man, iana see, nata sleep)

| Alantian | gloss |
|---|---|
| kutu ianna | dog-DIR see.N.PST.IPFV — "dog sees" |
| kara īna | man-DIR see.PST.PFV — "man saw" |
| kutu nanda | dog-DIR sleep.PST.IPFV — "dog was sleeping" |
| kara natti | man-DIR sleep.N.PST.PFV — "man will sleep" |
| kutu kagar ianna | dog-DIR man-ACC see.IPFV — "dog sees man" (nom-acc) |
| kara kuitu ianna | man-DIR dog-ACC see.IPFV — "man sees dog" |
| kuttu kara īna | dog-ERG man-DIR see.PFV — "dog saw man" (erg-abs) |
| karra kutu īna | man-ERG dog-DIR see.PFV — "man saw dog" |

## Outputs

- [x] `grammar.md` — Nouns: alignment + case-by-reduplication (DIRECT/ERG/ACC); SOV
- [x] `lexicon.csv` — first entries (kut, kar, iana, nata)
- [ ] oblique cases, number, class

## Open / next

- **Case markers** (DIRECT/ERG/ACC forms) — ideally derived diachronically.
- **Oblique cases** (genitive, dative, locative, …) — inventory size.
- **Number** (sg/pl; dual? collective?).
- **Noun class / gender** (none? animacy? Bantu-style classes?).
- **Agreement** split in parallel with case (with the verb agreement system).

## License note

Nothing reproduced from external sources; typological comparison only.
