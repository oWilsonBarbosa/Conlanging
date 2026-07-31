"""Gerador de palavras do Proto-Orogeniano.

Respeita a fonotática derivada em docs/02_PROTO_OROGENIAN_PHONOLOGY.md §4,
que por sua vez foi medida sobre as 873 raízes de PIE_roots.

  onset   (s)(C)(R)     máx. 3
  núcleo  V | R̩
  coda    (R)(C)(s)     máx. 3

Restrições ativas:
  - dissimilação glotálica: no máximo uma obstruinte glotalizada por raiz
    (medido: 1 raiz em 216 com duas — `gʷeg-`)
  - sem /ʔp/ (lacuna sistemática do sistema glotálico)
  - sequenciamento de sonoridade, com a exceção de /s/ nas bordas

Uso:
    python3 gen.py [n] [--seed N] [--roots|--words]

Sem dependências externas.
"""

import random
import sys

from inventory import (OBSTRUENTS, SONORANTS, NASALS, LIQUIDS, GLIDES,
                       VOWELS, LONG_VOWELS, SYLLABIC, is_glottalized, agrees)

# Pesos das posições de onset e coda, proporcionais à contagem sobre as
# raízes do PIE (docs/02 §4). "C" = obstruinte, "R" = sonorante.
ONSET_SHAPES = [
    ("C", 275), ("R", 147), ("CR", 108), ("H", 86), ("HR", 67),
    ("sC", 60), ("s", 38), ("sR", 33), ("", 30), ("RR", 12),
    ("sCR", 9), ("CC", 5),
]
CODA_SHAPES = [
    ("RC", 227), ("R", 164), ("C", 127), ("RH", 124), ("H", 68),
    ("Rs", 39), ("HC", 35), ("s", 22), ("HR", 20), ("", 20),
    ("CH", 7), ("Hs", 6),
]

# "H" no esqueleto = laringal. No Proto-Orogeniano as laringais são a coluna
# uvular: /qː/ (→ *h₂), /qʷː/ (→ *h₃) e as não-fortis /q ʔq qʷ ʔqʷ/, que
# colapsam em *h₁ na fase terrestre.
LARYNGEALS = ["qː", "qʷː", "q", "ʔq", "qʷ", "ʔqʷ"]
NON_LARYNGEAL = [o for o in OBSTRUENTS if o not in LARYNGEALS]


def _pick(shapes, rng):
    total = sum(w for _, w in shapes)
    r = rng.uniform(0, total)
    for shape, w in shapes:
        r -= w
        if r <= 0:
            return shape
    return shapes[-1][0]


def _by_class(segs, cls):
    """Filtra pela classe harmônica. Segmentos neutros passam sempre."""
    return [s for s in segs if agrees(s, cls)]


def _fill(shape, rng, cls):
    out = []
    for slot in shape:
        if slot == "C":
            out.append(rng.choice(_by_class(NON_LARYNGEAL, cls)))
        elif slot == "R":
            out.append(rng.choice(SONORANTS))       # sonorantes são neutras
        elif slot == "H":
            out.append(rng.choice(_by_class(LARYNGEALS, cls)))
        elif slot == "s":
            out.append("s")
    return out


def _glottal_count(segs):
    return sum(1 for s in segs if is_glottalized(s))


def make_root(rng, long_vowel_chance=0.15, cls=None):
    """Gera uma raiz monossilábica no formato canônico.

    A raiz inteira pertence a uma classe harmônica: vogais e dorsais concordam.
    """
    cls = cls or rng.choice(["plain", "round"])
    for _ in range(80):
        onset = _fill(_pick(ONSET_SHAPES, rng), rng, cls)
        coda = _fill(_pick(CODA_SHAPES, rng), rng, cls)
        nucleus = rng.choice(_by_class(
            LONG_VOWELS if rng.random() < long_vowel_chance else VOWELS, cls))
        segs = onset + [nucleus] + coda
        if _glottal_count(segs) > 1:
            continue                      # dissimilação glotálica
        if len(onset) and len(coda) and onset[-1] == coda[0]:
            continue                      # evita eco trivial em torno do núcleo
        return segs
    return onset + [nucleus] + coda


def _bad_juncture(coda, onset):
    """Valida o encontro consonantal entre duas sílabas.

    Interna às palavras, a fonotática é mais apertada que nas bordas: o
    aglomerado medial resultante não passa de dois segmentos, e segmentos
    idênticos ou homorgânicos-idênticos não se encostam.
    """
    cluster = coda + onset
    if len(cluster) > 2:
        return True
    for a, b in zip(cluster, cluster[1:]):
        if a.rstrip("ː") == b.rstrip("ː"):     # *nnː, *tːt, *ss…
            return True
    return False


def make_word(rng, syllables=None, cls=None):
    """Gera uma palavra polissilábica, validando cada junção silábica.

    A harmonia vale para a palavra toda — é o mesmo domínio da raiz enquanto
    não houver morfologia derivacional para definir um domínio menor.
    """
    cls = cls or rng.choice(["plain", "round"])
    n = syllables or rng.choice([2, 2, 2, 3, 3, 4])
    syls = []
    for i in range(n):
        last = i == n - 1
        for _ in range(60):
            onset = _fill(_pick(ONSET_SHAPES, rng), rng, cls)
            if i > 0 and not onset:
                onset = _fill("C", rng, cls)        # evita hiato
            if rng.random() < 0.12:
                son = rng.choice(NASALS + LIQUIDS)
                nucleus = SYLLABIC[son.rstrip("ː")]  # núcleo sonorante
            else:
                nucleus = rng.choice(_by_class(
                    LONG_VOWELS if rng.random() < 0.12 else VOWELS, cls))
            # só a sílaba final carrega coda complexa
            coda = (_fill(_pick(CODA_SHAPES, rng), rng, cls) if last
                    else _fill(rng.choice(["", "", "", "R", "C"]), rng, cls))
            if i > 0 and _bad_juncture(syls[-1][2], onset):
                continue
            break
        syls.append((onset, [nucleus], coda))

    segs = [s for syl in syls for part in syl for s in part]
    if _glottal_count(segs) > 1:
        return make_word(rng, syllables, cls)
    return segs


def stress(segs, rng):
    """Acento livre: marca uma sílaba ao acaso. É livre, não fixo."""
    nuclei = [i for i, s in enumerate(segs)
              if s in VOWELS + LONG_VOWELS or s in SYLLABIC.values()]
    if not nuclei:
        return "".join(segs)
    k = rng.choice(nuclei)
    out = list(segs)
    j = k
    while j > 0 and out[j - 1] not in VOWELS + LONG_VOWELS \
            and out[j - 1] not in SYLLABIC.values():
        j -= 1
    out.insert(j, "ˈ")
    return "".join(out)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    n = int(args[0]) if args else 20
    seed = 4400                                   # AEC, por gosto
    if "--seed" in sys.argv:
        seed = int(sys.argv[sys.argv.index("--seed") + 1])
    rng = random.Random(seed)

    mode = "roots" if "--roots" in sys.argv else "words"
    print(f"# Proto-Orogeniano — {n} {mode} (seed {seed})\n")
    for _ in range(n):
        cls = rng.choice(["plain", "round"])
        segs = (make_root(rng, cls=cls) if mode == "roots"
                else make_word(rng, cls=cls))
        mark = "−" if cls == "plain" else "+"
        print(f"  [{mark}round]  /" + stress(segs, rng) + "/")


if __name__ == "__main__":
    main()
