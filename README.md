# Conlanging

## Syllable/word generator

`conlang_gen/` is a random syllable and word generator: plug in your own phoneme
inventory (JSON), or generate from a real language's phonology pulled from the
bundled PHOIBLE/BDPROTO/CLTS/Phonotacticon data in `data/`, with a naturalism
report scoring generated consonant clusters against what's actually attested.
See `conlang_gen/README.md` for usage.

## Mobile web app

`webapp/index.html` is a self-contained page (no build step, no server, no
dependencies) for picking phonemes and syllable shapes and generating words
straight from a phone browser: open the file directly, or serve the folder.
Tap sounds by manner/height, set syllable-shape weights, and generate — the
"Export inventory.json" button downloads a file in the same format
`conlang_gen` reads, so a phonology built on your phone can be dropped
straight into `inventories/` for the command-line tool.