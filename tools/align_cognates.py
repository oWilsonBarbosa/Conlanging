#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
align_cognates.py — primeira-passada *automática* do método comparativo
(ver data/cognate-method.md), sem dependências externas (só stdlib).

Para cada família de data/fire-by-family.md (na ORDEM em que aparecem):
  1. normaliza cada forma em CLASSES DE SOM (esquema Dolgopolsky simplificado);
  2. particiona a família em CONJUNTOS DE COGNATOS (clustering single-linkage
     sobre o esqueleto consonantal — significado != cognato);
  3. ALINHA cada conjunto (alinhamento múltiplo progressivo);
  4. extrai a TABELA DE CORRESPONDÊNCIAS e um TEMPLATE de consenso por coluna.

Saída: data/cognate-alignments.md  (+ resumo no stdout).
Uso:   python3 tools/align_cognates.py [filtro_de_família]
       (o filtro é um substring case-insensitive; sem ele, roda todas.)

AVISO: é uma heurística de triagem. As formas das listas são romanizações
(não IPA limpo), então o passo 1 aproxima. A cognação e a reconstrução finais
continuam sendo julgamento informado — isto só propõe os conjuntos e os alinha.
"""
import sys, os, re, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, "data", "fire-by-family.md")
OUT  = os.path.join(ROOT, "data", "cognate-alignments.md")

# ----------------------------------------------------------------------------
# 1. Classes de som (Dolgopolsky simplificado). V = vogal; '?' = desconhecido.
#    P labial obstr. | M nasal labial | W glide labial | T dental/alv. oclus.
#    S sibilante/africada | K velar/uvular/glotal | N nasal não-labial
#    R líquida | J glide palatal | V vogal
# ----------------------------------------------------------------------------
SINGLE = {}
def _put(chars, cls):
    for c in chars: SINGLE[c] = cls
_put("aeiouyàáâãäåèéêëìíîïòóôõöùúûüœøæɐəɛɔɨɪʊʌɘɵ", "V")
_put("pbfvɸβ",       "P")
_put("m",            "M")
_put("w",            "W")
_put("tdθð",         "T")
_put("szʃʒɕʑçʐʂ",    "S")
_put("kgcxɣqɢhħʁχ",  "K")   # 'c' romanizado = /k/ (foc, fuoco, focus)
_put("nŋɲɳ",         "N")
_put("rlɾʀɽʎɭ",      "R")
_put("j",            "J")
# dígrafos (testados antes dos caracteres simples)
DIGRAPHS = {
    "ph":"P","bh":"P","th":"T","dh":"T","kh":"K","gh":"K",
    "ch":"S","sh":"S","zh":"S","ts":"S","dz":"S","tʃ":"S","dʒ":"S",
    "ng":"N","ny":"N","gn":"N","ll":"R","rr":"R",
}
# modificadores a descartar (ejetivos, aspiração, comprimento, tom, cliques…)
DROP = set("ʼʰʷˀːˑ'ˈ`´ʲˠⁿ()[]ǃǀǁǂ.,/")

def normalize(form):
    """Pega a 1ª variante, decompõe, remove diacríticos/modificadores, minúscula."""
    form = form.strip()
    # 1ª variante antes de vírgula/ponto-e-vírgula/parêntese
    form = re.split(r"[,;(]", form)[0].strip()
    form = unicodedata.normalize("NFD", form)
    out = []
    for ch in form:
        if unicodedata.category(ch) == "Mn":   # marca combinante
            continue
        if ch in DROP or ch == " ":
            continue
        out.append(ch.lower())
    return "".join(out)

def tokenize(form):
    s = normalize(form)
    toks, i = [], 0
    while i < len(s):
        two = s[i:i+2]
        if two in DIGRAPHS:
            toks.append((two, DIGRAPHS[two])); i += 2
        else:
            ch = s[i]; toks.append((ch, SINGLE.get(ch, "?"))); i += 1
    return toks                          # lista de (grafema, classe)

def classes(toks):  return [c for _, c in toks]
def skeleton(toks): return [c for _, c in toks if c not in ("V", "?")]

# ----------------------------------------------------------------------------
# 2. Clustering de cognatos: single-linkage sobre o esqueleto consonantal.
# ----------------------------------------------------------------------------
def lev(a, b):
    if a == b: return 0
    if not a: return len(b)
    if not b: return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[-1] + 1, prev[j-1] + (ca != cb)))
        prev = cur
    return prev[-1]

def cognate(t1, t2, thr=0.5):
    s1, s2 = skeleton(t1), skeleton(t2)
    if not s1 or not s2:
        return s1 == s2
    if s1[0] != s2[0]:                       # 1ª consoante diferente => não cognato
        return False
    if len(s1) >= 2 and len(s2) >= 2 and s1[1] != s2[1]:
        return False                         # critério Dolgopolsky: 2 primeiras consoantes
    return lev(s1, s2) / max(len(s1), len(s2)) <= thr

def cluster(items):
    """complete-linkage guloso: um item só entra num conjunto se for cognato com
    TODOS os membros (evita o 'chaining' do single-linkage). Semeia pelos
    esqueletos mais longos (formas mais informativas primeiro)."""
    order = sorted(range(len(items)), key=lambda i: -len(skeleton(items[i][3])))
    clusters = []                        # cada cluster: lista de índices
    for i in order:
        for cl in clusters:
            if all(cognate(items[i][3], items[j][3]) for j in cl):
                cl.append(i); break
        else:
            clusters.append([i])
    groups = [[items[i] for i in cl] for cl in clusters]
    return sorted(groups, key=lambda g: (-len(g), items.index(g[0])))

# ----------------------------------------------------------------------------
# 3. Alinhamento múltiplo progressivo (perfil x sequência, Needleman–Wunsch).
# ----------------------------------------------------------------------------
GAP = -1.0
def col_score(col, cls):                # col: lista de classes (ou None)
    vals = [c for c in col if c is not None]
    if not vals: return 0.0
    return sum(1.0 if c == cls else -1.0 for c in vals) / len(vals)

def align_to_profile(prof_cols, seq_cls):
    """prof_cols: lista de colunas(=listas de classes/None). Retorna novo perfil."""
    m, n = len(prof_cols), len(seq_cls)
    dp = [[0.0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1): dp[i][0] = dp[i-1][0] + GAP
    for j in range(1, n+1): dp[0][j] = dp[0][j-1] + GAP
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = max(dp[i-1][j-1] + col_score(prof_cols[i-1], seq_cls[j-1]),
                           dp[i-1][j] + GAP, dp[i][j-1] + GAP)
    # traceback
    i, j, ops = m, n, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + col_score(prof_cols[i-1], seq_cls[j-1]):
            ops.append(("M", i-1, j-1)); i -= 1; j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + GAP:
            ops.append(("D", i-1, None)); i -= 1            # gap na seq nova
        else:
            ops.append(("I", None, j-1)); j -= 1            # inserção da seq nova
    ops.reverse()
    return ops

def msa(seqs_cls):
    """seqs_cls: lista de listas-de-classe. Retorna matriz (linha por seq) de classes/None."""
    order = sorted(range(len(seqs_cls)), key=lambda k: -len(seqs_cls[k]))
    # perfil-semente = sequência mais longa
    first = order[0]
    cols = [[seqs_cls[first][k]] for k in range(len(seqs_cls[first]))]
    members = [first]
    for idx in order[1:]:
        ops = align_to_profile(cols, seqs_cls[idx])
        newcols, prof_i = [], 0
        for op, pi, sj in ops:
            if op == "M":
                col = cols[pi] + [seqs_cls[idx][sj]]; newcols.append(col)
            elif op == "D":
                newcols.append(cols[pi] + [None])
            else:  # I  -> coluna nova, None p/ membros anteriores
                newcols.append([None]*len(members) + [seqs_cls[idx][sj]])
        cols = newcols; members.append(idx)
    # remontar matriz na ordem original
    pos = {m: r for r, m in enumerate(members)}
    matrix = []
    for orig in range(len(seqs_cls)):
        r = pos[orig]
        matrix.append([col[r] for col in cols])
    return matrix

# ----------------------------------------------------------------------------
# parsing de data/fire-by-family.md  (preserva a ordem das famílias)
# ----------------------------------------------------------------------------
def parse():
    fams = []           # [(family, [(lang, branch, form)])]
    cur_fam = cur_branch = None
    for line in open(SRC, encoding="utf-8"):
        if line.startswith("## "):
            name = line[3:].strip()
            if name.startswith("Nota"): break
            cur_fam = name; cur_branch = None
            fams.append((cur_fam, []))
        elif line.startswith("### "):
            cur_branch = line[4:].strip()
        else:
            m = re.match(r"^\s*- \*\*(.+?):\*\* (.+?)\s*$", line)
            if m and cur_fam is not None:
                lang, form = m.group(1), m.group(2)
                fams[-1][1].append((lang, cur_branch, form))
    return fams

# ----------------------------------------------------------------------------
# render
# ----------------------------------------------------------------------------
def render_cluster(fam, gi, group):
    items = [(lang, br, form, toks) for (lang, br, form, toks) in group]
    seqs_cls = [classes(t) for (_, _, _, t) in items]
    seqs_gra = [[g for g, _ in t] for (_, _, _, t) in items]
    matrix = msa(seqs_cls)                     # classes alinhadas
    # alinhar também os grafemas usando o mesmo gabarito de gaps
    width = len(matrix[0])
    rows_gra = []
    for r, (lang, br, form, toks) in enumerate(items):
        gi_, cells = 0, []
        for c in range(width):
            if matrix[r][c] is None: cells.append("-")
            else: cells.append(seqs_gra[r][gi_]); gi_ += 1
        rows_gra.append((lang, br, cells))
    # template por coluna: classe majoritária; estável se todas iguais
    templ, notes = [], []
    for c in range(width):
        col = [matrix[r][c] for r in range(len(items)) if matrix[r][c] is not None]
        uniq = sorted(set(col))
        if len(uniq) == 1:
            templ.append(uniq[0])
        else:
            from collections import Counter
            maj = Counter(col).most_common(1)[0][0]
            templ.append(maj + "*")
            notes.append(f"col {c+1}: {'/'.join(uniq)}")
    # montar bloco
    colw = max(4, max(len(x) for row in rows_gra for x in row[2]) + 1)
    def fmt(cells): return " ".join(s.ljust(colw) for s in cells)
    L = []
    L.append(f"#### {fam} — conjunto #{gi} (n={len(items)})")
    L.append("")
    L.append("```")
    namew = max(len(f"{lang}") for lang, _, _ in rows_gra) + 2
    for lang, br, cells in sorted(rows_gra, key=lambda x: x[0]):
        L.append(f"{lang.ljust(namew)}{fmt(cells)}")
    L.append(f"{'TEMPLATE(classe)'.ljust(namew)}{fmt(templ)}")
    L.append("```")
    if notes:
        L.append(f"- correspondências variáveis (`*` = classe majoritária): {'; '.join(notes)}")
    else:
        L.append("- todas as colunas têm correspondência regular (classe estável).")
    L.append("")
    return "\n".join(L)

def main():
    filt = sys.argv[1].lower() if len(sys.argv) > 1 else None
    fams = parse()
    out = []
    out.append("# Alinhamentos de cognatos (primeira passada automática)")
    out.append("")
    out.append("Gerado por `tools/align_cognates.py` a partir de `fire-by-family.md`, na ordem")
    out.append("das famílias da lista. Conjuntos de cognatos propostos por clustering do esqueleto")
    out.append("consonantal (classes de som Dolgopolsky simplificadas); alinhamento múltiplo")
    out.append("progressivo. **Heurística de triagem** — ver método em `cognate-method.md`.")
    out.append("")
    out.append("Legenda de classes: **P** labial · **T** dental · **S** sibilante · **K** velar/glotal ·")
    out.append("**M** nasal-m · **N** nasal · **R** líquida · **W**/**J** glides · **V** vogal · `-` gap.")
    out.append("")
    summary = []
    for fam, langs in fams:
        if filt and filt not in fam.lower(): continue
        items = [(lang, br, form, tokenize(form)) for (lang, br, form) in langs]
        groups = cluster(items)
        multi = [g for g in groups if len(g) >= 2]
        singles = [g for g in groups if len(g) == 1]
        summary.append((fam, len(langs), len(multi), len(singles)))
        out.append(f"## {fam}")
        out.append("")
        out.append(f"*{len(langs)} línguas → {len(multi)} conjunto(s) de cognatos (n≥2) "
                   f"+ {len(singles)} isolada(s).*")
        out.append("")
        gi = 0
        for g in multi:
            gi += 1
            out.append(render_cluster(fam, gi, g))
        if singles:
            iso = ", ".join(g[0][0] for g in sorted(singles, key=lambda g: g[0][0]))
            out.append(f"- **isoladas / sem cognato detectado:** {iso}")
            out.append("")
    open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n")
    # resumo no stdout
    print(f"escrito: {OUT}\n")
    print(f"{'família':<48} línguas  conj.  isoladas")
    for fam, n, m, s in summary:
        print(f"{fam:<48} {n:>6}  {m:>5}  {s:>7}")

if __name__ == "__main__":
    main()
