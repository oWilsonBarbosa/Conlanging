# Proto-Orogeniano — fonologia

**Conlangs University · Phonology 2 — "Designing a phonology"**

Este documento é a resposta ao trabalho da lição 06 do curso (`course/06
Phonology 2.pdf` e `06a`), aplicada ao Proto-Orogeniano. Ele segue a estrutura
das sete tarefas do enunciado.

| | |
|---|---|
| Lição | Phonology 2 — Designing a phonology (Slorany, abril 2020) |
| Pré-requisito cumprido | Phonology 1 (IPA, fonema vs. fone) |
| Restrições de entrada | [`01_PROTO_INDO_ANATOLIAN.md`](01_PROTO_INDO_ANATOLIAN.md) §9 |
| Ferramentas | [`tools/po-phonology/`](../tools/po-phonology/) |
| Próximas lições | Phonology 3 (traços e notação de regras) → Phonology 4 (mudança sonora) |

## Posição no curso

A trilha de fonologia do curso tem quatro lições: **1** (IPA e notação),
**2** (desenhar uma fonologia), **3** (traços distintivos e notação de regras)
e **4** (mudança sonora). Estamos na **2** porque ainda não há inventário — e
o inventário é pré-requisito das lições 3 e 4 em qualquer ordem. A lição 4 é
onde o projeto realmente se decide, porque é lá que a derivação
Proto-Orogeniano → proto-indo-hitita vira um conjunto de regras verificável
contra as 873 raízes.

## O caso do curso que se aplica a nós

A lição enumera cinco maneiras de escolher os sons de uma língua. A nossa é a
**quinta** — *"Choose phone(me)s based on a specific input"* — e a lição
descreve exatamente a nossa situação:

> *"An a posteriori conlanger will have to take into consideration the existing
> phonology of the language their conlang will be derived from, and the
> daughter will likely not stray too far from the parent."*

Com uma inversão: aqui **a filha é a língua atestada** (o PIH, e através dele o
PIE) e a mãe é a que estamos construindo. O input não é uma sugestão, é uma
obrigação — o sistema tem que produzir o alvo de §9.1 por mudança regular.

Isso apaga quase toda a liberdade estética que a lição normalmente concede. O
que sobra de escolha real está marcado como **PROJETO** ao longo do texto.

---

## 1 | Como a língua deve soar

**Gutural, tensa e cortada.** Três coisas produzem esse efeito, e as três são
exigidas pelo alvo, não escolhidas:

- **Uvulares em posição de destaque.** As laringais do PIE são, no PIH,
  oclusivas uvulares (`*h₂ = *[qː]`, `*h₃ = *[qʷː]`). Elas não são sons de
  rodapé: aparecem em **397 das 873 raízes (45 %)**. Uma língua cujo fonema
  mais frequente depois das oclusivas comuns é uma uvular longa soa,
  necessariamente, guteral.
- **Glotalização.** A série que o PIE clássico reinterpretou como "sonora" era
  pré-glotalizada. Isso dá um ataque cortado, tenso, em um terço das
  obstruintes.
- **Harmonia de arredondamento.** Oito vogais contra 32 consoantes: a língua
  segue consonante-pesada, mas o vocalismo não é pobre — é **organizado**. Cada
  raiz pertence a uma de duas classes, e ouve-se isso como uma cor que
  atravessa a palavra inteira, dorsais inclusive.

**Comparação com línguas reais.** Não há uma só: o perfil é duplo. Pelas
consoantes — inventário denso, uvulares, glotalização — o mais próximo é o
**Cáucaso Noroeste** (abkhaz, ubykh). Pela harmonia vocálica de raiz, o
paralelo é **turco ou urálico**. O contraste de duração consonantal fazendo
trabalho lexical lembra o finlandês ou o italiano.

Essa combinação não existe em nenhuma língua real, e é a assinatura da língua:
consoantes caucasianas com morfofonologia urálica.

Há uma coincidência agradável nisso, registrada como observação e não como
argumento: §7.4 do documento 01 diz que o indo-europeu sofreu influência de
substrato **norte-caucasiano** ao chegar à estepe. Uma língua com esse perfil
não teria soado estrangeira ali.

**O que ela não é.** Não é fluida, não é melodiosa, não é vocálica. Não tem
tom. Não tem nasais vocálicas, retroflexas, cliques nem faringais.

---

## 2 | Amostra sonora

Arranjo fonoestético, **não uma frase analisada** — a morfologia é assunto das
lições 03 e 05, e nenhuma decisão morfológica foi tomada ainda. O que segue é
uma sequência de formas com o formato de raiz, arranjadas pelo som:

