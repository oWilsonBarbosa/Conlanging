#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Estágio 1: valida fire-by-family.md contra o Glottolog (CLDF languages.csv).
# Não-destrutivo: gera data/glottolog-check.md (relatório) e data/glottolog-map.csv
# (mapeamento nome->glottocode reutilizável). Não altera arquivos curados.
# O CSV do Glottolog é baixado uma vez para um cache gitignored, se ausente.
import csv, re, unicodedata, os, sys, urllib.request

ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA  = os.path.join(ROOT, "data")
GLOTTO = os.path.join(DATA, ".glottolog-languages.csv")    # cache (ver .gitignore)
GLOTTO_URL = ("https://raw.githubusercontent.com/glottolog/glottolog-cldf/"
              "master/cldf/languages.csv")
SRC  = os.path.join(DATA, "fire-by-family.md")
REkP = os.path.join(DATA, "glottolog-check.md")
MAPP = os.path.join(DATA, "glottolog-map.csv")

if not os.path.exists(GLOTTO):
    print(f"baixando Glottolog CLDF languages.csv -> {GLOTTO} ...", file=sys.stderr)
    urllib.request.urlretrieve(GLOTTO_URL, GLOTTO)

def norm(s):
    s = re.split(r"\s*\(", s)[0]
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()

# ---- index Glottolog (todas as candidatas por nome) ----
by_name, by_code = {}, {}
with open(GLOTTO, encoding="utf-8") as f:
    for r in csv.DictReader(f):
        by_code[r["Glottocode"]] = r
        by_name.setdefault(norm(r["Name"]), []).append(r)
PSEUDO = {"bookkeeping", "unclassifiable", "spurious", "unattested",
          "artificial language", "sign language", "speech register"}

def fam_name(r):
    if r.get("Is_Isolate") == "true":
        return "(isolate)"
    fid = r.get("Family_ID") or ""
    if not fid:
        return "(top-level/isolate)" if r["Level"] != "family" else r["Name"]
    fr = by_code.get(fid)
    return fr["Name"] if fr else fid

# ---- normalização de NOME DE FAMÍLIA p/ comparação ----
def famkey(s): return re.sub(r"[^a-z0-9]", "", norm(s))   # norm() já corta parênteses
FAM_ALIAS = {   # famkey(nossa etiqueta) -> família canônica do Glottolog (só nomenclatura)
    "kradai":            "taikadai",
    "northwestcaucasian":"abkhazadyge",
    "northeastcaucasian":"nakhdaghestanian",
    "nigercongo":        "atlanticcongo",   # Bantu/Volta; Mande fica como DIFERE (correto)
    "australian":        "pamanyungan",
}
# famílias nossas que são rótulos AREAIS/cobertura: não cobrar concordância genética
def is_areal_fam(ourfam):
    return ourfam.startswith(("Papuan", "Khoisan", "Isolates", "Constructed",
                              "Creoles", "Americas"))

# ---- parse fire-by-family.md (na ordem) ----
ours = []   # (lang, ourfam)
curfam = None
for line in open(SRC, encoding="utf-8"):
    if line.startswith("## "):
        n = line[3:].strip()
        if n.startswith("Nota"): break
        curfam = n
    m = re.match(r"^\s*- \*\*(.+?):\*\* ", line)
    if m and curfam:
        ours.append((m.group(1), curfam))

# ---- match sensível ao contexto ----
def fam_ok(ourfam, glfam):
    ofk = famkey(ourfam); gfk = famkey(glfam)
    ofk = FAM_ALIAS.get(ofk, ofk)
    return bool(ofk) and (gfk == ofk or ofk in gfk or gfk in ofk)

# ---- mapeamento manual curado (resolve a cauda de não-casados) ----
MANUAL = {}   # language -> glottocode
manual_csv = os.path.join(DATA, "glottolog-manual.csv")
if os.path.exists(manual_csv):
    for r in csv.DictReader(open(manual_csv, encoding="utf-8")):
        MANUAL[r["language"]] = r["glottocode"]

LEVEL_RANK = {"language": 0, "dialect": 1, "family": 2}
rows = []     # (lang, ourfam, glottocode, glname, glfam, status)
matched = unmatched = agree = differ = areal_n = ambig = manual_n = 0
for lang, ourfam in ours:
    # override manual tem prioridade
    if lang in MANUAL and MANUAL[lang] in by_code:
        r = by_code[MANUAL[lang]]
        rows.append((lang, ourfam, r["Glottocode"], r["Name"], fam_name(r), "MANUAL"))
        matched += 1; manual_n += 1; continue
    cands = [r for r in by_name.get(norm(lang), [])
             if famkey(fam_name(r)) not in PSEUDO]
    is_areal = is_areal_fam(ourfam)
    if not cands:
        rows.append((lang, ourfam, "", "", "", "SEM-MATCH")); unmatched += 1; continue
    # prefere candidata cuja família bate com a nossa; senão, língua > dialeto
    fam_hits = [r for r in cands if fam_ok(ourfam, fam_name(r))]
    if fam_hits:
        r = sorted(fam_hits, key=lambda x: LEVEL_RANK.get(x["Level"], 3))[0]
        status = "OK"; agree += 1
    else:
        r = sorted(cands, key=lambda x: LEVEL_RANK.get(x["Level"], 3))[0]
        if is_areal:
            status = "AREAL"; areal_n += 1
        elif len(cands) > 1:
            status = "AMBÍGUO"; ambig += 1     # homônimos, nenhum na família esperada
        else:
            status = "DIFERE"; differ += 1
    matched += 1
    rows.append((lang, ourfam, r["Glottocode"], r["Name"], fam_name(r), status))

