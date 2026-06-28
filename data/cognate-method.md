# Método para achar o *template* comum de cognatos

Como, a partir das listas de palavras (ex.: `fire-by-family.md`), recuperar a **forma-mãe**
comum a um conjunto de cognatos — o "template" do qual as línguas-filhas derivam. É o
**método comparativo** da linguística histórica, operacionalizado com os datasets em `data/`.

Para um conlang isto serve nas duas direções:
1. **Análise** — descobrir como uma proto-forma vira suas filhas (as *leis de som*).
2. **Geração** — definir as leis e *produzir* as filhas a partir da raiz inventada.

---

## Princípio 0 — Comparar **pronúncia (IPA)**, nunca a grafia

A escrita engana, e as listas misturam script nativo, romanização e IPA. Exemplos das
próprias listas:

- `g` = /ɣ/ no Espanhol *fuego*, mas /ɡ/ no Português *fogo* — mesma letra, sons diferentes.
- `ch` = /x/ numa romanização, /tʃ/ noutra.
- Armênio *hur* e Grego *pûr* parecem distantes na escrita, mas `h-` é o reflexo **regular**
  de `p-`; só os fonemas revelam isso.

**Passo zero, portanto: normalizar tudo para IPA fonêmico.** É exatamente o papel do
**CLTS** (`data/clts-master.zip`):

| Recurso CLTS | Para quê |
|---|---|
| `data/graphemes.tsv` | mapeia grafemas/romanizações → IPA (orthography profiles) |
| `data/sounds.tsv` | cada som IPA → vetor de **traços** (ponto, modo, vozeamento…) |
| `pkg/soundclasses/lingpy.tsv` | IPA → **classes de som** (alfabeto reduzido p/ alinhar) |

As classes de som (SCA/Dolgopolsky) agrupam sons que costumam corresponder entre línguas
(ex.: todas as oclusivas labiais p/b/f/v numa classe **P**), o que torna o alinhamento
robusto a pequenas diferenças.

---

## Princípio 1 — Significado ≠ cognato: **particionar primeiro**

Agrupar por *sentido* ("fire") **não** dá um conjunto de cognatos. Dentro de "fire" há
palavras de **origens distintas**, que não se reconstroem juntas. No indo-europeu, "fogo"
vem de **três** fontes diferentes:

- **\*péh₂ur̥** (fogo *inanimado*, "a substância"): Grego *pûr*, inglês *fire*, Hitita
  *paḫḫur*, Tocário B *puwar*, Armênio *hur*.
- **\*h₁n̥gʷnis** (fogo *animado*): Latim *ignis*, Sânscrito *agni*, Lituano *ugnis*,
  Eslavo Eclesiástico *ognĭ*.
- **Latim *focus*** ("lareira"), que substituiu *ignis* e gerou todo o românico (*fogo*,
  *fuego*, *fuoco*, *feu*…).

Antes de reconstruir, **separe o conjunto-significado em conjuntos de cognatos** usando
correspondências sonoras regulares (passo 3 do pipeline). Empréstimos e inovações
(ex.: Servo-croata *vatra*, Búlgaro…) também são descartados aqui.

---

## Princípio 2 — Reconstruir **de baixo pra cima**, nível por nível

O método é hierárquico e a árvore de `fire-by-family.md` já é o andaime:

1. Comparar **irmãs** (mesmo nível) → reconstruir a **mãe** (um nível acima).
   Ex.: línguas românicas → Proto-Românico.
2. Comparar **mães reconstruídas** entre si → reconstruir a **avó**.
   Ex.: Proto-Românico + Proto-Germânico + Proto-Eslavo… → PIE.
3. **Níveis diferentes** servem de **âncora**: uma mãe *atestada* na lista (Latim, Old Norse,
   Ancient Greek, Old Church Slavonic…) **valida** a reconstrução. Se o teu Proto-Românico
   bate com o Latim atestado, o método está calibrado.

> Resumo: **mesmo nível** para reconstruir; **níveis diferentes** para verificar.

---

## O pipeline (6 passos)

| # | Passo | O que faz | Ferramenta / dado |
|--:|-------|-----------|-------------------|
| 1 | **Significado** | ancora o conceito (FIRE = Concepticon 221) | `concept-list.csv` / Concepticon |
| 2 | **IPA** | grafia → IPA fonêmico → classes de som | **CLTS** (`graphemes.tsv`, `sounds.tsv`, `soundclasses/lingpy.tsv`) |
| 3 | **Cognação** | particiona o conjunto-significado em cognatos | LexStat/SCA (LingPy) ou manual por correspondência |
| 4 | **Alinhamento** | alinha as formas **coluna a coluna** | multiple alignment (SCA; LingPy/EDICTOR) |
| 5 | **Correspondências** | extrai a regra som-a-som de cada coluna | tabela de correspondências |
| 6 | **Reconstrução** | deriva o proto-segmento de cada coluna → *template* | método comparativo |

Mudanças sonoras já atestadas (p/ checar plausibilidade) estão em
`data/clts-master.zip → pkg/transcriptiondata/diachronica.tsv` (base do *Index Diachronica*).

---

## Exemplo trabalhado A — *fogo* → Proto-Românico **\*ˈfɔku**