Classe `[−round]`:

```
/ˈqːweq  ˈstːeqː  wejˈʔt-es  ˈlewkː-mn̩  pːenˈtː-eres/
```

Classe `[+round]`:

```
/ˈqʷːor  ˈkʷːolːtː  moˈlqʷː-os  ˈtːol-nː̩/
```

As formas antes do hífen são derivadas de raízes reais (§5.1); o que vem depois
é preenchimento silábico, sem valor gramatical. Repare que o preenchimento
**também concorda** — `-es` numa palavra `[−round]`, `-os` numa `[+round]`. É
essa concordância que colapsa e vira o ablaut.

Para ouvir o contraste central do sistema, o par mínimo que separa duração de
vozeamento:

| Proto-Orogeniano | → PIE clássico | sentido |
|---|---|---|
| `/ˈpːentː/` | `*pent-` | 'trilha, pisar' |
| `/ˈpent/` | `*bʰendʰ-` | 'atar' |

No Proto-Orogeniano essas duas palavras diferem **só em duração**. No PIE
clássico, depois do vozeamento e da degeminação de §3.5, elas diferem em
vozeamento e aspiração. É a mudança inteira de Kloekhorst 2016 em duas
palavras.

---

## 3 | O inventário

### 3.1 Obstruintes — três séries × sete pontos

O contraste é de **ajuste laríngeo**, não de vozeamento:

| | labial | dental | palatal | velar | labiovelar | uvular | labiouvular |
|---|---|---|---|---|---|---|---|
| **fortis** (longa) | `pː` | `tː` | `ḱː` | `kː` | `kʷː` | `qː` | `qʷː` |
| **glotalizada** (breve pré-glotalizada) | — | `ʔt` | `ʔḱ` | `ʔk` | `ʔkʷ` | `ʔq` | `ʔqʷ` |
| **lenis** (breve simples) | `p` | `t` | `ḱ` | `k` | `kʷ` | `q` | `qʷ` |

Notação: `ḱ` é a palatal(izada); `ː` marca duração fonêmica; `ʔC` marca
pré-glotalização. Total: **20 obstruintes**.

### 3.2 As duas lacunas, e por que só uma é surpreendente

A lição distingue lacunas esperadas de lacunas surpreendentes. Temos uma de
cada tipo, e elas se resolvem de modos opostos.

**A lacuna em `/ʔp/` é esperada e fica.** Em sistemas glotálicos, o membro
labial é justamente o que costuma faltar — a ejetiva labial é a mais rara das
ejetivas, transculturalmente. É essa lacuna que produz a quase-ausência de
`*b` no PIE clássico: **5 raízes em 873** no nosso dataset. Ou seja, um dos
buracos mais famosos da reconstrução indo-europeia deixa de ser anomalia e
vira consequência do sistema.

**A lacuna uvular é surpreendente, e por isso é preenchida.** No PIH
reconstrutível a coluna uvular existe **só na série fortis**: `/qː/` (= `*h₂`)
e `/qʷː/` (= `*h₃`). Não há `/q/` nem `/ʔq/`. Pela regra da própria lição
— *"if your language has voiced and unvoiced fricatives in 4 places of
articulation but only one of them in a fifth place, that's a surprising gap"*
— isso é exatamente o tipo de assimetria que não se espera.

**PROJETO.** O Proto-Orogeniano tinha a coluna uvular **completa**. As
não-fortis colapsaram durante a fase terrestre:

```
/q/, /ʔq/, /qʷ/, /ʔqʷ/   >   /ʔ/   =   *h₁
```

É a **primeira** das duas invenções estruturais do documento — a segunda é a
harmonia de §3.4 — e paga o próprio custo com três consequências verificáveis:

1. **`*h₁` ganha explicação.** Seu valor fonético é indeterminado na literatura
   (*"h ou oclusiva glotal"*) precisamente porque não é um som herdado, e sim
   o resíduo de um colapso.
2. **As 76 raízes com `H` indeterminada** — casos em que a filologia não
   decide *qual* laringal estava lá — são onde o colapso apagou a distinção.
3. A simetria se restaura: o sistema vira uma grade limpa de 3 × 7.

### 3.3 Sibilante e sonorantes

A duração não é um traço só das oclusivas. Ela atravessa o sistema:

| classe | breve | longa |
|---|---|---|
| sibilante | `s` | `sː` |
| nasais | `m` `n` | `mː` `nː` |
| líquidas | `r` `l` | `rː` `lː` |
| glides | `w` `j` | — |

