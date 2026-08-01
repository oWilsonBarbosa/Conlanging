"""Aplica a derivação Proto-Orogeniano → PIE clássico, em ordem, e testa se a
ordem importa.

A lição avisa: *"the order may be important!"*. Aqui isso é medido em vez de
afirmado. O teste central: a cadeia de arraste de Kloekhorst exige que o
**vozeamento preceda a degeminação**. Se a ordem se inverter, `/tː/` degemina
para `/t/` antes que `/t/` tenha vozeado, os dois se fundem, e o contraste
triplo vira duplo.

Uso:
    python3 derive.py            # deriva e compara as duas ordens
    python3 derive.py --sample   # mostra derivações passo a passo

Sem dependências externas.
"""

import collections
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from invert import load_roots, invert, segment                    # noqa: E402
from theories import BASELINE                                     # noqa: E402

# ─── Correspondências das regras ────────────────────────────────────────────
FORTIS = {"pː": "p", "tː": "t", "ḱː": "ḱ", "kː": "k", "kʷː": "kʷ"}
GLOT = {"ʔt": "d", "ʔḱ": "ǵ", "ʔk": "g", "ʔkʷ": "gʷ"}
LENIS = {"p": "bʰ", "t": "dʰ", "ḱ": "ǵʰ", "k": "gʰ", "kʷ": "gʷʰ"}
NONFORTIS_UVULAR = {"q": "h₁", "ʔq": "h₁", "qʷ": "h₁", "ʔqʷ": "h₁"}
FORTIS_UVULAR = {"qː": "h₂", "qʷː": "h₃"}
LONG_SON = {"sː": "s", "mː": "m", "nː": "n", "rː": "r", "lː": "l"}


def _map(table):
    def rule(form):
        return [table.get(s, s) for s in form]
    return rule


# nome, categoria na taxonomia da lição, função
U1 = ("U1 debucalização das uvulares não-fortis",
      "lenição / abertura (debucalização)", _map(NONFORTIS_UVULAR))
K1 = ("K1 vozeamento de lenis e glotalizadas",
      "lenição / sonorização", _map({**GLOT, **LENIS}))
K2 = ("K2 degeminação das oclusivas fortis",
      "lenição / abertura", _map(FORTIS))
K3 = ("K3 espirantização das uvulares fortis",
      "lenição / abertura (espirantização)", _map(FORTIS_UVULAR))
K4 = ("K4 degeminação de sibilante e sonorantes",
      "lenição / abertura — com FUSÃO", _map(LONG_SON))

ORDER_OK = [U1, K1, K2, K4, K3]        # vozeamento antes da degeminação
ORDER_BAD = [U1, K2, K1, K4, K3]       # degeminação antes do vozeamento


def apply_all(form, order, trace=False):
    steps = []
    for name, cat, fn in order:
        before = list(form)
        form = fn(form)
        if trace and form != before:
            steps.append((name, "".join(before), "".join(form)))
    return form, steps


def po_forms(roots):
    """Formas proto-orogenianas legais, obtidas por inversão."""
    out = []
    for w in roots:
        form, _ = invert(w, BASELINE)
        if any(s is None for s in form):
            continue
        if any(isinstance(s, str) and s.startswith("?") for s in form):
            continue
        out.append((w, form))
    return out


def measure(pairs, order):
    seen = collections.defaultdict(set)
    for w, form in pairs:
        out, _ = apply_all(list(form), order)
        seen["".join(out)].add("".join(form))
    merged = {k: v for k, v in seen.items() if len(v) > 1}
    lost = sum(len(v) - 1 for v in merged.values())
    return len(seen), merged, lost


def main():
    roots = load_roots()
    pairs = po_forms(roots)
    print(f"raízes distintas: {len(roots)}")
    print(f"formas proto-orogenianas utilizáveis: {len(pairs)}"
          f"   (excluídas as ambíguas e as sem correspondência)\n")

    if "--sample" in sys.argv:
        print("=== derivações passo a passo (ordem correta) ===")
        for w, form in pairs[:6]:
            out, steps = apply_all(list(form), ORDER_OK, trace=True)
            print(f"\n  PO /{''.join(form)}/   ->   PIE *{''.join(out)}-"
                  f"      (alvo: *{w}-)")
            for name, a, b in steps:
                print(f"      {name:44s} {a} > {b}")
        return

    print(f"{'ordem':44s} {'saídas':>8s} {'fusões':>8s} {'formas perdidas':>16s}")
    print("-" * 80)
    for label, order in (("vozeamento ANTES da degeminação", ORDER_OK),
                         ("degeminação ANTES do vozeamento", ORDER_BAD)):
        n, merged, lost = measure(pairs, order)
        print(f"{label:44s} {n:8d} {len(merged):8d} {lost:16d}")

    n_ok, m_ok, _ = measure(pairs, ORDER_OK)
    n_bad, m_bad, _ = measure(pairs, ORDER_BAD)
    print(f"\ndiferença: {n_ok - n_bad} contrastes a mais na ordem correta")
    print("\nexemplos de fusão causada pela ordem errada:")
    for out, ins in list(m_bad.items())[:6]:
        if out not in m_ok:
            print(f"   *{out:18s} <-  {', '.join('/' + i + '/' for i in sorted(ins))}")


if __name__ == "__main__":
    main()
