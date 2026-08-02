"""Inverte as 873 raízes do PIE para o Proto-Orogeniano e mede o resultado.

## Por que isto não é circular

Como o Proto-Orogeniano é *definido* pelas correspondências com o PIE, aplicar
as regras para a frente devolveria o PIE de volta por construção, e um "índice
de acerto" seria 100 % sem significar nada.

O que se pode medir de verdade é outra coisa:

1. **Ambiguidade** — quantos segmentos do PIE têm mais de uma origem possível
   no Proto-Orogeniano. Cada um é um ponto onde a derivação não é invertível
   e precisa de condicionamento.
2. **Legalidade** — as formas proto-orogenianas resultantes obedecem à
   fonotática do documento 02 §4? Uma teoria que produz formas ilegais está
   errada em algum lugar. **É este o teste que discrimina.**
3. **Colisão** — quantas raízes distintas do PIE colapsam na mesma forma
   proto-orogeniana. É a pergunta 4 do exercício da lição: *"does it merge
   grammatically distinct forms?"*

Uso:
    python3 invert.py            # todas as teorias, resumo comparativo
    python3 invert.py baseline   # uma teoria, com exemplos

Sem dependências externas.
"""

import collections
import json
import re
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "po-phonology"))
from theories import VARIANTS                                    # noqa: E402
from inventory import OBSTRUENTS, SONORANTS, SIBILANTS, is_glottalized  # noqa: E402

ROOTS = os.path.join(os.path.dirname(__file__), "..", "..", "..",
                     "PIE_roots", "kaikki.org-dictionary-ProtoIndoEuropean.jsonl")

# unidades do dataset, mais longas primeiro
UNITS = ["gʷʰ", "kʷ", "gʷ", "bʰ", "dʰ", "ǵʰ", "gʰ", "h₁", "h₂", "h₃",
         "ḱ", "ǵ", "ē", "ō", "H",
         "m̥", "n̥", "r̥", "l̥"]          # sonorantes silábicas (anel combinante)

NOISE = "()⁽⁾-"                            # resíduo de notação do dataset


def segment(word):
    word = "".join(c for c in word if c not in NOISE)
    out, i = [], 0
    while i < len(word):
        for u in UNITS:
            if word.startswith(u, i):
                out.append(u); i += len(u); break
        else:
            out.append(word[i]); i += 1
    return out


def load_roots():
    """Raízes DISTINTAS. O dataset repete a mesma grafia para homógrafos
    (*wer- aparece três vezes); contá-los como colisão seria contar o
    dataset, não a derivação."""
    seen = []
    for line in open(ROOTS):
        d = json.loads(line)
        if d.get("pos") == "root":
            seen.append(re.sub(r"[()]", "", d["word"].strip("*-")))
    return sorted(set(seen))


# ─── Fonotática do documento 02 §4, como validador ──────────────────────────
SONORITY = {"stop": 0, "sib": 1, "son": 2, "vow": 3}
_LAR = {"qː", "qʷː", "q", "ʔq", "qʷ", "ʔqʷ", "ʔ"}


def kind(seg):
    if seg in ("e", "eː", "o", "oː"):
        return "vow"
    if seg in SONORANTS:
        return "son"
    if seg in SIBILANTS:
        return "sib"
    return "stop"


def check(form):
    """Devolve a lista de violações da fonotática."""
    bad = []
    if any(s is None for s in form):
        return ["segmento sem correspondência"]
    if sum(1 for s in form if is_glottalized(s)) > 1:
        bad.append("duas glotalizadas")
    if "ʔp" in form:
        bad.append("/ʔp/ inexistente")
    nuclei = [i for i, s in enumerate(form) if kind(s) in ("vow", "son")]
    if not nuclei:
        bad.append("sem núcleo possível")
    # margens: no máximo 3 segmentos antes do primeiro núcleo e depois do último
    if nuclei:
        if nuclei[0] > 3:
            bad.append(f"onset de {nuclei[0]}")
        tail = len(form) - nuclei[-1] - 1
        if tail > 3:
            bad.append(f"coda de {tail}")
    return bad