A justificativa é **direta**, e mais forte do que a primeira versão deste
documento registrava. Kloekhorst (2016: 216–17) estende o contraste
explicitamente para além das oclusivas:

> *"I therefore assume that also for these fricatives and resonants, including
> ḫ(ḫ), the distinction between fortis and lenis was one in consonantal length:
> the single spelled, lenis consonants were in fact short ([s], [χ], [r], [l],
> [m], [n]), whereas the geminate spelled, fortis ones were in fact long
> ([sː], [χː], [rː], [lː], [mː], [nː])."*

O hitita grafa `š r l m n` contra `šš rr ll mm nn`, e nunca se alegou que essa
distinção fosse de voz — ao contrário do que às vezes se propôs para `ḫ`/`ḫḫ`.

*(A versão anterior justificava `/sː/` e `/mː/` pelos itens 31 e 21 da lista de
inovações — `*h₁éssi` > `*h₁ési` e `*h₁mm-` > `*h₁m-`. Essas duas geminadas são
**derivadas**: uma de fronteira de morfema, outra de assimilação de `*mn`. Elas
mostram degeminação, não contraste lexical de duração. A citação foi
corrigida.)*

Ponto extra, e relevante para §3.2: Kloekhorst inclui **`ḫ(ḫ)`** nessa lista,
isto é, `[χ]` contra `[χː]`. O sistema tolera uma uvular fortis e uma lenis —
apoio parcial à coluna uvular completa. Parcial porque no hitita a lenis `ḫ` é
**derivada** pela lenição proto-anatólia entre moras átonas (§4.4 do documento
01), e portanto não atesta diretamente uma uvular não-fortis no PIH.

Sonorantes silábicas servem de núcleo: `m̩ n̩ r̩ l̩`. E — ponto que resolve
sozinho a pobreza vocálica — **`[i]` e `[u]` são os alofones silábicos de
`/j/` e `/w/`**. É daí que saem `*i` e `*u` do PIE.

### 3.4 Vogais e harmonia

Quatro qualidades — duas alturas × duas classes — cada uma com contraste de
duração. **Oito vogais.**

| | `[−round]` | `[+round]` |
|---|---|---|
| **médias** | `e` `eː` | `o` `oː` |
| **baixas** | `a` `aː` | `ɒ` `ɒː` |

As altas `[i]` e `[u]` **não são fonemas**: são os alofones silábicos de `/j/`
e `/w/`. A prova é morfofonológica e vem do próprio PIE — `*weyd-` 'ver' tem
grau zero `*wid-`, onde o `*i` **é** o `*y` silabificado. Medido: 1 raiz com
`*i` e 7 com `*u`, em 873. Elas não ocorrem como vogal de raiz.

#### O arredondamento é um traço de raiz

Esta é a decisão estrutural da lição. O arredondamento não é propriedade de
segmentos isolados: é **harmônico**, e a raiz inteira pertence a uma classe.
Vogais e dorsais concordam; labiais, dentais, palatais e sonorantes são
neutras e ocorrem nas duas.

| classe | vogais | dorsais |
|---|---|---|
| `[−round]` | `e eː a aː` | `k kː ʔk` · `q qː ʔq` |
| `[+round]` | `o oː ɒ ɒː` | `kʷ kʷː ʔkʷ` · `qʷ qʷː ʔqʷ` |

**PROJETO — e sob revisão.** É a segunda e última invenção estrutural do
projeto; a primeira foi a coluna uvular completa (§3.2). Ela foi adotada para
pagar três dívidas. A auditoria de fontes e dados manteve uma e derrubou duas:

1. ~~**O ablaut ganha origem.**~~ **Não funciona.** A ideia era que o grau-o
   fosse o resíduo lexical da classe `[+round]`. Mas Melchert dá como
   estabelecido que o PIE tinha presentes radicais com ablaut `*ó/é` — e o
   grau-o **alterna dentro do paradigma** (hitita `karāp-`/`karēp-`), ao lado
   do tipo `*é/zero`. Uma classe harmônica de raiz prevê que a raiz mostre `o`
   *ou* `e` de forma constante; o que se atesta é alternância morfológica. Ver
   "problemas em aberto" abaixo.
2. **`*h₃` ganha razão para ser labializado** — mas é o elo mais fraco.
   `/qː/` e `/qʷː/` seriam a mesma uvular nas duas classes, e a "coloração
   laringal" viraria concordância. O teste de §4.5 mostra `*h₂` coocorrendo
   com labiovelares em 10 raízes, o que sob essa atribuição é violação.
