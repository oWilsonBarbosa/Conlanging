# `po-derivation`

Banco de provas da derivação Proto-Orogeniano → proto-indo-hitita, e das
teorias rivais que a disputam. Python 3, **sem dependências**.

Especificação em [`docs/04_SOUND_CHANGE.md`](../../docs/04_SOUND_CHANGE.md).

## Uso

```bash
python3 invert.py             # todas as teorias, resumo comparativo
python3 invert.py baseline    # uma teoria, com violações e colisões
python3 invert.py --ambiguidade  # onde a inversão escolhe sem evidência
python3 derive.py             # deriva e compara as duas ordens de regras
python3 derive.py --sample    # derivações passo a passo
python3 stems.py              # perfil do corpus de formas flexionadas
python3 stems.py --abtonung   # o grau-o contra o acento
python3 stems.py --longas     # de onde vêm as vogais longas
python3 stems.py --lei-m      # as duas leis do *o, separadas
python3 tarefa4.py            # tarefa 4: dez mudanças sorteadas, aplicadas
python3 tarefa4.py --custo    # o que cada mudança funde, sozinha
```

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `theories.py` | as variantes como **configuração**: correspondências PIE ↔ PO. Trocar de teoria é trocar um dicionário, não bifurcar o código |
| `invert.py` | segmentação das raízes, inversão e as três medidas |
| `derive.py` | a derivação ordenada PO → PIE clássico, e o teste de que a ordem importa |
| `tarefa4.py` | a tarefa 4 do exercício — sorteia dez mudanças de um catálogo de vinte **antes** de ver as palavras, aplica, e mede o que funde nos paradigmas |
| `stems.py` | o corpus de **formas flexionadas** — 40.894 formas, 93 % com acento. É o corpus que permite testar a *Abtönung* e as vogais longas, que as raízes não permitem |

## As três medidas, e por que não são circulares

O Proto-Orogeniano é definido pelas correspondências com o PIE, então derivar
para a frente devolveria o PIE por construção — um "índice de acerto" daria
100 % sem significar nada. O que se mede em vez disso:

- **legalidade** — as formas resultantes obedecem à fonotática do documento 02
  §4? É o teste que pode reprovar uma teoria.
- **colisão** — quantas raízes distintas fundem na mesma forma.
- **ambiguidade** — quantos pontos não são invertíveis. **80 % das raízes têm
  pelo menos um**: 23 % por laringal (`*h₁`, `*H`) e 73 % por sonorante ou
  `*s`, que a regra K4 degemina. Toda forma proto-orogeniana citada nos
  documentos é *uma* das pré-imagens legais, não a única.

## Armadilha na leitura dos números

**Menos violações não é teoria melhor.** As violações do baseline são, na
maioria, previsões cumprindo-se: as raízes com `*b` violam porque a lacuna
`/ʔp/` prevê que elas não deveriam existir. Uma teoria que não faz a previsão
não pode falhá-la e marca menos. Ver `docs/04` §2.3.

## Limitações conhecidas

- A variante da aspiração usa símbolos que `is_glottalized()` não reconhece, e
  por isso escapa de uma violação que deveria marcar.
- As raízes do dataset vêm **sem acento** — mas isso não impede o teste da
  *Abtönung*, só o desloca: use `stems.py`, que lê as tabelas de flexão, onde
  93 % das formas marcam acento. *(O agudo é pré-composto; normalize para NFD
  antes de contar, ou a contagem erra por duas ordens de grandeza.)*
- O corpus de flexão não é evidência independente da *Abtönung*: quem
  reconstruiu essas formas já assume a regra. O que ele mede é a consistência
  da aplicação. Ver `docs/04` §8.2.
- A inversão trabalha segmento a segmento; não há ainda ordenação de regras
  nem contexto.
