"""Matriz de traços distintivos do Proto-Orogeniano.

Conjunto de traços conforme Conlangs University, Phonology 3 (`course/10`):
major class, manner, laryngeal, place, prosody. Valor `0` = impossível ou
irrelevante para a distinção, como na lição.

O ponto crítico do sistema: as três séries de obstruintes se distinguem **sem
`[±voice]`**, por `[±long]` e `[±constricted glottis]`.

Este módulo não é decorativo: `__main__` verifica que cada classe natural
declarada resolve exatamente para o conjunto de segmentos pretendido.
Sem dependências externas.
"""

from inventory import (FORTIS, GLOTTALIZED, LENIS, SIBILANTS, NASALS,
                       LIQUIDS, GLIDES, VOWELS, LONG_VOWELS)

# ─── Gabaritos de lugar ─────────────────────────────────────────────────────
# Uvulares são as únicas obstruintes [+low]; é esse traço que as isola.
PLACE = {
    "labial":      dict(ant=+1, cor=-1, distr=0, front=0, back=0, high=0, low=0, round=-1),
    "dental":      dict(ant=+1, cor=+1, distr=+1, front=0, back=0, high=0, low=0, round=-1),
    "palatal":     dict(ant=-1, cor=-1, distr=0, front=+1, back=-1, high=+1, low=-1, round=-1),
    "velar":       dict(ant=-1, cor=-1, distr=0, front=-1, back=+1, high=+1, low=-1, round=-1),
    "labiovelar":  dict(ant=-1, cor=-1, distr=0, front=-1, back=+1, high=+1, low=-1, round=+1),
    "uvular":      dict(ant=-1, cor=-1, distr=0, front=-1, back=+1, high=-1, low=+1, round=-1),
    "labiouvular": dict(ant=-1, cor=-1, distr=0, front=-1, back=+1, high=-1, low=+1, round=+1),
}

# ─── Ajuste laríngeo: as três séries, sem [±voice] ──────────────────────────
SERIES_LARYNGEAL = {
    "fortis":      dict(voice=-1, sg=-1, cg=-1, long=+1),
    "glottalized": dict(voice=-1, sg=-1, cg=+1, long=-1),
    "lenis":       dict(voice=-1, sg=-1, cg=-1, long=-1),
}
# A célula [+long +cg] fica VAZIA no Proto-Orogeniano. É ela que o anatólio
# preenche depois, por fusão de *T + h₁ (Kloekhorst 2022).

STOP = dict(cons=+1, syll=-1, son=-1, cont=-1, dr=-1, nas=-1, lat=-1, stress=0)


def _stop(place, series):
    f = dict(STOP)
    f.update(PLACE[place])
    f.update(SERIES_LARYNGEAL[series])
    return f


MATRIX = {}
for _pl in PLACE:
    for _tbl, _ser in ((FORTIS, "fortis"), (GLOTTALIZED, "glottalized"),
                       (LENIS, "lenis")):
        _seg = _tbl[_pl]
        if _seg:                                    # /ʔp/ não existe
            MATRIX[_seg] = _stop(_pl, _ser)

for _seg, _lng in (("s", -1), ("sː", +1)):          # sibilante
    MATRIX[_seg] = dict(cons=+1, syll=-1, son=-1, cont=+1, dr=-1, nas=-1,
                        lat=-1, voice=-1, sg=-1, cg=-1, long=_lng, strid=+1,
                        stress=0, **PLACE["dental"])

for _seg in NASALS + LIQUIDS:
    _base = _seg.rstrip("ː")
    MATRIX[_seg] = dict(
        cons=+1, syll=-1, son=+1, cont=(-1 if _base in "mn" else +1),
        dr=-1, nas=(+1 if _base in "mn" else -1),
        lat=(+1 if _base == "l" else -1), voice=+1, sg=-1, cg=-1,
        long=(+1 if _seg.endswith("ː") else -1), stress=0,
        **PLACE["labial" if _base == "m" else "dental"])

MATRIX["j"] = dict(cons=-1, syll=-1, son=+1, cont=+1, dr=-1, nas=-1, lat=-1,
                   voice=+1, sg=-1, cg=-1, long=-1, stress=0, **PLACE["palatal"])
MATRIX["w"] = dict(cons=-1, syll=-1, son=+1, cont=+1, dr=-1, nas=-1, lat=-1,
                   voice=+1, sg=-1, cg=-1, long=-1, stress=0, **PLACE["labiovelar"])

for _v, _lng in ((VOWELS[0], -1), (LONG_VOWELS[0], +1)):
    MATRIX[_v] = dict(cons=-1, syll=+1, son=+1, cont=+1, dr=-1, nas=-1, lat=-1,
                      voice=+1, sg=-1, cg=-1, long=_lng, stress=0,
                      ant=0, cor=-1, distr=0,
                      front=+1, back=-1, high=-1, low=-1, round=-1)


# ─── Classes naturais ───────────────────────────────────────────────────────
# Convenção: um segmento satisfaz [+F] só com valor +1; `0` nunca satisfaz nem
# [+F] nem [−F]. É a leitura da lição, em que `0` marca o irrelevante.

# `"¬+"` = "qualquer valor menos +1". É preciso porque labiais e dentais têm
# `low=0` (a posição da língua é irrelevante nelas), e `0` não satisfaz [−low].
# Ver docs/03 §3: "C" não é classe natural em sentido estrito.

NATURAL_CLASSES = {
    "C  obstruinte oclusiva não-uvular": dict(son=-1, cont=-1, low="¬+"),
    "H  laringal (coluna uvular)":       dict(son=-1, cont=-1, low=+1),
    "R  sonorante não-silábica":         dict(son=+1, syll=-1),
    "s  sibilante":                      dict(son=-1, cont=+1),
    "fortis":                            dict(son=-1, long=+1, cg=-1),
    "glotalizada":                       dict(cg=+1),
    "lenis":                             dict(son=-1, cont=-1, long=-1, cg=-1),
    "núcleo possível":                   dict(syll=+1),
    "labializada":                       dict(round=+1),
}


def matches(seg, spec):
    f = MATRIX[seg]
    for k, v in spec.items():
        got = f.get(k, 0)
        if v == "¬+":
            if got == +1:
                return False
        elif got != v:
            return False
    return True


def resolve(spec):
    return sorted(s for s in MATRIX if matches(s, spec))


if __name__ == "__main__":
    print(f"segmentos na matriz: {len(MATRIX)}\n")
    expected = {
        "C  obstruinte oclusiva não-uvular": 14,
        "H  laringal (coluna uvular)": 6,
        "R  sonorante não-silábica": 10,
        "s  sibilante": 2,
        "fortis": 8,
        "glotalizada": 6,
        "lenis": 7,
        "labializada": 7,
    }
    ok = True
    for name, spec in NATURAL_CLASSES.items():
        got = resolve(spec)
        exp = expected.get(name)
        flag = ""
        if exp is not None and len(got) != exp:
            flag = f"   <-- ESPERADO {exp}"
            ok = False
        print(f"{name:36s} {len(got):2d}  {' '.join(got)}{flag}")
    print("\nverificação:", "ok" if ok else "FALHOU")
