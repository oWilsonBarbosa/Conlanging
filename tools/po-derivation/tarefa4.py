"""Tarefa 4 da lição Phonology 4.

> *"Take ten random words from your conlang and try to make ten random sound
> changes **before applying them**. What do you see? Are all words affected
> equally much? Does it happen to merge grammatically distinct forms?"*

O "before applying them" é a regra do exercício, e é ela que o torna honesto:
as mudanças não podem ser escolhidas depois de ver as palavras, senão o
resultado é decorativo. Aqui isso é imposto pela construção — as dez mudanças
saem de um catálogo por sorteio com semente, numa função que **não recebe as
palavras**. Trocar a semente troca as mudanças, não o corpus.

As três perguntas do enunciado precisam de coisas diferentes:

- *what do you see* / *affected equally* — palavras geradas por `gen.py`
  servem, porque só interessa a forma.
- *merge grammatically distinct forms* — precisa de **paradigma**, que a
  conlang ainda não tem (morfologia é a lição 5). A saída: inverter para o
  Proto-Orogeniano as formas flexionadas reais do corpus (`stems.py`) e
  aplicar as mudanças sobre os paradigmas resultantes. Formas gramaticalmente
  distintas de verdade, com etiqueta.

Uso:
    python3 tarefa4.py              # o experimento completo
    python3 tarefa4.py --seed 7     # outro sorteio de mudanças
    python3 tarefa4.py --regras     # só as dez mudanças sorteadas

Sem dependências externas.
"""

import collections
import os
import random
import sys
import unicodedata

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "po-phonology"))

from theories import BASELINE                                    # noqa: E402
from invert import segment                                       # noqa: E402
from stems import load_forms                                     # noqa: E402
from inventory import (OBSTRUENTS, SONORANTS, SIBILANTS, VOWELS,  # noqa: E402
                       FORTIS, LENIS, GLOTTALIZED, is_glottalized)
import gen                                                       # noqa: E402

ACUTE = "́"
LARYNGEALS = ["qː", "qʷː", "q", "ʔq", "qʷ", "ʔqʷ"]
STOPS = [o for o in OBSTRUENTS if o not in LARYNGEALS]
FORT = [v for v in FORTIS.values() if v]
LEN = [v for v in LENIS.values() if v]
GLOT = [v for v in GLOTTALIZED.values() if v]
NASAL = ["m", "mː", "n", "nː"]
LIQUID = ["r", "rː", "l", "lː"]
GLIDE = ["w", "j"]

# Vozeamento: o Proto-Orogeniano não contrasta voz, mas uma mudança sonora
# pode fonemizar a alofonia de 4.4. Os alvos existem só como saída.
VOICED = {"p": "b", "t": "d", "ḱ": "ɟ", "k": "ɡ", "kʷ": "ɡʷ",
          "q": "ɢ", "qʷ": "ɢʷ"}
FRIC = {"pː": "ɸ", "tː": "θ", "ḱː": "ç", "kː": "x", "kʷː": "xʷ",
        "qː": "χ", "qʷː": "χʷ", "p": "ɸ", "t": "θ", "k": "x"}


def is_vowel(s):
    return s in VOWELS or s in ("i", "u") or s in gen.SYLLABIC.values()


# ─── O catálogo de mudanças ─────────────────────────────────────────────────
# Cada entrada: (rótulo, categoria da lição, função sobre a lista de segmentos).
# A função recebe (segs, stress_idx) e devolve a lista nova.

def _map_env(segs, targets, out, env):
    """Aplica `out` a cada segmento de `targets` cujo ambiente satisfaz `env`."""
    new = []
    for i, s in enumerate(segs):
        prev = segs[i - 1] if i else "#"
        nxt = segs[i + 1] if i + 1 < len(segs) else "#"
        if s in targets and env(prev, nxt, i, segs):
            r = out(s) if callable(out) else out
            if r is not None:
                new.append(r)
        else:
            new.append(s)
    return new


def _intervoc(prev, nxt, i, segs):
    return is_vowel(prev) and is_vowel(nxt)


def _final(prev, nxt, i, segs):
    return nxt == "#"


def _initial(prev, nxt, i, segs):
    return prev == "#"


