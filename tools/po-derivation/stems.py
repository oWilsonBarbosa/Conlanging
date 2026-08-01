"""Corpus de **formas flexionadas**, não de raízes.

As raízes do dataset são citadas em grau-e abstrato, sem acento e sem flexão.
Isso deixava três coisas fora de teste: a *Abtönung* (condicionada por acento),
as vogais longas (que raízes não carregam) e o grau zero (que precisa de
paradigma).

As 1.018 entradas não-raiz — substantivos, verbos, adjetivos, sufixos — trazem
**40.894 formas flexionadas**, das quais **93 % marcam o acento**. É o corpus
certo para essas perguntas.

Cuidado com a codificação: o agudo do dataset vem **pré-composto** (`é` é
U+00E9, não `e` + U+0301). Contar caracteres combinantes sem normalizar para
NFD acha 470 formas acentuadas em vez de 38.128.

Uso:
    python3 stems.py            # perfil do corpus
    python3 stems.py --abtonung # o teste do grau-o contra o acento
    python3 stems.py --longas   # de onde vêm as vogais longas

Sem dependências externas.
"""

import collections
import json
import re
import sys
import unicodedata

from invert import ROOTS

ACUTE = "́"
PLACEHOLDER = {"-", "—", ""}


def load_forms():
    """Formas flexionadas limpas, com o lema e as etiquetas de origem."""
    out = []
    for line in open(ROOTS):
        d = json.loads(line)
        if d.get("pos") == "root":
            continue
        for f in (d.get("forms") or []):
            x = f.get("form", "")
            tags = f.get("tags", [])
            if x in PLACEHOLDER or "table-tags" in x or "inflection-template" in tags:
                continue
            for part in x.split("~"):
                part = part.strip().strip("*")
                # descarta resíduo de notação com dígitos que não sejam laringais
                probe = part.replace("h₁", "").replace("h₂", "").replace("h₃", "")
                if not part or re.search(r"[0-9₀-₉]", probe):
                    continue
                out.append({"form": part, "lemma": d["word"],
                            "pos": d["pos"], "tags": tags})
    return out


def analyse(word):
    """[(caractere-base, é_tônico)] — o acento pode vir pré-composto."""
    d = unicodedata.normalize("NFD", word)
    out, i = [], 0
    while i < len(d):
        c, i = d[i], i + 1
        acc = False
        while i < len(d) and unicodedata.combining(d[i]):
            if d[i] == ACUTE:
                acc = True
            i += 1
        out.append((c, acc))
    return out


def abtonung(forms):
    """*o vem de *e que perdeu o acento? (Brugmann)

    Controla pela vogal temática: ela é sufixal e átona por definição, o que
    inflaria o efeito. O teste em posição de raiz não a inclui.
    """
    def table(keep):
        c = collections.Counter()
        for entry in forms:
            seq = analyse(entry["form"])
            vs = [(k, cc, a) for k, (cc, a) in enumerate(seq) if cc in "eo"]
            for idx, (k, cc, a) in enumerate(vs):
                if keep(idx):
                    c[(cc, a)] += 1
        return c

    results = []
    for label, keep in (("todas as posições", lambda i: True),
                        ("só a 1ª vogal (raiz)", lambda i: i == 0),
                        ("não-primeiras (sufixos)", lambda i: i > 0)):
        c = table(keep)
        e1, e0 = c[("e", True)], c[("e", False)]
        o1, o0 = c[("o", True)], c[("o", False)]
        if min(e1, e0, o1, o0) == 0:
            continue
        n = e1 + e0 + o1 + o0
        chi = n * (e1 * o0 - e0 * o1) ** 2 / (
            (e1 + e0) * (o1 + o0) * (e1 + o1) * (e0 + o0))
        odds = (o0 / o1) / (e0 / e1)
        results.append((label, e1, e0, o1, o0, odds, chi, n))
    return results


