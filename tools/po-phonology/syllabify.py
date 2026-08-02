"""Divisão silábica do Proto-Orogeniano, pelo molde do documento 02 §4.

```
onset  (s)(C)(R)     máx. 3
núcleo  V | R̩
coda   (R)(C)(s)     máx. 3
```

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


def kind(seg):
    if seg in VOWELS:
        return "V"
    if seg in SYLLABIC.values() or seg in ("i", "u"):
        return "V"
    if seg in SIBILANTS:
        return "s"
    if seg in SONORANTS:
        return "R"
    if seg in OBSTRUENTS:
        return "C"
    return "?"


def legal_onset(segs):
    """(s)(C)(R), máx. 3."""
    if len(segs) > 3:
        return False
    pat = "".join(kind(s) for s in segs)
    return pat in ("", "s", "C", "R", "sC", "sR", "CR", "sCR", "CC", "RR")


def legal_coda(segs):
    """(R)(C)(s), máx. 3."""
    if len(segs) > 3:
        return False
    pat = "".join(kind(s) for s in segs)
    return pat in ("", "R", "C", "s", "RC", "Rs", "Cs", "RCs", "CC")


# Escala de sonoridade para decidir QUAL sonorante vira núcleo. Glides são as
# mais sonoras, e é por isso que /w/ e /j/ vocalizam antes de /r l/ ou /m n/ —
# a regra 4.2 do documento 03. Sem isso, `/ʔterw/` (< *dóru) sairia
# `[ˈʔte]σ[r̩w]σ` em vez do correto `[ˈʔte]σ[ru]σ`.
SONORITY = {"w": 3, "j": 3, "r": 2, "l": 2, "m": 1, "n": 1}


def _promote(segs, run):
    """Índice da sonorante mais sonora de `run` (lista de índices)."""
    cands = [i for i in run if kind(segs[i]) == "R"]
    if not cands:
        return None
    return max(cands, key=lambda i: (SONORITY.get(segs[i].rstrip("ː"), 0), -i))


def nuclei(segs):
    """Índices dos núcleos.

    Toda vogal é núcleo. Uma sonorante vira núcleo quando o material à sua
    volta não cabe num onset ou numa coda legal — é a regra 4.1 do documento
    03, e aqui ela é *forçada pelo molde*, não estipulada.
    """
    ix = sorted(i for i, s in enumerate(segs) if kind(s) == "V")
    if not ix:
        i = _promote(segs, range(len(segs)))
        return [i] if i is not None else []

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
            j = _promote(segs, run)
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
            j = _promote(segs, tail)
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
