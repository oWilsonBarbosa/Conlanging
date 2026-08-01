# `po-derivation`

Banco de provas da derivação Proto-Orogeniano → proto-indo-hitita, e das
teorias rivais que a disputam. Python 3, **sem dependências**.

Especificação em [`docs/04_SOUND_CHANGE.md`](../../docs/04_SOUND_CHANGE.md).

## Uso

```bash
python3 invert.py             # todas as teorias, resumo comparativo
python3 invert.py baseline    # uma teoria, com violações e colisões
python3 derive.py             # deriva e compara as duas ordens de regras
python3 derive.py --sample    # derivações passo a passo
```

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `theories.py` | as variantes como **configuração**: correspondências PIE ↔ PO. Trocar de teoria é trocar um dicionário, não bifurcar o código |
| `invert.py` | segmentação das raízes, inversão e as três medidas |
| `derive.py` | a derivação ordenada PO → PIE clássico, e o teste de que a ordem importa |

## As três medidas, e por que não são circulares

O Proto-Orogeniano é definido pelas correspondências com o PIE, então derivar
para a frente devolveria o PIE por construção — um "índice de acerto" daria
100 % sem significar nada. O que se mede em vez disso:

- **legalidade** — as formas resultantes obedecem à fonotática do documento 02
  §4? É o teste que pode reprovar uma teoria.
- **colisão** — quantas raízes distintas fundem na mesma forma.
- **ambiguidade** — quantos pontos não são invertíveis.

## Armadilha na leitura dos números

**Menos violações não é teoria melhor.** As violações do baseline são, na
maioria, previsões cumprindo-se: as raízes com `*b` violam porque a lacuna
`/ʔp/` prevê que elas não deveriam existir. Uma teoria que não faz a previsão
não pode falhá-la e marca menos. Ver `docs/04` §2.3.

## Limitações conhecidas

- A variante da aspiração usa símbolos que `is_glottalized()` não reconhece, e
  por isso escapa de uma violação que deveria marcar.
- As raízes do dataset vêm **sem acento**, e a *Abtönung* é condicionada por
  acento. Essa regra não é testável neste corpus.
- A inversão trabalha segmento a segmento; não há ainda ordenação de regras
  nem contexto.