3. **As labiovelares consonantais do PIE** (`*kʷ *gʷ *gʷʰ`) deixam de ser uma
   série avulsa e passam a ser o que sobrou da harmonia nas dorsais. **Esta
   sobrevive** — é uma propriedade lexical de raiz, exatamente o que harmonia
   explica bem, e não conflita com nada nas fontes.

#### Problemas em aberto

| Problema | Gravidade |
|---|---|
| O grau-o alterna dentro do paradigma, não por raiz (Melchert) | **estrutural** — invalida a dívida 1 |
| `*h₂` coocorre com labiovelares em 10 raízes (§4.5) | alta — a atribuição das laringais às classes não se sustenta bem |
| Sem apoio empírico: 13 raízes com duas dorsais, sem supressão detectável | média — os dados não decidem |
| `*h₁` viria do colapso de `/q ʔq/` **e** `/qʷ ʔqʷ/`, atravessando as duas classes, sem deixar traço de arredondamento | baixa — `*h₁` de fato não colore nem arredonda, o que é consistente |

**Posição atual:** a harmonia fica registrada como opção de projeto, com a
dívida 3 como única justificativa que resiste. Se o ablaut vier de acento e
apofonia — como a corrente principal sustenta — as duas contas não competem: a
harmonia explicaria as labiovelares, e o acento explicaria o ablaut.

#### A ponte para o PIH

O sistema tem que chegar ao alvo sem `/a/`. Três passos, a formalizar na
lição 4:

1. `/a/` → `/e/` e `/ɒ/` → `/o/` fora da vizinhança de uvular;
2. **junto a uvular a vogal baixa resiste.** Uvulares abaixam e recuam vogais
   adjacentes — efeito bem atestado em semítico, caucasiano noroeste,
   esquimó-aleúte e quíchua. É o que a tradição registra como a sequência
   `*h₂e`;
3. a harmonia colapsa e `[±round]` se relexicaliza (nas dorsais e no grau-o).

Isso **inverte a coloração laringal**: as laringais não colorem as vogais —
elas *protegem* a qualidade original de uma fusão que ocorreu em todo o resto.
Mesmo resultado de superfície, história mais funda. A origem do grau-o é
questão aberta na literatura, e é por isso que a vaga está livre para nós.

#### O que os dados dizem sobre `*a`

Medição sobre as 873 raízes, e o resultado separa duas populações que não se
tocam:

| | n | com `*h₂` |
|---|---|---|
| raízes com `*a` subjacente | 9 | **0** |
| raízes com `*h₂` | 181 | — (179 com `*e`, **0 com `*a`**) |

Leitura obrigatória desse zero: **a coloração é invisível nas formas de
citação**, porque a raiz é uma abstração no grau-e. O `*a` de `*h₂ent-` só
aparece nos reflexos das filhas — lat. *ante*, gr. *anti*. Então o `*a`
protegido por uvular de que trata o passo 2 **não é** o `*a` subjacente dessas
9 raízes.

E as 9 são um conjunto à parte: `kap`, `ḱad`, `kagʰ`, `h₁yaǵ`, `bak`, `smal`,
`kakka`, `skabʰ`. Formato e sentido de empréstimo, substrato e linguagem
infantil — `kakka` é literalmente a palavra que Kloekhorst descarta como
irrelevante para a reconstrução. Onde `*a` é reconstruído como subjacente no
PIE, ele cheira a não-nativo, o que é exatamente o que a nossa ponte prevê.

### 3.5 Acento

**Livre** — pode cair em qualquer sílaba, e é contrastivo. Herdado direto do
alvo: a língua-mãe tinha acento livre pelos reflexos em védico, grego,
balto-eslavo e germânico, e o lídio tinha acento tônico livre.

É o acento que condiciona a lenição — no anatólio, entre moras átonas — e é
ele que vai alimentar o ablaut. As regras ficam para a lição 3.

### 3.6 Total

```
obstruintes  20    sibilantes   2    sonorantes  10    vogais  8
TOTAL        40
```

Perfil consonante-pesado: 32 consoantes contra 8 vogais. Dos 40 fonemas, 20
são harmônicos (10 por classe) e 20 são neutros. Confere com o retrato de §1.

---

## 4 | Fonotática

As regras abaixo **não foram inventadas**: foram medidas sobre as 873 raízes
de `PIE_roots`, segmentadas e reduzidas a esqueletos.

### 4.1 O molde silábico

