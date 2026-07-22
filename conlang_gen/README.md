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

- **BDPROTO** — phoneme inventories for ~800 languages and proto-languages.
- **CLTS (BIPA)** — canonical IPA symbol lists, used to classify each BDPROTO
  phoneme as a consonant or vowel.
- **Phonotacticon** — attested onset/coda consonant clusters for ~500
  languages, matched to BDPROTO via Glottocode.

Find a language name:

```
python -m conlang_gen search-language hawaiian
```

Generate words from its real phoneme inventory, and get a naturalism report:

```
python -m conlang_gen from-language Hawaiian --count 20
```

This prints the derived consonant/vowel split, generates words with
generic-but-plausible syllable shapes (biased toward that language's actual
cluster complexity when a Phonotacticon match is found), and reports:

- average syllables per word and consonant/vowel ratio
- **onset/coda legality rate**: of the multi-consonant clusters the
  generator produced, what fraction are actually attested for that language
  in Phonotacticon. This is the main "how naturalistic is this?" signal —
  low rates mean the generator is inventing clusters that don't occur in the
  real language.

Note this only checks clusters, since BDPROTO gives a phoneme *inventory*,
not a corpus of real syllables — single consonants/vowels are always
"legal." Phonotacticon coverage is also a sample of each language's
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
