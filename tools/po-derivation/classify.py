"""Classifica o corpus de formas flexionadas em termos do Proto-Orogeniano.

Para cada forma do PIE que inverta limpo, devolve:

| campo | o que é |
|---|---|
| `pie` | a forma do dataset, sem acento agudo |
| `lema`, `pos`, `tags` | de onde veio, e o que é gramaticalmente |
| `po` | a forma proto-orogeniana |
| `esqueleto` | as **classes naturais** do documento 03 §3: `C H R s V` |
| `silabas` | a divisão pelo molde do documento 02 §4.1 |
| `n_sil` | quantas sílabas |
| `acento` | índice da sílaba tônica, ou `-1` se o dataset não marca |
| `stem` | o esqueleto consonantal invariante do paradigma |
| `grau` | o que preenche o primeiro vão vocálico: `e`, `o` ou `zero` |

As classes vêm de `features.py`, não de uma reimplementação: é a mesma matriz
que o documento 03 verifica, então o esqueleto aqui e as classes naturais de
lá não podem divergir.

**O que `stem` é e não é.** É a subsequência consonantal comum a todas as
formas do lema. Para `*dóru` dá `ʔt r w` — que é raiz *mais* sufixo de tema
(`*der-u-`), não a raiz sozinha. Separar os dois exige morfologia, que é a
lição 5. O campo é honesto sobre isso: chama-se `stem`, não `raiz`.

Uso:
    python3 classify.py                    # resumo do corpus
    python3 classify.py --tsv saida.tsv.gz # a tabela inteira (.gz opcional)
    python3 classify.py --moldes           # onsets e codas medidos
    python3 classify.py --lema dóru        # um paradigma, legível

Sem dependências externas.
"""

import collections
import gzip
import os
import sys
import unicodedata

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "po-phonology"))

from theories import BASELINE                                     # noqa: E402
from invert import segment as pie_segment                         # noqa: E402
from stems import load_forms                                      # noqa: E402
from features import MATRIX, matches, NATURAL_CLASSES             # noqa: E402
from inventory import SYLLABIC                                    # noqa: E402
from syllabify import syllabify                                   # noqa: E402

ACUTE = "́"
SYLLABIC_SET = set(SYLLABIC.values())

# Os quatro rótulos da fonotática, resolvidos pela matriz de traços.
_CLASS_SPEC = [(n[0], s) for n, s in NATURAL_CLASSES.items() if n[0] in "CHRs"]


def natural_class(seg):
    """`C` `H` `R` `s` `V` — o rótulo do documento 02 §4 para este segmento."""
    if seg in SYLLABIC_SET or seg in ("i", "u"):
        return "V"
    f = MATRIX.get(seg)
    if f is None:
        return "?"
    if f.get("syll") == +1:
        return "V"
    for label, spec in _CLASS_SPEC:
        if matches(seg, spec):
            return label
    return "?"


def deacc(word):
    return unicodedata.normalize(
        "NFC", "".join(c for c in unicodedata.normalize("NFD", word)
                       if c != ACUTE))


def stress_index(word):
    """Índice do SEGMENTO acentuado na forma do PIE, ou -1."""
    d = unicodedata.normalize("NFD", word)
    k = -1
    seen = 0
    for c in d:
        if unicodedata.combining(c):
            if c == ACUTE:
                k = seen - 1
        else:
            seen += 1
    return k


def to_po(word):
    """Inverte para o Proto-Orogeniano. Devolve None se algum ponto falha."""
    out = []
    for s in pie_segment(word):
        t = BASELINE["map"].get(s)
        if t is None or (isinstance(t, str) and t.startswith("?")):
            return None
        out.append(t)
    return out or None


def _consonants(segs):
    return [s for s in segs if natural_class(s) != "V"]


def _lcs(a, b):
    """Maior subsequência comum — para achar o esqueleto invariante."""
    m = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            m[i][j] = (m[i + 1][j + 1] + 1 if a[i] == b[j]
                       else max(m[i + 1][j], m[i][j + 1]))
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            out.append(a[i]); i += 1; j += 1
        elif m[i + 1][j] >= m[i][j + 1]:
            i += 1
        else:
            j += 1
    return out


def grade(pie_segs):
    """O que preenche o primeiro vão vocálico da forma do PIE."""
    for s in pie_segs:
        if s in ("e", "ē"):
            return "e"
        if s in ("o", "ō"):
            return "o"
        if s in ("m̥", "n̥", "r̥", "l̥", "i", "u"):
            return "zero"
    return "—"


