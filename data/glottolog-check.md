# Validação contra o Glottolog (estágio 1)

Confronto de `fire-by-family.md` com o **Glottolog** (CLDF `languages.csv`, `glottolog/glottolog-cldf`). Anexa o **glottocode**, confere a família atribuída à mão
e sinaliza divergências. **Não-destrutivo** — nada nos arquivos curados foi alterado.
Mapeamento completo (inclusive não-casados) em [`glottolog-map.csv`](glottolog-map.csv).

- Nomes confrontados: **531**
- Com glottocode: **531** (100%) — sem match: **0**
- Por automático: **405** · por **mapa manual**: **126** ([`glottolog-manual.csv`](glottolog-manual.csv))
- Dos automáticos: **346** família OK · **2** DIFERE · **0** AMBÍGUO (homônimo) · **57** rótulo areal

> Match automático por nome exato (normalizado), **sensível ao contexto**: entre homônimos
> escolhe-se a candidata cuja família bate com a nossa; pseudo-famílias (*Bookkeeping*,
> *Spurious*…) são descartadas. A cauda que o Glottolog **divide** ou nomeia diferente
> (Armenian → Eastern/Western; Sardinian → Logudorese) foi resolvida **manualmente** em
> `glottolog-manual.csv` e entra aqui com status `MANUAL`.

## Divergências de família (revisar)

Casamento confiável (nome único), mas família difere. Pode ser (a) erro nosso, ou (b)
só **nomenclatura** do Glottolog — ex.: ele aposentou *Niger-Congo* (usa **Atlantic-Congo**),
chama *Kra-Dai* de **Tai-Kadai**, *NW Caucasian* de **Abkhaz-Adyge**, e trata *Omótico*,
*Mande* e *Pama-Nyungan* como famílias independentes.

| Língua | nossa família | família no Glottolog | glottocode |
|---|---|---|---|
| Wolaytta | Afro-Asiatic | Ta-Ne-Omotic | `wola1242` |
| Duun | Niger-Congo | Mande | `duun1245` |

## Casamentos ambíguos (0) — homônimos, conferir manualmente

O nome existe em mais de um languoid e **nenhum** está na família esperada; a candidata
escolhida (abaixo) pode ser homônimo não-relacionado. Verificar antes de confiar no glottocode.


## Não-casados (0) — pendentes

*(nenhum — toda a cauda foi resolvida em `glottolog-manual.csv`.)*