```
onset  (s)(C)(R)     máx. 3
núcleo  V | R̩
coda   (R)(C)(s)     máx. 3
```

Distribuição medida (raízes monossilábicas), `C` = obstruinte, `R` = sonorante,
`H` = laringal:

| onsets | n | | codas | n |
|---|---|---|---|---|
| `C` | 275 | | `RC` | 227 |
| `R` | 147 | | `R` | 164 |
| `CR` | 108 | | `C` | 127 |
| `H` | 86 | | `RH` | 124 |
| `HR` | 67 | | `H` | 68 |
| `sC` | 60 | | `Rs` | 39 |
| `s` | 38 | | `HC` | 35 |
| `sR` | 33 | | `s` | 22 |
| `RR` | 12 | | `HR` | 20 |
| `sCR` | 9 | | `CH` | 7 |
| `CC` | 5 | | `Hs` | 6 |

Leitura: o onset típico sobe em sonoridade (obstruinte → sonorante) e a coda
típica desce (sonorante → obstruinte) — o sequenciamento de sonoridade que a
lição descreve. `CC` em onset é raríssimo (5 casos).

### 4.2 A exceção do /s/

`sC` (60) e `sCR` (9) violam a sonoridade: a fricativa é mais sonora que a
oclusiva que a segue. É exatamente o caso que a lição levanta em inglês
(*"stretch"*, *"space"*). No Proto-Orogeniano, `/s/` é **extrassilábico** nas
bordas — anexa-se fora do molde, à esquerda do onset e à direita da coda
(`Rs`, 39; `Hs`, 6).

### 4.3 Formato canônico da raiz

Os esqueletos mais frequentes:

| esqueleto | n | | esqueleto | n |
|---|---|---|---|---|
| `CVRC` | 68 | | `CVC` | 30 |
| `CVRH` | 56 | | `RVC` | 23 |
| `CVR` | 53 | | `RVR` | 22 |
| `RVRC` | 43 | | `HVC` | 22 |

Todos são variações de **√CVC** com sonorantes e laringais ocupando as
posições consonantais. A raiz canônica é monossilábica, com uma única vogal
plena.

### 4.4 Restrições de coocorrência nas oclusivas

As 873 raízes dão 216 com duas ou mais oclusivas, 216 pares. Comparando o
observado com o esperado a partir da frequência de cada série entre os 423
tokens (`T` 206, `Dʰ` 136, `D` 81):

| par (leitura glotálica) | obs. | esp. | razão | Poisson p(≤obs) |
|---|---|---|---|---|
| **glotalizada × glotalizada** | **1** | 7,9 | **0,13** | **0,0032** |
| **lenis × fortis** | **19** | 67,6 | **0,28** | **< 0,0001** |
| glotalizada × lenis | 30 | 26,6 | 1,13 | — |
| glotalizada × fortis | 49 | 40,3 | 1,22 | — |
| fortis × fortis | 72 | 51,2 | 1,41 | — |
| lenis × lenis | 45 | 22,3 | 2,02 | — |

Duas restrições reais, não uma:

**1. Dissimilação glotálica.** Uma raiz em 216 onde se esperavam oito. É a
conhecida restrição do PIE contra duas oclusivas sonoras simples numa raiz.
Sob a leitura tradicional é difícil de motivar — por que proibir duas sonoras e
liberar duas surdas e duas aspiradas? Sob a leitura glotálica é banal:
dissimilação de glotalização, do tipo atestado em semítico e caucasiano.

**2. Concordância de ajuste laríngeo.** Lenis com fortis é suprimido tão forte
quanto (0,28), enquanto fortis×fortis e lenis×lenis são *sobre*-representados.
Ou seja: as raízes preferem repetir a mesma série — **exceto** a glotalizada,
que dissimila. É a outra restrição clássica do PIE (surda + aspirada sonora), e
a formulação glotálica unifica as duas num quadro coerente.

A exceção única da primeira é `*gʷeg-`.

**Este é o resultado empírico que resiste.** Ele sustenta independentemente a
leitura glotálica que o sistema de Kloekhorst exige — ao contrário da previsão
harmônica de §4.5, que não se confirma.

Regra adotada: *no máximo uma obstruinte glotalizada por raiz.*

### 4.5 Harmonia de raiz

A segunda restrição de domínio, ao lado da dissimilação glotálica. Enquanto a
dissimilação **proíbe** repetição de um traço, a harmonia **exige** repetição
de outro:

> Todos os segmentos harmônicos de uma raiz pertencem à mesma classe.

