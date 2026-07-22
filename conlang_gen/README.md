# conlang_gen

A random syllable and word generator for conlangs, with tools to test how
naturalistic the output is against real-world phonology data.

No dependencies beyond the Python standard library (3.10+).

## Generate from your own phoneme inventory

Inventories are plain JSON files. Start from the template:

```
python -m conlang_gen new-inventory --output inventories/my_conlang.json
```

Edit `consonants`, `vowels`, and `syllable_patterns` (made of `C`/`V` slots,
each with a relative weight), then generate words:

```
python -m conlang_gen generate --inventory inventories/my_conlang.json --count 20
```

See `inventories/example.json` for a filled-out example, including
`illegal_sequences` (a simple substring blocklist applied across syllable
boundaries, e.g. to forbid `"kg"`) and `word_length_weights` (relative
likelihood of 1-, 2-, 3-syllable words).

## Test against real languages

`data/` already contains bundled linguistic databases:

- **PHOIBLE** (default source) — phoneme inventories for ~2,700 living and
  historical languages, each phoneme explicitly labeled consonant/vowel/tone.
  Some language names have multiple independent source inventories; pick one
  with `--inventory-id` (the command lists the alternatives).
- **BDPROTO** (`--source bdproto`) — phoneme inventories for ~800 languages,
  mostly reconstructed proto-languages (e.g. `Proto-Polynesian`). Has no
  consonant/vowel column of its own, so phonemes are classified using
  **CLTS (BIPA)**'s canonical IPA symbol lists.
- **Phonotacticon** — attested onset/coda consonant clusters for ~500
  languages, matched to PHOIBLE/BDPROTO via Glottocode (281 PHOIBLE languages
  and 5 BDPROTO languages currently overlap).

Find a language name:

```
python -m conlang_gen search-language hawaiian
python -m conlang_gen search-language proto --source bdproto
```

Generate words from its real phoneme inventory, and get a naturalism report:

```
python -m conlang_gen from-language Hawaiian --count 20
python -m conlang_gen from-language English --inventory-id 2252 --count 20
```

This prints the derived consonant/vowel split, generates words with
generic-but-plausible syllable shapes (biased toward that language's actual
cluster complexity when a Phonotacticon match is found), and reports:

- average syllables per word and consonant/vowel ratio
- **onset/coda legality rate**: of the multi-consonant clusters the
  generator produced, what fraction are actually attested for that language
  in Phonotacticon. This is the main "how naturalistic is this?" signal —
  low rates mean the generator is inventing clusters that don't occur in the
  real language. For example, `from-language English` typically lands
  around 10-15% onset legality and near 0% coda legality, showing that
  naive random consonant-clustering is far from how English actually
  clusters sounds.

Note this only checks clusters, since PHOIBLE/BDPROTO give a phoneme
*inventory*, not a corpus of real syllables — single consonants/vowels are
always "legal." Phonotacticon coverage is also a sample of each language's
attested wordlist, not an exhaustive phonotactic grammar, so treat the rate
as a rough signal, not a certainty.

You can save the derived inventory to tweak by hand:

```
python -m conlang_gen from-language Hawaiian --save-inventory inventories/hawaiian.json
```

## Using it as a library

```python
import random
from conlang_gen import Inventory, generate_words

inventory = Inventory.load("inventories/example.json")
words = generate_words(inventory, count=10, rng=random.Random(42))
print([w.text for w in words])
```