# ---- escreve mapeamento CSV ----
with open(MAPP, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["language", "our_family", "glottocode", "glottolog_name",
                "glottolog_family", "status"])
    for row in rows: w.writerow(row)

# ---- escreve relatório ----
def esc(s): return s.replace("|", "\\|")
L = []
A = L.append
A("# Validação contra o Glottolog (estágio 1)")
A("")
A("Confronto de `fire-by-family.md` com o **Glottolog** (CLDF `languages.csv`, "
  "`glottolog/glottolog-cldf`). Anexa o **glottocode**, confere a família atribuída à mão")
A("e sinaliza divergências. **Não-destrutivo** — nada nos arquivos curados foi alterado.")
A("Mapeamento completo (inclusive não-casados) em [`glottolog-map.csv`](glottolog-map.csv).")
A("")
A(f"- Nomes confrontados: **{len(ours)}**")
A(f"- Com glottocode: **{matched}** ({100*matched//len(ours)}%) — sem match: **{unmatched}**")
A(f"- Por automático: **{matched - manual_n}** · por **mapa manual**: **{manual_n}** "
  f"([`glottolog-manual.csv`](glottolog-manual.csv))")
A(f"- Dos automáticos: **{agree}** família OK · **{differ}** DIFERE · **{ambig}** AMBÍGUO "
  f"(homônimo) · **{areal_n}** rótulo areal")
A("")
A("> Match automático por nome exato (normalizado), **sensível ao contexto**: entre homônimos")
A("> escolhe-se a candidata cuja família bate com a nossa; pseudo-famílias (*Bookkeeping*,")
A("> *Spurious*…) são descartadas. A cauda que o Glottolog **divide** ou nomeia diferente")
A("> (Armenian → Eastern/Western; Sardinian → Logudorese) foi resolvida **manualmente** em")
A("> `glottolog-manual.csv` e entra aqui com status `MANUAL`.")
A("")

diffs = [r for r in rows if r[5] == "DIFERE"]
A("## Divergências de família (revisar)")
A("")
A("Casamento confiável (nome único), mas família difere. Pode ser (a) erro nosso, ou (b)")
A("só **nomenclatura** do Glottolog — ex.: ele aposentou *Niger-Congo* (usa **Atlantic-Congo**),")
A("chama *Kra-Dai* de **Tai-Kadai**, *NW Caucasian* de **Abkhaz-Adyge**, e trata *Omótico*,")
A("*Mande* e *Pama-Nyungan* como famílias independentes.")
A("")
if diffs:
    A("| Língua | nossa família | família no Glottolog | glottocode |")
    A("|---|---|---|---|")
    for lang, of, code, gn, gf, st in diffs:
        A(f"| {esc(lang)} | {esc(of)} | {esc(gf)} | `{code}` |")
else:
    A("*(nenhuma)*")
A("")

amb = [r for r in rows if r[5] == "AMBÍGUO"]
A(f"## Casamentos ambíguos ({len(amb)}) — homônimos, conferir manualmente")
A("")
A("O nome existe em mais de um languoid e **nenhum** está na família esperada; a candidata")
A("escolhida (abaixo) pode ser homônimo não-relacionado. Verificar antes de confiar no glottocode.")
A("")
if amb:
    A("| Língua | nossa família | candidata escolhida (família) | glottocode |")
    A("|---|---|---|---|")
    for lang, of, code, gn, gf, st in amb:
        nm = f"{gn} " if norm(gn) != norm(lang) else ""
        A(f"| {esc(lang)} | {esc(of)} | {esc(nm)}({esc(gf)}) | `{code}` |")
A("")

unm = [r[0] for r in rows if r[5] == "SEM-MATCH"]
A(f"## Não-casados ({len(unm)}) — pendentes")
A("")
if unm:
    A("Sem glottocode no automático nem no mapa manual. Adicionar a `glottolog-manual.csv`.")
    A("")
    A(", ".join(unm))
else:
    A("*(nenhum — toda a cauda foi resolvida em `glottolog-manual.csv`.)*")
A("")

open(REkP, "w", encoding="utf-8").write("\n".join(L) + "\n")

# ---- stdout ----
print(f"com glottocode {matched}/{len(ours)} (auto {matched-manual_n} + manual {manual_n}) | "
      f"OK {agree} | DIFERE {differ} | AMBÍGUO {ambig} | areal {areal_n} | sem-match {unmatched}")
print("\nDIFERE (família difere, match confiável):")
for lang, of, code, gn, gf, st in diffs:
    print(f"  {lang:24} {of:30} -> {gf}")
print("\nAMBÍGUO (homônimo, conferir):")
for lang, of, code, gn, gf, st in amb:
    print(f"  {lang:24} -> {gn} ({gf})")
