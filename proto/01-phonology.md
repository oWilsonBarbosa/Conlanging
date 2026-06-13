# Proto-Sevelian Phonology

*(Course units 2 & 10 — phoneme inventory, romanization, allophony, accent.)*

All forms are reconstructions and are cited with a leading asterisk.

## Consonants (22)

### Stops — three series × four places

| | Labial | Dental | Velar | Labiovelar |
|---|---|---|---|---|
| **Voiceless** | *p | *t | *k | *kʷ |
| **Voiced** | *b | *d | *g | *gʷ |
| **Aspirated** | *pʰ | *tʰ | *kʰ | *kʷʰ |

Notes:
- *b is rare (as in PIE) — low weight in the generator, and a ready-made
  asymmetry for daughters to repair.
- The labiovelars are single segments, not clusters: *kʷ contrasts with *kw
  (e.g. zero-grade of a *kew- root).

### Laryngeals

| Phoneme | Assumed value | Effect on adjacent *e |
|---|---|---|
| *h₁ | [ʔ] | none |
| *h₂ | [χ] | colors to [a] |
| *h₃ | [ʁʷ] | colors to [o] |

Laryngeals pattern as ordinary consonants in the phonotactics (they fill root
C-slots, e.g. *deh₃- "give"). Their coloring is allophonic in the proto-language;
in daughters the laryngeals will be lost with compensatory lengthening, turning
the colored qualities phonemic — the classic engine of vowel-system divergence.

### Fricative

Just **\*s**, with allophone [z] adjacent to voiced stops (*nisdós → [nizdós]).
The near-empty fricative row is deliberate headroom: daughters gain fricatives
through lenition and palatalisation (unit 11).

### Resonants

**\*m \*n \*r \*l \*y \*w** — each has a syllabic allophone when no vowel is
adjacent (between consonants or word-finally after a consonant):

| Consonantal | *m | *n | *r | *l | *y | *w |
|---|---|---|---|---|---|---|
| Syllabic | m̥ | n̥ | r̥ | l̥ | i | u |

So [i] and [u] are not independent vowel phonemes; they are the syllabic forms
of the glides (PIE-style). Different daughter branches will resolve the syllabic
nasals/liquids with different epenthetic vowels.

## Vowels

| | Short | Long |
|---|---|---|
| Mid front | *e | *ē |
| Mid back | *o | *ō |
| Low | *a | *ā |

- **\*e** is the default root vowel; **\*o** and **∅** (zero) arise by ablaut
  (see `proto/02-phonotactics.md`).
- **\*a** is marginal outside the neighborhood of *h₂ — many surface [a]s are
  /e/ colored by a laryngeal. Independent *a appears mainly in expressive and
  borrowed vocabulary.
- Long vowels arise chiefly from ablaut lengthened grade and (diachronically)
  laryngeal loss.

## Accent (unit 10)

Free, mobile **pitch accent**: one syllable per word carries a high tone, marked
with an acute (*sewél-, *séwol-). Position is lexical and morphological — suffixes
and ablaut grades can shift it (accent–ablaut paradigms, as in PIE and Vedic).
Clitics are unaccented.

Diachronic intent: branches can (a) fixate stress initially or on the penult and
syncopate unaccented vowels, (b) convert the pitch contrast into tone, or
(c) run Verner-style voicing conditioned on accent position.

## Allophony summary (kept light)

| Rule | Notation | Category (unit 11 terms) |
|---|---|---|
| /s/ voices next to voiced stops | s > [z] / adjacent to voiced stop | assimilation |
| Resonants vocalise between consonants | R > [R̥] / C_C, C_# | — (syllabicity) |
| /e/ colored by laryngeals | e > [a] / adjacent to h₂; e > [o] / adjacent to h₃ | assimilation |
| Nasals assimilate in place to a following stop | n > [m] / _P, [ŋ] / _K | assimilation |

## Romanization

Identical to the phonemic notation above: ⟨p t k kʷ b d g gʷ pʰ tʰ kʰ kʷʰ s
m n r l y w h₁ h₂ h₃ e o a ē ō ā⟩, syllabic resonants ⟨m̥ n̥ r̥ l̥ i u⟩, acute
for accent. ASCII fallbacks for filenames/code: `kw gw ph th kh kwh h1 h2 h3`.