Os vinte segmentos harmônicos são os de §3.4. Os outros vinte — labiais,
dentais, palatais, `/s sː/` e as sonorantes — são neutros e não interferem.

Consequência prática: uma raiz nunca tem `/k/` e `/kʷ/` juntos, nem `/qː/` e
`/qʷː/` juntos.

#### A previsão, e o teste — que **não** confirma a hipótese

Essa consequência é testável no PIE atestado, porque a harmonia, ao colapsar,
deixaria as dorsais para trás como segmentos. Se as labiovelares do PIE são
resíduo da classe `[+round]` e as velares simples da classe `[−round]`, elas
não deveriam coocorrer numa mesma raiz.

> ⚠ **Correção.** A primeira versão desta seção anunciava "90 % de supressão"
> comparando as coocorrências observadas contra `873 × p(labiovelar) ×
> p(velar)`. Essa linha de base está **errada**: ela ignora que raízes do PIE
> raramente contêm duas dorsais. Refeito o cálculo sobre a população certa, o
> resultado desaparece. O que segue é a versão correta.

Só **13 raízes em 873** contêm duas ou mais dorsais consonantais — 17 pares no
total. Contra a frequência dos tipos entre os 438 tokens dorsais do corpus:

| par | observado | esperado | razão |
|---|---|---|---|
| labiovelar × velar simples | 2 | 3,2 | 0,62 |
| velar × velar | 9 | 4,5 | 2,01 |
| palatal × velar | 5 | 5,3 | 0,95 |
| labiovelar × labiovelar | 0 | 0,6 | — |

**Não há supressão detectável**, e com 17 pares a amostra não sustenta
conclusão em nenhuma direção. O único desvio visível é a
sobre-representação de velar × velar, que é repetição do mesmo tipo — outro
fenômeno.

Ampliando para incluir as laringais, entre as 72 raízes com duas ou mais
dorsais harmônicas, 52 (72 %) são de classe uniforme e 20 (28 %) são mistas. E
a mistura concentra-se num lugar só: **labiovelar × `*h₂`, 10 casos** — que sob
a nossa atribuição (`*h₂` = `[−round]`) é justamente a violação mais grave.

Conclusão honesta: **a harmonia não tem apoio empírico nos dados que temos**, e
a atribuição das laringais às classes opostas é o elo mais fraco da proposta.
Ver §3.4, "problemas em aberto".

Enquanto não houver morfologia derivacional, o domínio da harmonia é a palavra
inteira. Definir um domínio menor é assunto das lições 03 e 05.

### 4.6 Junção silábica

Dentro da palavra a fonotática é mais apertada que nas bordas: o aglomerado
resultante do encontro coda + onset não passa de dois segmentos, e segmentos
idênticos não se encostam (`*nnː`, `*tːt`, `*ss`).

---

## 5 | Palavras

Geradas por [`tools/po-phonology/gen.py`](../tools/po-phonology/gen.py), que
implementa §4. Saída com `--seed 4400`, curada (o gerador é uma primeira
aproximação; a tarefa 7 é justamente conferir).

O gerador sorteia uma classe harmônica por forma e filtra vogais e dorsais por
ela, de modo que a harmonia é imposta na geração, não conferida depois.

**Raízes `[−round]`:**

```
/ˈseqːtː/    /ˈtːelːt/    /ˈnaːq/
/ˈḱeq/       /ˈseːmḱ/     /ˈsteʔqp/    /ˈpːeːmː/
```

**Raízes `[+round]`:**

```
/ˈqʷːor/     /ˈkʷːɒwḱ/    /ˈkʷːolːtː/
/ˈtːol/      /ˈmɒːqʷː/
```

**Polissilábicas:**

```
[−round]   /ˈpaːstarḱː/    /ˈwakelːerːtː/    /seːˈkːwejpː/
[+round]   /ˈqʷːopːoʔqʷ/   /qʷjɒˈtːrːn̩s/     /pːoˈlɒːʔtqʷ/
```

Repare que nenhuma forma mistura `e a` com `o ɒ`, nem `k q` com `kʷ qʷ`.

### 5.1 Formas derivadas de raízes reais

Mais úteis que as geradas, porque já são material do projeto. A tabela de
correspondências que as produz:

| Proto-Orogeniano | PIH | PIE clássico |
|---|---|---|
| `pː tː ḱː kː kʷː` | idem | `*p *t *ḱ *k *kʷ` |
| `— ʔt ʔḱ ʔk ʔkʷ` | idem | `*b *d *ǵ *g *gʷ` |
| `p t ḱ k kʷ` | idem | `*bʰ *dʰ *ǵʰ *gʰ *gʷʰ` |
| `qː` | `qː` | `*h₂` |
| `qʷː` | `qʷː` | `*h₃` |
| `q ʔq qʷ ʔqʷ` | `ʔ` | `*h₁` |
| `sː mː nː rː lː` | idem | `*s *m *n *r *l` (degeminadas) |
| `e eː` / `o oː` | idem | `*e *ē` / `*o *ō` |
| `a aː` / `ɒ ɒː` | — | fundidas antes do PIH (§3.4) |

**As vogais não têm correspondência unívoca.** O colapso da harmonia e a
reorganização em graus de ablaut se interpõem, de modo que a vogal da forma
proto-orogeniana segue a **classe** da raiz, e não a vogal da citação do PIE.
Formalizar isso é o trabalho da lição 4; aqui as formas são dadas na classe
que suas dorsais exigem.

Aplicada de trás para a frente:

| PIE clássico | sentido | Proto-Orogeniano | classe |
|---|---|---|---|
| `*steh₂-` | ficar de pé | `/ˈstːeqː/` | `[−round]` |
| `*lewk-` | brilhante | `/ˈlewkː/` | `[−round]` |
| `*weyd-` | ver | `/ˈwejʔt/` | `[−round]` |
| `*bʰer-` | carregar | `/ˈper/` | `[−round]` |
| `*bʰendʰ-` | atar | `/ˈpent/` | `[−round]` |
| `*pent-` | trilha | `/ˈpːentː/` | `[−round]` |
| `*dʰeh₁-` | amamentar | `/ˈteq/` | `[−round]` |
| `*ǵenh₁-` | gerar | `/ˈʔḱenq/` | `[−round]` |
| `*h₂weh₁-` | soprar | `/ˈqːweq/` | `[−round]` |
| `*h₁eḱu-` | cavalo | `/ˈqeḱːw/` | `[−round]` |
| `*welh₃-` | golpear | `/ˈwolqʷː/` | `[+round]` |
| `*kʷekʷlos` | roda | `/ˈkʷːokʷːlos/` | `[+round]` |

Três coisas a notar.

`*h₁eḱu-` 'cavalo' sai **sem tema em `-o-`**, como exige o item 11 da lista de
inovações — a tematização é posterior à cisão, e o anatólio conserva a forma
atemática.

`*welh₃-` e `*kʷekʷlos` são os casos que mostram a não-univocidade: ambos são
citados com `*e` no PIE, mas suas dorsais (`*h₃`, `*kʷ`) são `[+round]`, então
a forma proto-orogeniana traz `/o/`. O `*e` do PIE é grau, não herança direta.

E as duas laringais nunca aparecem na mesma linha, porque não podem: `*h₂` é
`[−round]` e `*h₃` é `[+round]` — a supressão medida em §4.5.

---

## 6 | Divisão silábica

Cinco polissilábicas, pelo Princípio do Onset Máximo (M.O.P.), com a ressalva
de que o M.O.P. só se aplica quando o onset resultante for legal.

**1.** `/ˈpaːstarḱː/` `[−round]` → `[ˈpaː]σ[starḱː]σ`

```
      σ                    σ
     / \            /   /  |  \   \
    C   V          C   C   V   C   C
    p   aː         s   t   a   r   ḱː
```

O M.O.P. leva o grupo `st` inteiro para o onset da segunda sílaba — legal pela
exceção do `/s/` (§4.2), embora desça em sonoridade.

**2.** `/ˈsepːeːmːtː/` `[−round]` → `[ˈse]σ[pːeːmːtː]σ` — o M.O.P. leva `pː`
inteiro para o onset, porque `/pː/` é monofonemática (§5.3 do documento 01:
`/tː/` não é `/t/`+`/t/`).

**3.** `/kʷːroˈnqʷonː/` `[+round]` → `[kʷːron]σ[ˈqʷonː]σ`

Aqui o M.O.P. **falha**. Levar `nqʷ` inteiro para o onset daria um onset que
desce em sonoridade (nasal → oclusiva), proibido por §4.1. O `n` fica na coda
da primeira sílaba, e o acento cai na segunda. *(Forma construída à mão para o
exemplo, não saída do gerador — as demais são geradas.)*

**4.** `/seːˈkːwejpː/` `[−round]` → `[seː]σ[ˈkːwejpː]σ` — onset `kːw` sobe em
sonoridade (obstruinte → glide), legal, e o M.O.P. se aplica sem obstáculo.