CATALOGUE = [
    ("lenição · degeminação intervocálica: fortis > lenis / V_V",
     "lenição",
     lambda s, st: _map_env(s, FORT, lambda x: x.rstrip("ː"), _intervoc)),

    ("lenição · espirantização: oclusiva > fricativa / V_V",
     "lenição",
     lambda s, st: _map_env(s, list(FRIC), lambda x: FRIC[x], _intervoc)),

    ("lenição · sonorização: lenis > sonora / V_V",
     "lenição",
     lambda s, st: _map_env(s, list(VOICED), lambda x: VOICED[x], _intervoc)),

    ("lenição · debucalização: oclusiva > ʔ / _#",
     "lenição",
     lambda s, st: _map_env(s, STOPS, "ʔ", _final)),

    ("perda · apócope: V > ∅ / _#",
     "perda",
     lambda s, st: _map_env(s, list(VOWELS), None, _final)),

    ("perda · síncope: V > ∅ em sílaba átona entre consoantes",
     "perda",
     lambda s, st: [x for i, x in enumerate(s)
                    if not (is_vowel(x) and i != st and 0 < i < len(s) - 1
                            and not is_vowel(s[i - 1])
                            and not is_vowel(s[i + 1]))]),

    ("perda · redução de aglomerado: CC > C / _#",
     "perda",
     lambda s, st: (s[:-2] + s[-1:]
                    if len(s) > 2 and not is_vowel(s[-1])
                    and not is_vowel(s[-2]) else s)),

    ("perda · degeminação final: Cː > C / _#",
     "perda",
     lambda s, st: s[:-1] + [s[-1].rstrip("ː")] if s else s),

    ("perda · queda de laringal com alongamento compensatório: H > ∅ / V_",
     "fusão",
     lambda s, st: _lar_loss(s)),

    ("adição · epêntese: ∅ > e entre duas consoantes finais",
     "epêntese",
     lambda s, st: _epenthesis(s)),

    ("adição · prótese: ∅ > e / #_CC",
     "epêntese",
     lambda s, st: (["e"] + s if len(s) > 1 and not is_vowel(s[0])
                    and not is_vowel(s[1]) else s)),

    ("fortição: lenis > fortis / #_",
     "fortição",
     lambda s, st: _map_env(s, LEN, lambda x: x + "ː", _initial)),

    ("fortição · desglotalização: ʔC > C / _#",
     "fortição",
     lambda s, st: _map_env(s, GLOT, lambda x: x[1:], _final)),

    ("assimilação regressiva: nasal toma o ponto da oclusiva seguinte",
     "assimilação",
     lambda s, st: _nasal_place(s)),

    ("assimilação · palatalização: k kː > ḱ ḱː / _{j, i}",
     "assimilação",
     lambda s, st: _map_env(s, ["k", "kː"], lambda x: "ḱ" + x[1:],
                            lambda p, n, i, g: n in ("j", "i"))),

    ("assimilação · coloração laringal: e > o / _{qʷ, qʷː, ʔqʷ}",
     "assimilação",
     lambda s, st: _map_env(s, ["e"], "o",
                            lambda p, n, i, g: n in ("qʷ", "qʷː", "ʔqʷ"))),

    ("metátese: sC > Cs em onset inicial",
     "metátese",
     lambda s, st: ([s[1], s[0]] + s[2:]
                    if len(s) > 2 and s[0] == "s"
                    and not is_vowel(s[1]) else s)),

    ("rotacismo: s > r / V_V",
     "rotacismo",
     lambda s, st: _map_env(s, ["s", "sː"], "r", _intervoc)),

    ("vocalização: j w > i u entre consoantes",
     "lenição",
     lambda s, st: _map_env(s, GLIDE, lambda x: "i" if x == "j" else "u",
                            lambda p, n, i, g: not is_vowel(p) and p != "#")),

    ("fusão · coalescência: sonorante silábica + V > V",
     "fusão",
     lambda s, st: [x for x in s if x not in gen.SYLLABIC.values()]
     if any(is_vowel(x) and x in VOWELS for x in s) else s),
]


def _lar_loss(segs):
    out = []
    for i, s in enumerate(segs):
        if s in LARYNGEALS and i and is_vowel(segs[i - 1]):
            if out and not out[-1].endswith("ː"):
                out[-1] = out[-1] + "ː"          # alongamento compensatório
            continue
        out.append(s)
    return out


def _epenthesis(segs):
    if len(segs) > 1 and not is_vowel(segs[-1]) and not is_vowel(segs[-2]):
        return segs[:-1] + ["e"] + segs[-1:]
    return segs


_PLACE_OF = {"p": "m", "pː": "m", "t": "n", "tː": "n", "ʔt": "n",
             "ḱ": "ɲ", "ḱː": "ɲ", "ʔḱ": "ɲ", "k": "ŋ", "kː": "ŋ", "ʔk": "ŋ",
             "kʷ": "ŋ", "kʷː": "ŋ", "ʔkʷ": "ŋ",
             "q": "ɴ", "qː": "ɴ", "qʷ": "ɴ", "qʷː": "ɴ"}


