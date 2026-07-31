"""Inventário fonêmico do Proto-Orogeniano.

Fonte das restrições: docs/01_PROTO_INDO_ANATOLIAN.md §9.
Toda escolha aqui ou é forçada pelo alvo (o sistema que precisa alimentar o
proto-indo-hitita) ou está justificada em docs/02_PROTO_OROGENIAN_PHONOLOGY.md.

Sem dependências externas.
"""

# ─── Obstruintes: 3 séries × 7 pontos de articulação ────────────────────────
#
# O contraste é de AJUSTE LARÍNGEO, não de vozeamento:
#   fortis      = longa/geminada        /Cː/
#   glotalizada = breve pré-glotalizada /ʔC/
#   lenis       = breve simples         /C/
#
# A lacuna em /ʔp/ é sistemática, não acidental: o membro labial é o que
# tipicamente falta em sistemas glotálicos. É a origem da quase-ausência de
# *b no PIE (5 raízes em 873).

PLACES = ["labial", "dental", "palatal", "velar", "labiovelar",
          "uvular", "labiouvular"]

FORTIS = {
    "labial": "pː", "dental": "tː", "palatal": "ḱː", "velar": "kː",
    "labiovelar": "kʷː", "uvular": "qː", "labiouvular": "qʷː",
}
GLOTTALIZED = {
    "labial": None,                      # ← lacuna sistemática
    "dental": "ʔt", "palatal": "ʔḱ", "velar": "ʔk",
    "labiovelar": "ʔkʷ", "uvular": "ʔq", "labiouvular": "ʔqʷ",
}
LENIS = {
    "labial": "p", "dental": "t", "palatal": "ḱ", "velar": "k",
    "labiovelar": "kʷ", "uvular": "q", "labiouvular": "qʷ",
}

SERIES = {"fortis": FORTIS, "glottalized": GLOTTALIZED, "lenis": LENIS}

OBSTRUENTS = [s for serie in SERIES.values() for s in serie.values() if s]

# ─── Sibilante: participa do contraste de duração ───────────────────────────
# /sː/ é exigido por PIH *h₁éssi > hit. /ʔésːi/ vs. PIE clássico *h₁ési.
SIBILANTS = ["s", "sː"]

# ─── Sonorantes: também participam do contraste de duração ──────────────────
# /mː/ é exigido pelo item 21 da lista: *h₁mm- > cl.PIE *h₁m-.
NASALS = ["m", "mː", "n", "nː"]
LIQUIDS = ["r", "rː", "l", "lː"]
GLIDES = ["w", "j"]
SONORANTS = NASALS + LIQUIDS + GLIDES

# Sonorantes silábicas — núcleos alternativos.
# [i] e [u] são os alofones silábicos de /j/ e /w/: é daí que vêm *i e *u do PIE.
SYLLABIC = {"m": "m̩", "n": "n̩", "r": "r̩", "l": "l̩", "w": "u", "j": "i"}

# ─── Vogais ─────────────────────────────────────────────────────────────────
# Sistema de duas qualidades. Restrição dura: NÃO existe /a/
# (Lubotsky 1989, Pronk 2019 — consequência última da teoria laringal).
VOWELS = ["e", "o"]
LONG_VOWELS = ["eː", "oː"]

PHONEMES = OBSTRUENTS + SIBILANTS + SONORANTS + VOWELS + LONG_VOWELS


def series_of(seg):
    """Retorna 'fortis' | 'glottalized' | 'lenis' | None."""
    for name, table in SERIES.items():
        if seg in table.values():
            return name
    return None


def is_glottalized(seg):
    return series_of(seg) == "glottalized"


if __name__ == "__main__":
    print(f"obstruintes  {len(OBSTRUENTS):3d}  {' '.join(OBSTRUENTS)}")
    print(f"sibilantes   {len(SIBILANTS):3d}  {' '.join(SIBILANTS)}")
    print(f"sonorantes   {len(SONORANTS):3d}  {' '.join(SONORANTS)}")
    print(f"vogais       {len(VOWELS + LONG_VOWELS):3d}  "
          f"{' '.join(VOWELS + LONG_VOWELS)}")
    print(f"TOTAL        {len(PHONEMES):3d}")