**5.** `/ˈqʷːopːoʔqʷ/` `[+round]` → `[ˈqʷːo]σ[pːoʔqʷ]σ`

```
        σ                   σ
      /   \            /    |    \
     C     V          C     V     C
     qʷː   o          pː    o     ʔqʷ
```

Todas as cinco são harmonicamente uniformes: as três primeiras `[−round]` não
contêm `/o ɒ kʷ qʷ/`, e as `[+round]` não contêm `/e a k q/`.

---

## 7 | Conferência das regras

| Regra | Verificação |
|---|---|
| Onset ≤ 3, coda ≤ 3 | ✔ nenhuma forma de §5 excede |
| Sonoridade sobe no onset, desce na coda | ✔ com as exceções de `/s/` (§4.2), todas nas bordas |
| Máximo uma glotalizada por raiz | ✔ imposto pelo gerador; nenhuma forma de §5 viola |
| Sem `/ʔp/` | ✔ ausente do inventário, não filtrado depois |
| **Harmonia de raiz** | ✔ imposta na geração; 0 violações em 800 formas — mas a regra em si está sob revisão, §3.4 |
| Junção medial ≤ 2 segmentos, sem geminação acidental | ✔ validado por `_bad_juncture` |
| Acento marcado em toda forma | ✔ |

Verificação automática das três restrições de domínio sobre 800 formas geradas
(400 raízes + 400 palavras, sementes 0–399): **zero violações** de harmonia,
zero de dissimilação glotálica, zero ocorrências de `/ʔp/`.

### Conferência contra as restrições do documento 01

O teste que importa de verdade — o inventário alimenta o alvo de §9.1?

| Restrição (§9.1) | Estado |
|---|---|
| Oclusivas por duração + glotalização, não por voz | ✔ §3.1 |
| Laringais como oclusivas uvulares `/qː/`, `/qʷː/` | ✔ §3.1, coluna uvular |
| **Nenhum fonema `*a` no nó do PIH** | ✔ `/a ɒ/` existem no Proto-Orogeniano e se fundem antes do PIH — §3.4, "a ponte" |
| Acento livre condicionando lenição | ✔ §3.5 |
| `/tː/` monofonemática, distinta de `/t/`+`/t/` | ✔ §6, exemplo 2 |
| Contraste de duração em `/s/` e sonorantes | ✔ §3.3 |

| Restrição (§9.2) | Estado |
|---|---|
| Sem série de oclusivas sonoras | ✔ nenhuma sonora no inventário |
| Sem laringais fricativas | ✔ são oclusivas |
| Fonema `*a` **no PIH** | ✔ fundido antes do nó, §3.4 |

Nada em conflito. A linha do `*a` é a única que mudou de leitura: a restrição
vale no **nó do PIH**, não no Proto-Orogeniano, e o §9.4 do documento 01 já
licenciava explicitamente contrastes que colapsam antes desse nó. A redação do
§9.1 foi corrigida para dizer isso.

---

## O que fica em aberto para a lição 3

A lição 3 pede traços distintivos e notação de regras. Cinco coisas ficam
esperando por ela:

1. **A matriz de traços das obstruintes.** O contraste de três séries precisa
   de traços que o descrevam sem apelar a `[±voz]`: provavelmente `[±longo]` e
   `[±constrição glotal]`.
2. **`[±round]` como traço único de dois subsistemas.** É o mesmo traço que
   distingue `/k/` de `/kʷ/` e `/e/` de `/o/`. A lição 3 lista `[±round]` entre
   os traços disponíveis; formalizar a harmonia é escrevê-la como regra de
   espraiamento desse traço pelo domínio da raiz.
3. **`[±low]` para separar `/e o/` de `/a ɒ/`**, e a formulação do abaixamento
   uvular que protege as baixas (§3.4).
4. **As regras de alofonia.** Silabificação das sonorantes, realização de
   `/j w/` como `[i u]`, e a lenição condicionada pelo acento.
5. **A regra de assibilação.** `*-TT-` > `*-TsT-`, com `/tː/` imune por ser
   monofonemática — está reconstruída já para o PIH e precisa de formulação
   formal.

E a lição 4, mudança sonora, é onde a tabela de §5.1 deixa de ser uma tabela e
vira um conjunto de regras ordenadas, aplicável às 873 raízes e conferível
contra elas. Duas coisas ficam explicitamente adiadas para lá:

- **o colapso da harmonia** e a relexicalização de `[±round]` nas dorsais;
- **a origem do grau-o**, que é a dívida que a harmonia se propõe a pagar e que
  este documento apenas registra como hipótese.