def _nasal_place(segs):
    out = list(segs)
    for i, s in enumerate(out[:-1]):
        if s.rstrip("ː") in ("m", "n") and out[i + 1] in _PLACE_OF:
            out[i] = _PLACE_OF[out[i + 1]] + ("ː" if s.endswith("ː") else "")
    return out


def draw_changes(seed, n=10):
    """Sorteia n mudanças do catálogo. NÃO recebe as palavras — de propósito."""
    rng = random.Random(seed)
    return rng.sample(CATALOGUE, n)


def apply_all(segs, stress, changes):
    """Aplica as mudanças em ordem. Devolve (forma final, quantas pegaram)."""
    cur, hits = list(segs), 0
    for _, _, fn in changes:
        before = list(cur)
        try:
            cur = fn(cur, stress)
        except Exception:
            cur = before
        if cur != before:
            hits += 1
    return cur, hits


# ─── Corpus ─────────────────────────────────────────────────────────────────

def po_words(n, seed=4400):
    """n palavras do gerador do Proto-Orogeniano, com o índice do acento."""
    rng = random.Random(seed)
    out = []
    while len(out) < n:
        segs = gen.make_word(rng)
        nuclei = [i for i, s in enumerate(segs) if is_vowel(s)]
        if not nuclei:
            continue
        out.append((segs, rng.choice(nuclei)))     # acento livre (§3.5)
    return out


CORPUS_SEED = 4400          # fixo de propósito — ver a nota em `main`


def po_paradigms(n_lemmas=6, seed=CORPUS_SEED):
    """Paradigmas reais invertidos para o Proto-Orogeniano.

    A conlang ainda não tem morfologia (lição 5), então as formas
    gramaticalmente distintas vêm do corpus do PIE, invertidas segmento a
    segmento pela tabela de correspondências do baseline.
    """
    theory = BASELINE
    by_lemma = collections.defaultdict(dict)
    for e in load_forms():
        tags = tuple(t for t in e["tags"] if t not in ("error-unrecognized-form",))
        if not tags:
            continue
        d = unicodedata.normalize("NFD", e["form"])
        bare = "".join(c for c in d if c != ACUTE)
        stress = 0
        seen = 0
        for i, c in enumerate(unicodedata.normalize("NFD", e["form"])):
            if unicodedata.combining(c):
                if c == ACUTE:
                    stress = seen - 1
            else:
                seen += 1
        segs, ok = [], True
        for s in segment(unicodedata.normalize("NFC", bare)):
            # `None` é a lacuna /ʔp/: *b não tem origem no Proto-Orogeniano.
            # A forma inteira é descartada, não remendada.
            if theory["map"].get(s) is None:
                ok = False
                break
            segs.append(theory["map"][s])
        if ok and segs:
            by_lemma[e["lemma"]][", ".join(tags)] = (segs, max(stress, 0))

    rich = [(l, d) for l, d in by_lemma.items() if len(d) >= 6]
    rich.sort(key=lambda x: -len(x[1]))
    rng = random.Random(seed)
    return rng.sample(rich, min(n_lemmas, len(rich)))


# ─── Relatório ──────────────────────────────────────────────────────────────

def show(segs):
    return "/" + "".join(segs) + "/"


def cost_each(n_lemmas=6):
    """Cada mudança do catálogo aplicada SOZINHA: quantas distinções custa?

    O sorteio de dez responde *se* funde; isto responde *o quê* funde, e é o
    que explica a variância entre sementes.
    """
    paradigms = po_paradigms(n_lemmas, CORPUS_SEED)
    base = 0
    for _, forms in paradigms:
        base += len({"".join(s) for s, _ in forms.values()})
    rows = []
    for label, cat, fn in CATALOGUE:
        after = 0
        for _, forms in paradigms:
            after += len({"".join(apply_all(s, st, [(label, cat, fn)])[0])
                          for s, st in forms.values()})
        rows.append((base - after, cat, label))
    rows.sort(key=lambda r: -r[0])
    return base, rows


