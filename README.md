# Conlanging: Proto-Sevelian

A naturalistic **proto-language** (working name: *Proto-Sevelian*), built to serve as
the reconstructed ancestor of a family of daughter languages — the same way
Proto-Indo-European sits behind Latin, Greek, Sanskrit, and English.

The project follows the *Conlangs University* course materials (units 1–13),
completing each unit's assignment for the proto-language and, later, applying
sound changes and grammatical evolution to derive daughters.

## Layout

| Path | Contents |
|---|---|
| `docs/course-profile.md` | Index of the course units and project progress tracker |
| `docs/design-goals.md` | Vision, naming, and the diachronic design principles |
| `proto/01-phonology.md` | Phoneme inventory, romanization, allophony, accent |
| `proto/02-phonotactics.md` | Syllable & root structure, clusters, ablaut |
| `data/phonology.json` | Machine-readable inventory + phonotactic rules |
| `tools/wordgen.py` | Root generator (stdlib-only Python) for testing the phonology |

## Quick start

Generate 20 sample roots in e-grade:

```sh
python3 tools/wordgen.py -n 20
```

Render roots in another ablaut grade:

```sh
python3 tools/wordgen.py -n 10 --grade zero
```

## Conventions

- Reconstructed (i.e. all) Proto-Sevelian forms are cited with a leading asterisk: *séwol-.
- Phonemic notation stays close to IPA; see `proto/01-phonology.md` for the romanization.
- `data/phonology.json` is the single source of truth for the inventory; the prose
  docs explain and motivate it. If they disagree, fix whichever is wrong and say so
  in the commit message.

## Status

Foundations (phonology + phonotactics) — in progress. Morphology, verbs, nouns,
lexicon, and daughter-language derivation come next; see `docs/course-profile.md`.