Conjunto de cognatos (filhas do Latim *focus* /ˈfokus/, todas em `fire-by-family.md`):

**Passo 4 — alinhamento** (uma coluna por correspondência; `—` = ∅):

| Língua | C1 | V1 | (G) | C2 | V2 | C3 |
|--------|:--:|:--:|:--:|:--:|:--:|:--:|
| Latim *focus*     | f | ɔ | —  | k | u | s |
| Italiano *fuoco*  | f | w | ɔ  | k | o | — |
| Espanhol *fuego*  | f | w | e  | ɣ | o | — |
| Português *fogo*  | f | o | —  | ɡ | u | — |
| Francês *feu*     | f | ø | —  | — | — | — |
| Romeno *foc*      | f | o | —  | k | — | — |
| Sardo *fogu*      | f | o | —  | ɡ | u | — |

**Passo 5 — correspondências regulares:**

| Posição | Latim | reflexos | regra |
|---|---|---|---|
| C1 inicial | k... f | f em todas | **f- estável** |
| V1 (ˈo tônico, sílaba aberta) | o | *uo/ue* (It, Es), *o* (Pt, Ro), *ø* (Fr) | **ditongação** do o tônico no oeste/italo-românico |
| C2 intervocálico | k | **k** (It, Ro) ~ **ɡ/ɣ** (Pt, Es, Sard) ~ **∅** (Fr) | **lenição** do -k- intervocálico (mantém-se a leste, voza/cai a oeste) |
| -s final | s | ∅ | **perda do -s** (exceto ibero-românico de plural) |

**Passo 6 — template:** Proto-Românico **\*ˈfɔku** — **confirmado** pelo Latim atestado
*focus* (a âncora de nível superior). ✅

---

## Exemplo trabalhado B — *fire* → PIE **\*péh₂ur̥**

Comparando os **proto-formas de ramo** (cada um já reconstruído a partir das suas irmãs):

**Passo 4 — alinhamento:**

| Ramo (forma citada) | C1 | núcleo | resto |
|---------------------|:--:|:------:|:------|
| Helênico — Grego *pûr* | p | uː | r |
| Anatólico — Hitita *paḫḫur* | p | a | ḫ(ʷ)ur |
| Tocário — Toc. B *puwar* | p | u | war |
| Itálico/Germânico — ing. *fire* < *fȳr | **f** | uː | r |
| Armênio — *hur* | **h** | u | r |

**Passo 5 — a correspondência inicial diagnóstica:**

| | p | p | p | f | h |
|---|---|---|---|---|---|
| ramo | Grego | Hitita | Tocário | Germânico | Armênio |

A série **p ~ p ~ p ~ f ~ h** é **regular** (a mesma aparece em "pai": *patḗr / fadar / hayr*):
é a **Lei de Grimm** (p→f no germânico) e a mudança **p→h** do armênio. O `ḫ` hitita
preserva a **laringal \*h₂**.

**Passo 6 — template:** PIE **\*péh₂ur̥** (raiz heteroclítica r/n: genitivo *ph₂uéns*).
A coexistência das duas raízes (\*péh₂ur̥ vs \*h₁n̥gʷnis) em ramos diferentes mostra por que
o **passo 3 (particionar)** é obrigatório: juntar tudo por significado misturaria dois
templates incompatíveis.

---

## Usando o método "ao contrário" (para o conlang)

1. Defina o **inventário** da proto-língua (já há `concept-list.csv` p/ os conceitos a cunhar).
2. Cunhe a **proto-forma** da raiz (ex.: *fire* = `*TAR-`).
3. Escreva as **leis de som** por filha (lenição? ditongação? perda de final?), inspirando-se
   em correspondências reais de `diachronica.tsv`.
4. **Aplique** as leis em cascata pela árvore (`fire-by-family.md` dá a topologia) para gerar
   formas-filhas regulares e cognatas entre si.
5. Verifique rodando o método comparativo *para frente* nas filhas geradas: você deve
   **recuperar** a proto-forma. Se não recuperar, alguma lei não é regular.

---

## Notas e limitações

- **Regularidade é o critério.** Uma correspondência só conta se for **recorrente** em vários
  cognatos; coincidências isoladas (e empréstimos) não reconstroem nada.
- A cognação automática (LexStat) **propõe** conjuntos; a decisão final e a reconstrução
  continuam sendo julgamento informado, não saída de algoritmo.
- As **formas citadas** nas listas às vezes vêm sem IPA — o passo 2 (CLTS / orthography
  profile) é o que padroniza antes de qualquer comparação.
- Reconstruções marcadas com `*` são hipóteses; as âncoras atestadas (Latim, Grego antigo…)
  é que mantêm o método honesto.

## Datasets relevantes (em `data/`)

- **CLTS** (`clts-master.zip`) — IPA, traços, classes de som, `diachronica.tsv`.
- **Concepticon** (`concepticon-data-3.4.0.zip`) — ancoragem de significado (FIRE = 221).
- **WOLD** (`wold_dataset.cldf.zip`) — *borrowed scores*, para descartar empréstimos no passo 3.
- **BDPROTO** (`bdproto-master.zip`) — inventários de proto-línguas reconstruídas (referência).