def build():
    """Constrói a tabela. Devolve (linhas, descartes por motivo)."""
    forms = load_forms()
    drop = collections.Counter()

    # passo 1: inverter, e agrupar por lema para achar o esqueleto invariante
    parsed = []
    by_lemma = collections.defaultdict(list)
    for e in forms:
        bare = deacc(e["form"])
        po = to_po(bare)
        if po is None:
            drop["sem correspondência no PO"] += 1
            continue
        parsed.append((e, bare, po))
        by_lemma[e["lemma"]].append(_consonants(po))

    stems = {}
    for lemma, cons in by_lemma.items():
        cur = cons[0]
        for c in cons[1:]:
            cur = _lcs(cur, c)
            if not cur:
                break
        stems[lemma] = cur

    rows = []
    for e, bare, po in parsed:
        syls = syllabify("".join(po))
        # O esqueleto é lido da forma JÁ SILABIFICADA, não dos segmentos crus:
        # em /ˈʔte.ru/ o `w` é núcleo `[u]`, e vale `V`, não `R`. Ler dos
        # segmentos daria `CVRR` para uma palavra que tem duas vogais.
        skel = "".join(natural_class(x)
                       for on, nu, cd in syls for x in on + nu + cd)
        k = stress_index(e["form"])
        acc = -1
        if k >= 0:
            n = 0
            for i, (on, nu, cd) in enumerate(syls):
                n += len(on) + len(nu) + len(cd)
                if k < n:
                    acc = i
                    break
        rows.append(dict(
            pie=bare, lema=e["lemma"], pos=e["pos"], tags="|".join(e["tags"]),
            po="".join(po), esqueleto=skel,
            silabas=".".join("".join(on + nu + cd) for on, nu, cd in syls),
            n_sil=len(syls), acento=acc,
            stem="".join(stems.get(e["lemma"], [])),
            grau=grade(pie_segment(bare)),
            # a estrutura vai junto: reconstruí-la a partir da string
            # re-segmentaria `l̩` como `l` + diacrítico solto
            _margens=[("".join(natural_class(x) for x in on),
                       "".join(natural_class(x) for x in cd))
                      for on, nu, cd in syls]))
    return rows, drop


COLS = ["pie", "lema", "pos", "tags", "po", "esqueleto", "silabas",
        "n_sil", "acento", "stem", "grau"]


def margins(rows):
    """Onsets e codas efetivamente atestados, em classes naturais."""
    on = collections.Counter()
    cd = collections.Counter()
    for r in rows:
        for o, c in r["_margens"]:
            on[o] += 1
            cd[c] += 1
    return on, cd


def main():
    rows, drop = build()

    if "--tsv" in sys.argv:
        path = sys.argv[sys.argv.index("--tsv") + 1]
        opener = gzip.open if path.endswith(".gz") else open
        with opener(path, "wt") as fh:
            fh.write("\t".join(COLS) + "\n")
            for r in rows:
                fh.write("\t".join(str(r[c]) for c in COLS) + "\n")
        print(f"{len(rows)} linhas -> {path}")
        return

    if "--lema" in sys.argv:
        alvo = sys.argv[sys.argv.index("--lema") + 1]
        sel = [r for r in rows if r["lema"] == alvo]
        if not sel:
            print(f"lema *{alvo} não encontrado")
            return
        print(f"*{alvo}   stem invariante: {sel[0]['stem']}\n")
        print(f"{'PIE':16s} {'Proto-Orogeniano':20s} {'esqueleto':12s} "
              f"{'grau':6s} {'ac':>3s}  tags")
        print("-" * 100)
        vistos = set()
        for r in sorted(sel, key=lambda x: x["tags"]):
            if r["po"] in vistos:
                continue
            vistos.add(r["po"])
            print(f"*{r['pie']:15s} /{r['silabas']:19s} {r['esqueleto']:12s} "
                  f"{r['grau']:6s} {r['acento']:3d}  {r['tags'][:34]}")
        return

    if "--moldes" in sys.argv:
        on, cd = margins(rows)
        tot_on, tot_cd = sum(on.values()), sum(cd.values())
        DECL_ON = {"", "s", "C", "R", "sC", "sR", "CR", "sCR",
                   "H", "HR", "sH"}
        DECL_CD = {"", "R", "C", "s", "RC", "Rs", "Cs", "RCs",
                   "H", "RH", "Hs"}
        print("ONSETS atestados (classes naturais do documento 03 §3)\n")
        print(f"{'molde':10s} {'n':>7s} {'%':>6s}   gerado pelo §4.1?")
        print("-" * 48)
        for k, v in on.most_common(16):
            ok = "sim" if k in DECL_ON else "**NÃO**"
            print(f"{k or '∅':10s} {v:7d} {100*v/tot_on:5.1f} %   {ok}")
        print("\nCODAS atestadas\n")
        print(f"{'molde':10s} {'n':>7s} {'%':>6s}   gerado pelo §4.1?")
        print("-" * 48)
        for k, v in cd.most_common(16):
            ok = "sim" if k in DECL_CD else "**NÃO**"
            print(f"{k or '∅':10s} {v:7d} {100*v/tot_cd:5.1f} %   {ok}")
        falta_on = sum(v for k, v in on.items() if k not in DECL_ON)
        falta_cd = sum(v for k, v in cd.items() if k not in DECL_CD)
        print(f"\nnão gerado pelo molde declarado: "
              f"{falta_on} onsets ({100*falta_on/tot_on:.1f} %), "
              f"{falta_cd} codas ({100*falta_cd/tot_cd:.1f} %)")
        return

    print(f"formas classificadas: {len(rows)}")
    for k, v in drop.most_common():
        print(f"   descartadas — {k}: {v}")
    print()
    print("por número de sílabas:",
          dict(sorted(collections.Counter(r["n_sil"] for r in rows).items())))
    print("por grau do 1º vão: ",
          dict(collections.Counter(r["grau"] for r in rows).most_common()))
    print("por classe:         ",
          dict(collections.Counter(r["pos"] for r in rows).most_common(6)))
    esq = collections.Counter(r["esqueleto"] for r in rows)
    print(f"\nesqueletos distintos: {len(esq)}")
    print("os 12 mais frequentes:")
    for k, v in esq.most_common(12):
        print(f"   {k:14s} {v:6d}")


if __name__ == "__main__":
    main()
