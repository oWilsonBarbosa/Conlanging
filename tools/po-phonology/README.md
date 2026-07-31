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
| `inventory.py` | os 40 fonemas, organizados por série e ponto de articulação; as duas classes harmônicas; `series_of()`, `is_glottalized()`, `harmony_of()`, `agrees()` |
| `gen.py` | molde silábico, pesos de onset/coda medidos sobre as 873 raízes de `PIE_roots`, harmonia de raiz, validação de junção silábica e acento livre |

Cada forma gerada vem marcada com sua classe: `[−round]` ou `[+round]`.

## Restrições impostas

- molde `(s)(C)(R)` · `V | R̩` · `(R)(C)(s)`, máximo 3 por margem
- pesos de onset e coda proporcionais à contagem real sobre as raízes do PIE
- **harmonia de raiz**: todos os segmentos harmônicos de uma forma pertencem à
  mesma classe. Vogais e dorsais concordam; labiais, dentais, palatais, `/s sː/`
  e sonorantes são neutros. Imposta na **seleção**, não filtrada depois
- **dissimilação glotálica**: no máximo uma obstruinte glotalizada por raiz
  (medido no PIE: 1 raiz em 216 com duas)
- lacuna sistemática em `/ʔp/` — não é filtro posterior, o fonema não existe
- junção medial de no máximo 2 segmentos, sem segmentos idênticos adjacentes

## Limitações conhecidas

O gerador é uma primeira aproximação e **não** modela:

- frequência relativa dos fonemas (todos são equiprováveis dentro da classe —
  o PIE real tem `/s/`, `/e/` e as sonorantes muito acima da média)
- restrições de coocorrência além da glotálica e da harmônica
- ablaut, que é o que de fato organiza a alternância vocálica
- qualquer morfologia

Sobre a harmonia: o domínio é a **palavra inteira**, porque não há ainda
morfologia derivacional que justifique um domínio menor. Sufixos harmônicos e
neutros — o que qualquer sistema de harmonia real tem — ficam para depois das
lições 03 e 05.

A tarefa 7 da lição — conferir as regras — pressupõe curadoria da saída. As
formas do documento 02 foram escolhidas da saída bruta, não aceitas em bloco.
