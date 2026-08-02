"""Divisão silábica do Proto-Orogeniano, pelo molde do documento 02 §4.

```
onset  (s)(C)(R)     máx. 3
núcleo  V | R̩
coda   (R)(C)(s)     máx. 3
```

Duas camadas, como o §4.1 e o §4.2 do documento:

1. o **molde nuclear** acima, que é do morfema;
2. `/s/` e `H` como **apêndices extrassilábicos** na borda externa da margem —
   à esquerda no onset, à direita na coda.

O Princípio do Onset Máximo (M.O.P.) governa, **com a ressalva** de que só se
aplica quando o onset resultante for legal — uma coda que suba em sonoridade
não é coda, e força a sonorante a virar núcleo.

Como a língua tem uma vogal só (§3.4), a silabificação faz trabalho pesado:
`/seqːl/` não é uma sílaba com coda `qːl` — a sonoridade subiria. É
`[ˈse]σ[qːl̩]σ`, com `/l/` silábico.

Uso:
    python3 syllabify.py seqːl weʔtr sqːles
    python3 syllabify.py --doc          # os exemplos do documento 02 §6

Sem dependências externas.
"""

import sys

from features import MATRIX
from inventory import (OBSTRUENTS, SONORANTS, SIBILANTS, VOWELS, SYLLABIC,
                       PHONEMES)

UNITS = sorted(PHONEMES, key=len, reverse=True)
SYLL_OF = dict(SYLLABIC)


def segment(word):
    """Quebra uma transcrição em segmentos do inventário."""
    out, i = [], 0
    word = word.replace("ˈ", "").replace(".", "")
    while i < len(word):
        for u in UNITS:
            if word.startswith(u, i):
                out.append(u)
                i += len(u)
                break
        else:
            out.append(word[i])
            i += 1
    return out


# A coluna uvular é uma classe à parte na fonotática (documento 02 §4.2): ela
# é `[+low]`, a única obstruinte que é, e é extrassilábica como o `/s/`. Sem
# separá-la de `C`, este módulo não conseguia enunciar a regra e precisava de
# uma lista de moldes escrita à mão.
LARYNGEALS = {"qː", "qʷː", "q", "ʔq", "qʷ", "ʔqʷ"}


def kind(seg):
    if seg in VOWELS:
        return "V"
    if seg in SYLLABIC.values() or seg in ("i", "u"):
        return "V"
    if seg in SIBILANTS:
        return "s"
    if seg in SONORANTS:
        return "R"
    if seg in LARYNGEALS:
        return "H"
    if seg in OBSTRUENTS:
        return "C"
    return "?"


def _core(pat, template):
    """`pat` cabe no molde nuclear, com `H` valendo como `C`?"""
    return pat.replace("H", "C") in template


# Molde nuclear do documento 02 §4.1, expandido: (s)(C)(R) e (R)(C)(s).
CORE_ON = {"", "s", "C", "R", "sC", "sR", "CR", "sCR"}
CORE_CD = {"", "R", "C", "s", "RC", "Rs", "Cs", "RCs"}


def legal_margin(pat, core, left):
    """Molde nuclear, ou molde nuclear depois de retirar o apêndice.

    `H` é extrassilábico como o `/s/` (§4.2), e com a **mesma geometria**:
    ancora na borda externa — à esquerda no onset, à direita na coda. Retirar
    `H` de dentro da margem não vale, e não pode valer: a coda `HR` de
    `/seqːl/` sobe em sonoridade e continua ilegal, que é o que força o `/l/`
    a ser núcleo.
    """
    if _core(pat, core):
        return True
    while pat and pat[0 if left else -1] == "H":
        pat = pat[1:] if left else pat[:-1]
        if _core(pat, core):
            return True
    return False


def legal_onset(segs):
    """(s)(C)(R), máx. 3 — mais o apêndice extrassilábico à esquerda."""
    if len(segs) > 3:
        return False
    return legal_margin("".join(kind(s) for s in segs), CORE_ON, left=True)


def legal_coda(segs):
    """(R)(C)(s), máx. 3 — mais o apêndice extrassilábico à direita."""
    if len(segs) > 3:
        return False
    return legal_margin("".join(kind(s) for s in segs), CORE_CD, left=False)


def sonority(seg):
    """Sonoridade, **derivada dos traços** — não uma escala escrita à mão.

    Ewen & van der Hulst (§2.6, §3.3) definem a escala pelos mesmos traços que
    a matriz do documento 03 já tem:

        *"the higher the sonority of a segment, the closer it is to the peak of
        the syllable"*
        *"[+continuant] segments are higher on the sonority hierarchy than
        [−continuant]"*

    Com `[±cons]` e `[±cont]`, a ordem cai sozinha:

        /w j/  [−cons +cont]  3     glides
        /r l/  [+cons +cont]  1     líquidas
        /m n/  [+cons −cont]  0     nasais

    É essa ordem que faz `/ʔterw/` (< *dóru) dar `[ˈʔte]σ[ru]σ` e não
    `[ˈʔte]σ[r̩w]σ` — e, por consequência, é por isso que o PIE tem *dóru e
    não **dór̥w.
    """
    f = MATRIX.get(seg.rstrip("ː"))
    if f is None:
        return 0
    return (2 if f.get("cons") == -1 else 0) + (1 if f.get("cont") == +1 else 0)


