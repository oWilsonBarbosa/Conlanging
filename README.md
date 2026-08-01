# Conlanging

Materiais para construção de línguas: um curso, um conjunto de bases de dados
tipológicas, e a documentação do projeto **Proto-Orogeniano**.

## Documentação

| Documento | Conteúdo |
|---|---|
| [`docs/01_PROTO_INDO_ANATOLIAN.md`](docs/01_PROTO_INDO_ANATOLIAN.md) | Estado da arte sobre o proto-indo-anatólio — o alvo de reconstrução contra o qual o Proto-Orogeniano é desenhado. Inclui a tabela de restrições de projeto (§9). |
| [`docs/02_PROTO_OROGENIAN_PHONOLOGY.md`](docs/02_PROTO_OROGENIAN_PHONOLOGY.md) | O inventário fonêmico e a fonotática do Proto-Orogeniano. Resposta ao trabalho da lição Phonology 2 do curso. |
| [`docs/03_PROTO_OROGENIAN_FEATURES_RULES.md`](docs/03_PROTO_OROGENIAN_FEATURES_RULES.md) | Matriz de traços distintivos, classes naturais e as regras fonológicas — sincrônicas e diacrônicas. Lição Phonology 3. |
| [`docs/04_SOUND_CHANGE.md`](docs/04_SOUND_CHANGE.md) | **Em andamento.** Mudança sonora: o banco de provas das teorias rivais, a derivação ordenada e as leis vocálicas medidas sobre as formas flexionadas. Lição Phonology 4. |

## Ferramentas

| Diretório | Conteúdo |
|---|---|
| [`tools/po-phonology/`](tools/po-phonology/) | Inventário fonêmico e gerador de palavras do Proto-Orogeniano (Python 3, sem dependências). |
| [`tools/po-derivation/`](tools/po-derivation/) | Banco de provas da derivação e das teorias rivais — inverte as 766 raízes e mede legalidade, colisão e ambiguidade; e mede as leis vocálicas sobre 40.894 formas flexionadas. |
| [`tools/pdf-ocr/`](tools/pdf-ocr/) | Recupera texto de PDFs que são só imagem, envelopando o fluxo CCITT num TIFF mínimo e passando ao tesseract — sem renderizador externo. |

## Dados

`data/` reúne bases públicas usadas para calibrar decisões tipológicas:

| Arquivo | Base | Uso |
|---|---|---|
| `bdproto-master.zip` | BDPROTO | inventários fonológicos de protolínguas — calibra o inventário do proto-ramo |
| `clts-master.zip`, `clts-2.3.0.zip` | CLTS | sistema de traços fonéticos |
| `pbasefiles.zip` | PBase | padrões e alternâncias fonológicas — 21.794 padrões em 625 línguas; usado em `docs/04` §6 para conferir a alofonia |
| `phonotacticon-main.zip` | Phonotacticon | tipologia de estrutura silábica |
| `wals-master.zip`, `wals-v2020.4.zip` | WALS | traços tipológicos e suas coocorrências |
| `grambank-master.zip` | Grambank | traços gramaticais |
| `concepticon-data-3.4.0.zip` | Concepticon | listas de conceitos (Swadesh e outras) |
| `wold_dataset.cldf.zip` | WOLD | *borrowability* — o que se empresta de um substrato |
| `MorphyNet-main.zip`, `MorphoLex-en-master.zip` | MorphyNet, MorphoLex | morfologia derivacional e flexional em escala |
| `wiktextract-master.zip` | wiktextract | extração do Wiktionary |
| `dev-master.zip` | — | ver o README interno do arquivo |

## Curso

`course/` contém as 13 aulas numeradas (fonologia 1–4, morfologia, verbos,
casos, número, classe, alinhamento, léxico, estrutura informacional,
documentação) com as respectivas listas de exercícios.

## Repositórios relacionados

- **`PIE_roots`** — 1.891 verbetes de proto-indo-europeu extraídos do Wiktionary
  (873 raízes), a base lexical de origem.
- **`0r063N`** — o planeta Orogen: geografia física, história geológica,
  paleoclima e camada biológica.
