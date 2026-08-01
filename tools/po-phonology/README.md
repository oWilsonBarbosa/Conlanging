# `po-phonology`

Inventário e gerador de palavras do Proto-Orogeniano. Python 3, **sem
dependências**.

Implementa o que está descrito em
[`docs/02_PROTO_OROGENIAN_PHONOLOGY.md`](../../docs/02_PROTO_OROGENIAN_PHONOLOGY.md);
esse documento é a especificação, este diretório é a implementação.

## Uso

```bash
python3 inventory.py            # imprime o inventário e o total de fonemas
python3 gen.py 20 --roots       # 20 raízes monossilábicas canônicas
python3 gen.py 20 --words       # 20 palavras polissilábicas
python3 gen.py 20 --seed 1234   # outra semente (padrão: 4400)
```

A saída é determinística por semente — as formas citadas no documento 02 saem
com `--seed 4400`.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `inventory.py` | os 34 fonemas, organizados por série e ponto de articulação; `series_of()` e `is_glottalized()` |
| `gen.py` | molde silábico, pesos de onset/coda medidos sobre as 873 raízes de `PIE_roots`, validação de junção silábica e acento livre |

## Restrições impostas

- molde `(s)(C)(R)` · `V | R̩` · `(R)(C)(s)`, máximo 3 por margem
- pesos de onset e coda proporcionais à contagem real sobre as raízes do PIE
- **dissimilação glotálica**: no máximo uma obstruinte glotalizada por raiz
  (medido no PIE: 1 raiz em 216 com duas)
- lacuna sistemática em `/ʔp/` — não é filtro posterior, o fonema não existe
- junção medial de no máximo 2 segmentos, sem segmentos idênticos adjacentes

## Limitações conhecidas

O gerador é uma primeira aproximação e **não** modela:

- frequência relativa dos fonemas (todos são equiprováveis dentro da classe —
  o PIE real tem `/s/`, `/e/` e as sonorantes muito acima da média)
- restrições de coocorrência além da glotálica — em especial a **concordância
  de ajuste laríngeo** (fortis com fortis, lenis com lenis), que o documento 02
  §4.4 mede mas o gerador ainda não impõe
- ablaut, que é o que de fato organiza a alternância vocálica
- qualquer morfologia

O vocalismo é de **uma qualidade** (`/e eː/`): o grau zero e as sonorantes
silábicas fazem o resto. `[o]`, `[a]`, `[i]` e `[u]` não são fonemas — ver
documento 02 §3.4 para de onde cada um vem.

A tarefa 7 da lição — conferir as regras — pressupõe curadoria da saída. As
formas do documento 02 foram escolhidas da saída bruta, não aceitas em bloco.