def _promote(segs, run, nucs=()):
    """Índice da sonorante que vira núcleo, dentre as de `run`.

    Critério primário: **sonoridade** — `/w j/` antes de `/r l/` antes de
    `/m n/`. É o que faz `/ʔterw/` (< *dóru) dar `[ˈʔte]σ[ru]σ`.

    Desempate: a **mais distante** de um núcleo já existente. Com dois glides
    lado a lado, o que sobrevive é o mais afastado — `/ʔtrewj/` (< *drewi) dá
    `[ˈʔtrew]σ[i]σ`, e não `[ˈʔtre]σ[uj]σ`.
    """
    cands = [i for i in run if kind(segs[i]) == "R"]
    if not cands:
        return None

    def dist(i):
        return min((abs(i - n) for n in nucs), default=0)

    return max(cands, key=lambda i: (sonority(segs[i]), dist(i), -i))


def nuclei(segs):
    """Índices dos núcleos.

    Toda vogal é núcleo. Uma sonorante vira núcleo quando o material à sua
    volta não cabe num onset ou numa coda legal — é a regra 4.1 do documento
    03, e aqui ela é *forçada pelo molde*, não estipulada.
    """
    ix = sorted(i for i, s in enumerate(segs) if kind(s) == "V")
    if not ix:
        # Palavra sem vogal plena: a mais sonora abre a primeira sílaba, e daí
        # o refinamento abaixo trata as margens como em qualquer outra palavra.
        # Devolver só esse índice deixava passar coda ilegal — `/ʔtrwmjs/`
        # saía como uma sílaba com coda `RRs`.
        i = _promote(segs, range(len(segs)), ())
        if i is None:
            return []
        ix = [i]

    for _ in range(len(segs)):            # itera até estabilizar
        changed = False
        # o material antes de cada núcleo tem de caber num onset legal
        for k, n in enumerate(ix):
            start = ix[k - 1] + 1 if k else 0
            run = list(range(start, n))
            if k:
                # parte vira coda da sílaba anterior, parte vira onset desta
                if any(legal_coda([segs[i] for i in run[:c]])
                       and legal_onset([segs[i] for i in run[c:]])
                       for c in range(len(run) + 1)):
                    continue
            elif legal_onset([segs[i] for i in run]):
                continue
            j = _promote(segs, run, ix)
            if j is not None and j not in ix:
                ix.append(j)
                ix.sort()
                changed = True
                break
        if changed:
            continue
        # e o material depois do último núcleo, numa coda legal
        tail = list(range(ix[-1] + 1, len(segs)))
        if not legal_coda([segs[i] for i in tail]):
            j = _promote(segs, tail, ix)
            if j is not None and j not in ix:
                ix.append(j)
                ix.sort()
                continue
        break
    return ix


def syllabify(word):
    """Devolve a lista de sílabas, cada uma (onset, núcleo, coda)."""
    segs = segment(word)
    ix = nuclei(segs)
    if not ix:
        return [([], segs, [])]
    out = []
    for k, n in enumerate(ix):
        prev = ix[k - 1] if k else -1
        start = prev + 1 if k else 0
        between = segs[start:n] if k == 0 else segs[prev + 1:n]
        if k == 0:
            onset, coda_prev = between, []
        else:
            # M.O.P.: dá ao onset o máximo que for legal, o resto vira coda
            onset, coda_prev = [], list(between)
            for cut in range(len(between) + 1):
                cand_on = between[cut:]
                cand_cd = between[:cut]
                if legal_onset(cand_on) and legal_coda(cand_cd):
                    onset, coda_prev = cand_on, cand_cd
                    break
            out[-1] = (out[-1][0], out[-1][1], coda_prev)
        nuc = [segs[n]]
        if kind(segs[n]) == "R":
            nuc = [SYLL_OF.get(segs[n].rstrip("ː"), segs[n])]
        out.append((onset, nuc, []))
    tail = segs[ix[-1] + 1:]
    out[-1] = (out[-1][0], out[-1][1], tail)
    return out


def show(word, stress=0):
    """`[ˈse]σ[qːl̩]σ` — com o acento na sílaba pedida."""
    parts = []
    for i, (on, nu, cd) in enumerate(syllabify(word)):
        mark = "ˈ" if i == stress else ""
        parts.append("[" + mark + "".join(on + nu + cd) + "]σ")
    return "".join(parts)


def flat(word, stress=0):
    """`/ˈse.qːl̩/` — a forma linear, com ponto silábico."""
    syls = syllabify(word)
    out = []
    for i, (on, nu, cd) in enumerate(syls):
        out.append(("ˈ" if i == stress else "") + "".join(on + nu + cd))
    return "/" + ".".join(out) + "/"


DOC = [("seqːl", 0), ("sqːel", 0), ("sqːles", 0), ("weʔtr", 0),
       ("weʔtnej", 0), ("ʔterw", 0), ("ʔtrews", 0), ("ʔtrwmes", 0),
       ("pːeʔts", 0), ("jekʷːr", 0), ("qːner", 0), ("wʔtnes", 1)]


def main():
    if "--doc" in sys.argv:
        print(f"{'forma':16s} {'sílabas':30s} linear")
        print("-" * 74)
        for w, st in DOC:
            print(f"{w:16s} {show(w, st):30s} {flat(w, st)}")
        return
    for w in sys.argv[1:]:
        if w.startswith("--"):
            continue
        print(f"{w:16s} {show(w):30s} {flat(w)}")


if __name__ == "__main__":
    main()