def invert(word, theory):
    out, unknown = [], []
    for seg in segment(word):
        if seg in theory["map"]:
            out.append(theory["map"][seg])
        else:
            unknown.append(seg); out.append(seg)
    return out, unknown


# Segmentos do PIE com mais de uma origem possível no Proto-Orogeniano.
# Duas fontes distintas, e a segunda ficou de fora da primeira contagem:
#   - laringal: *h₁ vem de qualquer uvular não-fortis (4 opções); *H é
#     indeterminado na própria filologia;
#   - sonorante e sibilante: a regra K4 degemina, então */l/ e */lː/ dão ambos
#     *l. Vale para *s *m *n *r *l e para as silábicas.
AMBIG_LAR = {"h₁", "H"}
AMBIG_SON = {"s", "m", "n", "r", "l", "m̥", "n̥", "r̥", "l̥"}


def ambiguity(roots):
    """Quantas raízes têm ponto não-invertível, por origem."""
    lar = son = both = 0
    for w in roots:
        segs = segment(w)
        a = any(s in AMBIG_LAR for s in segs)
        b = any(s in AMBIG_SON for s in segs)
        lar += a
        son += b
        both += (a or b)
    return dict(lar=lar, son=son, total=both, n=len(roots))


def run(theory, roots, verbose=False):
    amb = collections.Counter()
    unknown = collections.Counter()
    viol = collections.Counter()
    forms = collections.defaultdict(list)
    illegal = []
    for w in roots:
        form, unk = invert(w, theory)
        unknown.update(unk)
        for s in form:
            if isinstance(s, str) and s.startswith("?"):
                amb[s] += 1
        bad = check(form)
        if bad:
            viol.update(bad)
            illegal.append((w, "".join(str(s) for s in form), bad))
        forms["".join(str(s) for s in form)].append(w)
    collisions = {k: v for k, v in forms.items() if len(v) > 1}
    return dict(amb=amb, unknown=unknown, viol=viol, illegal=illegal,
                collisions=collisions, nforms=len(forms))


def main():
    roots = load_roots()
    only = sys.argv[1] if len(sys.argv) > 1 else None
    if "--ambiguidade" in sys.argv:
        a = ambiguity(roots)
        n = a["n"]
        print(f"raízes: {n}\n")
        print("pontos onde a inversão escolhe sem evidência:\n")
        print(f"  laringal (*h₁, *H)            {a['lar']:4d}  "
              f"({100*a['lar']/n:2.0f} %)   custo da coluna uvular")
        print(f"  sonorante ou *s (via K4)      {a['son']:4d}  "
              f"({100*a['son']/n:2.0f} %)   pago por toda teoria")
        print(f"  {'com algum ponto ambíguo':28s}{a['total']:4d}  "
              f"({100*a['total']/n:2.0f} %)")
        return
    print(f"raízes: {len(roots)}\n")
    print(f"{'teoria':18s} {'ilegais':>8s} {'colisões':>9s} "
          f"{'sem corresp.':>13s}   nota")
    print("-" * 92)
    detail = None
    for t in VARIANTS:
        if only and t["name"] != only:
            continue
        r = run(t, roots)
        nunk = sum(r["unknown"].values())
        print(f"{t['name']:18s} {len(r['illegal']):8d} {len(r['collisions']):9d} "
              f"{nunk:13d}   {t['note']}")
        if only:
            detail = (t, r)
    if detail:
        t, r = detail
        print(f"\n=== {t['name']} — detalhe ===")
        print("violações:", dict(r["viol"]))
        print("segmentos sem correspondência:", dict(r["unknown"]))
        print("ambíguos:", dict(r["amb"]))
        print("\nprimeiras formas ilegais:")
        for w, f, b in r["illegal"][:8]:
            print(f"   *{w:16s} -> /{f}/   {b}")
        print("\nprimeiras colisões:")
        for f, ws in list(r["collisions"].items())[:8]:
            print(f"   /{f}/  <-  {', '.join('*' + w for w in ws)}")


if __name__ == "__main__":
    main()