def main():
    seed = 4400
    if "--seed" in sys.argv:
        seed = int(sys.argv[sys.argv.index("--seed") + 1])

    if "--custo" in sys.argv:
        n = 6
        if "--lemas" in sys.argv:
            n = int(sys.argv[sys.argv.index("--lemas") + 1])
        base, rows = cost_each(n)
        print("CUSTO DE CADA MUDANÇA, APLICADA SOZINHA")
        print(f"sobre {n} paradigmas: {base} formas distintas\n")
        print(f"{'perdas':>7s}  {'categoria':13s} mudança")
        print("-" * 78)
        for lost, cat, label in rows:
            mark = " ←" if lost else ""
            print(f"{lost:7d}  {cat:13s} {label}{mark}")
        return

    changes = draw_changes(seed)

    print(f"AS DEZ MUDANÇAS (sorteadas com semente {seed}, antes de qualquer "
          f"palavra)\n")
    for i, (label, cat, _) in enumerate(changes, 1):
        print(f"{i:2d}. [{cat:12s}] {label}")

    if "--regras" in sys.argv:
        return

    # ── pergunta 1 e 2: o que se vê, e todas são afetadas igualmente? ──
    print("\n" + "=" * 78)
    print("DEZ PALAVRAS DA CONLANG\n")
    words = po_words(10, seed)
    print(f"{'antes':30s} {'depois':30s} {'regras':>7s}")
    print("-" * 72)
    rows = []
    for segs, st in words:
        out, hits = apply_all(segs, st, changes)
        rows.append((segs, out, hits))
        print(f"{show(segs):30s} {show(out):30s} {hits:5d}/10")

    hits = [h for _, _, h in rows]
    print(f"\nregras que pegaram: mín {min(hits)}, máx {max(hits)}, "
          f"média {sum(hits)/len(hits):.1f}")
    survived = sum(1 for a, b, _ in rows if a == b)
    print(f"palavras intactas: {survived}/10")
    dl = [abs(len(b) - len(a)) for a, b, _ in rows]
    print(f"variação de comprimento: média {sum(dl)/len(dl):.1f} segmentos, "
          f"máx {max(dl)}")

    # ── pergunta 3: funde formas gramaticalmente distintas? ──
    print("\n" + "=" * 78)
    print("FUNDE FORMAS GRAMATICALMENTE DISTINTAS?\n")
    print("Paradigmas reais do corpus, invertidos para o Proto-Orogeniano.\n")

    tot_forms = tot_before = tot_after = 0
    detail = []
    # O corpus de paradigmas NÃO varia com a semente: se as mudanças e as
    # palavras mudassem juntas, não daria para saber qual das duas moveu o
    # número. Mesma disciplina de §1 — variar uma dimensão por vez.
    for lemma, forms in po_paradigms(6, CORPUS_SEED):
        before, after = {}, {}
        for tags, (segs, st) in forms.items():
            before.setdefault("".join(segs), []).append(tags)
            out, _ = apply_all(segs, st, changes)
            after.setdefault("".join(out), []).append(tags)
        # fusão NOVA: etiquetas que estavam em grupos distintos antes e caíram
        # no mesmo grupo depois. Grupos já idênticos na inversão não contam.
        where = {t: k for k, ts in before.items() for t in ts}
        fresh = []
        for form, tags in after.items():
            origins = {where[t] for t in tags}
            if len(origins) > 1:
                fresh.append((form, tags, origins))
        tot_forms += len(forms)
        tot_before += len(before)
        tot_after += len(after)
        detail.append((lemma, len(forms), len(before), len(after), fresh))

    print(f"{'lema':22s} {'formas':>7s} {'após inversão':>14s} "
          f"{'após mudanças':>14s} {'fusões novas':>13s}")
    print("-" * 76)
    for lemma, nf, nb, na, fresh in detail:
        print(f"*{lemma:21s} {nf:7d} {nb:14d} {na:14d} {len(fresh):13d}")
    print("-" * 76)
    print(f"{'TOTAL':22s} {tot_forms:7d} {tot_before:14d} {tot_after:14d} "
          f"{sum(len(f) for _, _, _, _, f in detail):13d}")

    print(f"\nA inversão sozinha já custa {tot_forms - tot_before} distinções "
          f"({100*(tot_forms-tot_before)/tot_forms:.0f} % das {tot_forms} "
          f"formas) — antes de qualquer mudança sonora.")
    print(f"As dez mudanças custam mais {tot_before - tot_after}.")

    print("\nexemplos de fusão NOVA — distintas na inversão, idênticas depois:")
    shown = 0
    for lemma, _, _, _, fresh in detail:
        for form, tags, _ in fresh:
            if shown < 6:
                print(f"   *{lemma:16s} /{form}/")
                print(f"   {'':16s}  <- " + "  |  ".join(t for t in tags[:3]))
                shown += 1


if __name__ == "__main__":
    main()
