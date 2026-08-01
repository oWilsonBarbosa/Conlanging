"""Teorias rivais como configuração, não como forks de código.

Cada teoria é um conjunto de correspondências PIE ↔ Proto-Orogeniano. O
`BASELINE` é o sistema dos documentos 02 e 03; as variantes diferem dele em
**exatamente uma** dimensão, para que a comparação isole a variável.

Ver docs/04 §1 para por que só quatro das cinco apostas são teorias rivais.
"""

# ─── Séries de oclusivas ────────────────────────────────────────────────────
# Chave: grafia da raiz no dataset. Valor: segmento proto-orogeniano.

_STOPS_LENGTH = {                      # duração (Kloekhorst 2016) — baseline
    "p": "pː", "t": "tː", "ḱ": "ḱː", "k": "kː", "kʷ": "kʷː",
    "b": None, "d": "ʔt", "ǵ": "ʔḱ", "g": "ʔk", "gʷ": "ʔkʷ",
    "bʰ": "p", "dʰ": "t", "ǵʰ": "ḱ", "gʰ": "k", "gʷʰ": "kʷ",
}
_STOPS_VOICE = {                       # voz (Simon 2020; manuais)
    "p": "p", "t": "t", "ḱ": "ḱ", "k": "k", "kʷ": "kʷ",
    "b": "b", "d": "d", "ǵ": "ǵ", "g": "g", "gʷ": "gʷ",
    "bʰ": "bʰ", "dʰ": "dʰ", "ǵʰ": "ǵʰ", "gʰ": "gʰ", "gʷʰ": "gʷʰ",
}
_STOPS_ASPIR = {                       # aspiração (Patri 2009, 2019)
    "p": "pʰ", "t": "tʰ", "ḱ": "ḱʰ", "k": "kʰ", "kʷ": "kʷʰ",
    "b": None, "d": "ˀt", "ǵ": "ˀḱ", "g": "ˀk", "gʷ": "ˀkʷ",
    "bʰ": "b", "dʰ": "d", "ǵʰ": "ǵ", "gʰ": "g", "gʷʰ": "gʷ",
}

# ─── Laringais ──────────────────────────────────────────────────────────────
_LAR_FULL = {"h₂": "qː", "h₃": "qʷː", "h₁": "q", "H": "?H"}   # coluna completa
_LAR_MIN = {"h₂": "qː", "h₃": "qʷː", "h₁": "ʔ", "H": "?H"}    # *h₁ herdado

# ─── Vogais ─────────────────────────────────────────────────────────────────
# A duração vocálica NÃO é invertida: o Proto-Orogeniano não a contrasta
# (docs/04 §8.3), e toda vogal longa do PIE é derivada depois — por contração
# em fronteira de morfema, perda de laringal ou Lei de Szemerényi. As entradas
# `ē`/`ō` existem só por completude; nenhuma das 766 raízes as exerce.
# As duas variantes diferem em exatamente uma dimensão: a QUALIDADE.
_VOW_ONE = {"e": "e", "o": "e", "ē": "e", "ō": "e"}            # uma qualidade
_VOW_TWO = {"e": "e", "o": "o", "ē": "e", "ō": "o"}            # duas

_SON = {"m": "m", "n": "n", "r": "r", "l": "l", "w": "w", "y": "j",
        "i": "j", "u": "w", "s": "s",
        # as silábicas do PIE são o resultado da regra 4.1 do documento 03,
        # não segmentos próprios: desfazem-se na sonorante correspondente
        "m̥": "m", "n̥": "n", "r̥": "r", "l̥": "l"}


def _theory(stops, lar, vow, name, note):
    m = {}
    m.update(stops); m.update(lar); m.update(vow); m.update(_SON)
    return {"name": name, "note": note, "map": m}


BASELINE = _theory(_STOPS_LENGTH, _LAR_FULL, _VOW_ONE, "baseline",
                   "duração · coluna uvular completa · uma vogal")

VARIANTS = [
    BASELINE,
    _theory(_STOPS_VOICE, _LAR_FULL, _VOW_ONE, "voz",
            "contraste por voz (Simon 2020) — o resto igual"),
    _theory(_STOPS_ASPIR, _LAR_FULL, _VOW_ONE, "aspiração",
            "contraste por aspiração (Patri) — o resto igual"),
    _theory(_STOPS_LENGTH, _LAR_MIN, _VOW_ONE, "laringal mínima",
            "*h₁ herdado como /ʔ/, sem coluna uvular completa"),
    _theory(_STOPS_LENGTH, _LAR_FULL, _VOW_TWO, "duas vogais",
            "/e o/ fonêmicos, sem derivar *o por regra"),
]