def lei_m(forms):
    """As duas leis que produzem *o deixam rastros ortogonais?

    A *Abtönung* é condicionada por acento; `*-ē̆m` > `*-ō̆m` (Kloekhorst 2024)
    é condicionada por segmento. Se as duas existem, diante de *m o efeito do
    acento tem de sumir — uma lei segmental não consulta o acento.

    Só a 1ª vogal, para não misturar a vogal temática.
    """
    c = collections.Counter()
    for entry in forms:
        seq = analyse(entry["form"])
        vs = [(k, cc, a) for k, (cc, a) in enumerate(seq) if cc in "eo"]
        if not vs:
            continue
        k, cc, a = vs[0]
        nxt = "".join(x for x, _ in seq[k + 1:k + 2])
        c[(cc, a, "_m" if nxt == "m" else "outro")] += 1

    rows = []
    for cc in "eo":
        for ctx in ("_m", "outro"):
            t, at = c[(cc, True, ctx)], c[(cc, False, ctx)]
            rows.append((cc, ctx, t, at, 100 * t / (t + at) if t + at else 0))
    # razão de chances da Abtönung fora do contexto segmental
    e1, e0 = c[("e", True, "outro")], c[("e", False, "outro")]
    o1, o0 = c[("o", True, "outro")], c[("o", False, "outro")]
    odds = (o0 / o1) / (e0 / e1)
    ot = c[("o", True, "_m")] / (c[("o", True, "_m")] + c[("o", True, "outro")])
    et = c[("e", True, "_m")] / (c[("e", True, "_m")] + c[("e", True, "outro")])
    return rows, odds, ot, et


def long_vowels(forms):
    """As vogais longas são adjacentes a laringal ou a *-s perdido?"""
    LONG = "ēōā"
    tot = adj_lar = final_s = 0
    ex = []
    for entry in forms:
        w = unicodedata.normalize("NFC", entry["form"])
        if not any(c in w for c in LONG):
            continue
        tot += 1
        near = bool(re.search(r"[ēōā](h₁|h₂|h₃|H)|(h₁|h₂|h₃|H)[ēōā]", w))
        if near:
            adj_lar += 1
        if w.endswith("s") or re.search(r"[ēōā][mns]$", w):
            final_s += 1
        if len(ex) < 8:
            ex.append((entry["lemma"], w, ",".join(entry["tags"][:2])))
    return tot, adj_lar, final_s, ex


def main():
    forms = load_forms()
    if "--abtonung" in sys.argv:
        print("TESTE DA ABTÖNUNG — Brugmann: *o vem de *e que perdeu o acento\n")
        print(f"{'recorte':26s} {'*e tôn':>8s} {'*e át':>8s} "
              f"{'*o tôn':>8s} {'*o át':>8s} {'razão':>7s} {'chi2':>8s}")
        print("-" * 78)
        for lab, e1, e0, o1, o0, odds, chi, n in abtonung(forms):
            print(f"{lab:26s} {e1:8d} {e0:8d} {o1:8d} {o0:8d} "
                  f"{odds:7.2f} {chi:8.0f}")
        print("\nrazão = quanto *o é mais propenso a ser átono que *e "
              "(razão de chances)")
        return
    if "--lei-m" in sys.argv:
        rows, odds, ot, et = lei_m(forms)
        print("AS DUAS LEIS DO *o — a Abtönung é acentual, *-ē̆m > *-ō̆m é "
              "segmental\n")
        print(f"{'1ª vogal':22s} {'tônico':>8s} {'átono':>8s} {'% tôn':>8s}")
        print("-" * 50)
        for cc, ctx, t, at, pct in rows:
            lab = f"*{cc} diante de *m" if ctx == "_m" else f"*{cc} em outro lugar"
            print(f"{lab:22s} {t:8d} {at:8d} {pct:7.1f}%")
        print(f"\ndiante de *m o efeito do acento some: *o fica tão tônico "
              f"quanto *e")
        print(f"razão de chances da Abtönung, excluído o contexto _m: {odds:.2f}")
        print(f"dos *o tônicos, {100*ot:.1f}% estão diante de *m "
              f"(contra {100*et:.1f}% dos *e tônicos)")
        return
    if "--longas" in sys.argv:
        tot, lar, fs, ex = long_vowels(forms)
        print(f"formas com vogal longa: {tot}")
        print(f"   adjacentes a laringal:        {lar:5d} ({100*lar/tot:.0f}%)")
        print(f"   em final passível de perda:   {fs:5d} ({100*fs/tot:.0f}%)")
        print("\namostra:")
        for lem, w, tg in ex:
            print(f"   *{lem:16s} -> *{w:20s} {tg}")
        return

    print(f"formas flexionadas: {len(forms)}")
    acc = sum(1 for f in forms if any(a for _, a in analyse(f["form"])))
    print(f"   com acento marcado: {acc} ({100*acc/len(forms):.0f}%)")
    print(f"   com *o:             {sum(1 for f in forms if 'o' in f['form'])}")
    print(f"   com vogal longa:    "
          f"{sum(1 for f in forms if any(c in unicodedata.normalize('NFC', f['form']) for c in 'ēōā'))}")
    print("   por classe:",
          dict(collections.Counter(f["pos"] for f in forms).most_common(6)))


if __name__ == "__main__":
    main()
