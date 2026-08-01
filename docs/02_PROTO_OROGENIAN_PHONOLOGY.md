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
- **Pobreza vocálica extrema.** Uma qualidade de vogal contra 32 consoantes. A
  informação lexical mora inteiramente nas consoantes, no acento e no contraste
  de duração. Palavras inteiras podem não ter vogal plena nenhuma, apoiadas em
  sonorantes silábicas.

**Comparação com línguas reais.** O perfil mais próximo é o do **Cáucaso
Noroeste** — abkhaz, ubykh — pela combinação de inventário consonantal denso,
uvulares e vocalismo mínimo. A glotalização aproxima dos sistemas ejetivos
caucasianos. E o contraste de duração consonantal fazendo trabalho lexical
lembra o finlandês ou o italiano.

Há uma coincidência agradável nisso, registrada como observação e não como
argumento: §7.4 do documento 01 diz que o indo-europeu sofreu influência de
substrato **norte-caucasiano** ao chegar à estepe. Uma língua com esse perfil
não teria soado estrangeira ali.

**O que ela não é.** Não é fluida, não é melodiosa, não é vocálica. Não tem
tom. Não tem nasais vocálicas, retroflexas, cliques nem faringais.

---

## 2 | Amostra sonora

Arranjo fonoestético, **não uma frase analisada** — a morfologia é assunto das
lições 03 e 05, e nenhuma decisão morfológica foi tomada ainda:

```
/ˈqːweq  ˈstːeqː  wejˈʔt-es  ˈlewkː-mn̩  pːenˈtː-eres/
```

As formas antes do hífen são derivadas de raízes reais (§5.1); o que vem depois
é preenchimento silábico, sem valor gramatical.

Para ouvir o contraste central do sistema, o par mínimo que separa duração de
vozeamento:

| Proto-Orogeniano | → PIE clássico | sentido |
|---|---|---|
| `/ˈpːentː/` | `*pent-` | 'trilha, pisar' |
| `/ˈpent/` | `*bʰendʰ-` | 'atar' |

No Proto-Orogeniano essas duas palavras diferem **só em duração**. No PIE
clássico, depois do vozeamento e da degeminação de §5.1, elas diferem em
vozeamento e aspiração. É a mudança inteira de Kloekhorst 2016 em duas
palavras.

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

### 3.1b O mesmo inventário em IPA

A tabela acima usa a notação da indo-europeística, que é a certa para o
trabalho comparativo mas **não é IPA** — o enunciado da lição pede IPA, e a
diferença não é cosmética: `ḱ` não existe no alfabeto fonético.

| | labial | dental | palatal | velar | labiovelar | uvular | labiouvular |
|---|---|---|---|---|---|---|---|
| **fortis** | `/pː/` | `/tː/` | `/cː/` | `/kː/` | `/kʷː/` | `/qː/` | `/qʷː/` |
| **glotalizada** | — | `/ˀt/` | `/ˀc/` | `/ˀk/` | `/ˀkʷ/` | `/ˀq/` | `/ˀqʷ/` |
| **lenis** | `/p/` | `/t/` | `/c/` | `/k/` | `/kʷ/` | `/q/` | `/qʷ/` |

| classe | IPA |
|---|---|
| sibilante | `/s/` `/sː/` |
| nasais | `/m/` `/mː/` `/n/` `/nː/` |
| líquidas | `/r/` `/rː/` `/l/` `/lː/` |
| glides | `/w/` `/j/` |
| vogais | `/e/` `/eː/` |
| núcleos silábicos | `[m̩]` `[n̩]` `[r̩]` `[l̩]` `[i]` `[u]` |

Duas notas de tradução:

- **`ḱ` → `/c/`.** A série "palatal" da indo-europeística é oclusiva palatal em
  IPA. Alguns a reconstroem antes como palatalizada, `/kʲ/`; nada no projeto
  depende da escolha.
- **`ʔC` → `/ˀC/`.** Pré-glotalização se nota com o diacrítico sobrescrito
  antes do segmento. A notação `ʔt` do restante do documento segue Kloekhorst
  2016, que é a fonte do sistema.

#### Carta vocálica

```
      anterior   central   posterior
alto        i                    u      ← alofones de /j/ /w/
médio       e ────────────────────
baixo
```

Uma única posição preenchida fonemicamente. `[i]` e `[u]` aparecem na carta
porque ocorrem foneticamente, mas são alofones silábicos (§3.4).

### 3.2 As duas lacunas, e por que só uma é surpreendente

A lição distingue lacunas esperadas de lacunas surpreendentes. Temos uma de
cada tipo, e elas se resolvem de modos opostos.

**A lacuna em `/ʔp/` é esperada e fica.** Em sistemas glotálicos o membro
labial é **o mais frágil dos pontos centrais** — medido no BDPROTO, falta em
32 % das protolínguas com série ejetiva, contra 6 % para o velar (§3.7). É essa lacuna que produz a quase-ausência de
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

É a **única invenção estrutural** que sobrou no documento, e paga o próprio
custo com três consequências verificáveis:

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

### 3.4 Vogais

**Uma qualidade, duas durações.**

| | |
|---|---|
| **média anterior** | `e` `eː` |

Sistema radical, e é o que as fontes sustentam para este estágio. Kloekhorst
reduz os seis paradigmas de acento-ablaut do PIE tardio a **três do PIE
inicial**, e observa que neles

> *"all forms show only one morpheme that is accented and at the same time
> shows \*e-grade, whereas all other morphemes are unaccented and show
> zero-grade."*

Ou seja: no estágio anterior ao PIH, o vocalismo é **`/e/` acentuado contra
grau zero**. Tudo o mais é derivado e posterior.

#### As qualidades que não são fonemas

| forma | estatuto | origem |
|---|---|---|
| `[o]` | derivado, posterior | perda de acento sobre `*e` — a *Abtönung* de Brugmann: *"mit dem Zurücktreten des Tons die Umfärbung von ē̆ zu ō̆ im Zusammenhang stand"*. E, diante de `*-m` final, a lei pré-PIE `*-ē̆m` > `*-ō̆m` (Kloekhorst 2024) |
| `[a]` | **não existe** | Kloekhorst rejeita `*a` e `*ā` para o PIE — *"I myself do not see any good reason for reconstructing the vowels \*a and \*ā for PIE"* — e reanalisa os casos clássicos com `*h₂`: 'sal' é `*sh₂-ḗl / *sh₂-él-m / *sh₂-l-és`, não `*sāl` |
| `[i]` `[u]` | alofones silábicos | de `/j/` e `/w/`; `*weyd-` 'ver' tem grau zero `*wid-`, onde o `*i` **é** o `*y` silabificado. Medido: 1 raiz com `*i`, 7 com `*u`, em 873 |
| `m̩ n̩ r̩ l̩` | núcleos alternativos | sonorantes silábicas (§3.3) |

Duas leis independentes derivam `[o]` de `*e`, e as duas são condicionadas —
uma pelo acento, outra pelo contexto segmental. Nenhuma delas precisa de um
`/o/` fonêmico no estágio anterior.

#### Onde a carga funcional mora

Um sistema de uma vogal é tipologicamente extremo, e a lição avisa que a
maioria das línguas fica entre 5 e 8. Mas a lição também diz, duas vezes, que
*"these generalities are not rules"*. Aqui não se quebra por gosto: o alvo
obriga, e a informação lexical se distribui em quatro lugares —

1. o **acento livre**, que é contrastivo (§3.5);
2. o **grau zero**, que faz alternância morfológica sem material vocálico;
3. as **sonorantes silábicas** como núcleos;
4. o **contraste de duração** nas consoantes, que carrega o peso lexical.

#### Nota histórica: a harmonia descartada

Uma versão anterior deste documento deu ao Proto-Orogeniano quatro qualidades
em duas classes harmônicas (`/e a/` ~ `/o ɒ/`), com o arredondamento como
traço de raiz. A proposta pagava três dívidas. A auditoria contra as fontes
primárias derrubou as três:

| dívida | o que a derrubou |
|---|---|
| o grau-o seria resíduo da classe `[+round]` | **no PIE inicial o grau-o não existe** — o vocalismo é `*e` acentuado contra zero. Não há o que explicar. E onde `*o` surge, ele **alterna dentro do paradigma** (hit. `karāp-`/`karēp-`), o que uma classe lexical de raiz não produz |
| `*h₃` ganharia razão para ser labializado | não precisa de harmonia: é o membro labializado da série uvular, exatamente como `*kʷ` está para `*k`. A coloração é assimilação comum — `*h₂` recua e abaixa sem arredondar, `*h₃` recua e arredonda |
| as labiovelares consonantais deixariam de ser série avulsa | elas são simplesmente uma série labializada, que não pede explicação; e o teste de coocorrência não mostra supressão (§4.5) |

A proposta era testável e foi testada. Fica registrada aqui porque o registro
do que se descartou, e por quê, vale tanto quanto o do que se manteve.

### 3.5 Acento

**Livre** — pode cair em qualquer sílaba, e é contrastivo. Herdado direto do
alvo: a língua-mãe tinha acento livre pelos reflexos em védico, grego,
balto-eslavo e germânico, e o lídio tinha acento tônico livre.

É o acento que condiciona a lenição — no anatólio, entre moras átonas — e é
ele que vai alimentar o ablaut. As regras ficam para a lição 3.

### 3.6 Total

```
obstruintes  20    sibilantes   2    sonorantes  10    vogais  2
TOTAL        34
```

Perfil consonante-pesado ao extremo: **32 consoantes contra 2 vogais**. Confere
com o retrato de §1.

### 3.7 Conferência tipológica

A lição manda checar o inventário contra o que as línguas do mundo fazem, e
aponta o WALS e o PHOIBLE. O repositório tem o **BDPROTO** em `data/`, que é a
comparação certa: **229 protolínguas reconstruídas**, não línguas vivas. Isto
é, o mesmo tipo de objeto que o Proto-Orogeniano.

| medida | BDPROTO | nós | veredito |
|---|---|---|---|
| consoantes | mediana 20 | **32** | percentil 86 — grande, mas normal |
| **qualidades vocálicas** | mediana 5 | **1** | ver abaixo |
| tem uvulares | 17 % | sim | incomum, mas atestado |
| tem consoantes longas | 13,5 % | sim | incomum, mas atestado |
| tem ejetivas/glotalizadas | 16 % | sim | incomum, mas atestado |
| **sem** contraste de voz nas oclusivas | **37 %** | sim | inteiramente banal |

**O perfil consonantal existe.** Uvulares + longas + glotalizadas nas três ao
mesmo tempo: proto-neocaledônio, acádio, sul-arábico antigo. Uvulares +
glotalizadas, sem a duração: proto-atabascano, proto-kartveliano, proto-maia,
proto-salish, proto-pomo, egípcio médio. Não estamos inventando uma combinação
impossível.

**O vocalismo é o ponto extremo, e é preciso dizer sem maquiagem.** Em 229
protolínguas do BDPROTO, **uma única** tem uma só qualidade vocálica
(proto-tsimshian) e **nenhuma** tem duas. Estamos sozinhos numa amostra de 229.

Isso não invalida o sistema — ele é o que a reconstrução do estágio pré-PIH
força (§3.4), e a carga funcional está no acento, no grau zero e nas
sonorantes silábicas. Mas fica registrado como **o traço mais arriscado do
inventário**, e o primeiro a revisar se a lição 4 mostrar que as regras não
fecham.

#### A lacuna labial, testada

O §3.2 afirma que em sistemas glotálicos "o membro labial é o que costuma
faltar". Medido nas 34 protolínguas do BDPROTO com série ejetiva de dois ou
mais membros:

| ponto sem ejetiva | n | % |
|---|---|---|
| uvular | 24 | 71 % |
| **labial** | **11** | **32 %** |
| velar | 2 | 6 % |

A afirmação **se sustenta na direção certa mas estava forte demais**: entre os
pontos centrais, o labial falta cinco vezes mais que o velar — é o elo frágil.
Mas dois terços dos sistemas ejetivos *têm* a labial, então "costuma faltar"
vira "**é o mais frágil dos pontos centrais**". A redação de §3.2 foi ajustada.

(O uvular falta mais que todos, mas isso só reflete que uvulares são raras em
geral, não fragilidade da glotalização nesse ponto.)

#### Um controle externo que saiu a favor

O BDPROTO traz o hitita a partir da gramática de Hoffner & Melchert (2008). O
inventário consonantal listado é:

```
k kː  kʷ kʷː  l lː  m mː  n nː  p pː  r rː  s sː  t tː  ts tsː  w wː  hː  j jː
```

Contraste de duração atravessando oclusivas, sonorantes, sibilante e a
laringal — e **nenhuma oclusiva sonora no inventário**. É exatamente o que
§3.3 afirma citando Kloekhorst 2016, agora confirmado por uma fonte
independente e de referência.

Nota lateral: a entrada do próprio PIE no BDPROTO (a partir de Fortson 2011)
lista `pʼ tʼ kʼ kʷʼ` — ejetivas. A leitura glotálica que adotamos não é
excêntrica.

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

### 4.5 Junção silábica

Dentro da palavra a fonotática é mais apertada que nas bordas: o aglomerado
resultante do encontro coda + onset não passa de dois segmentos, e segmentos
idênticos não se encostam (`*nnː`, `*tːt`, `*ss`).

---

## 5 | Palavras

Geradas por [`tools/po-phonology/gen.py`](../tools/po-phonology/gen.py), que
implementa §4. Saída com `--seed 4400`, curada (o gerador é uma primeira
aproximação; a tarefa 7 é justamente conferir).

**Raízes:**

```
/ˈkːen/      /ˈʔke/       /ˈkrenː/     /ˈsmeqʷː/
/ˈkʷːelk/    /ˈqenːpː/    /ˈʔkeːtː/    /ˈpeḱːqː/
/ˈkʷmew/     /ˈmːeːmḱː/
```

**Polissilábicas:**

```
/seˈkʷenq/       /ˈsepːeːmːtː/    /kʷːreˈnqʷenː/   /rːeˈrqʷes/
/ˈlːerjesḱekː/   /ˈskʷemːejkː/    /weˈtelːʔk/      /ʔkʷeˈqʷn̩tːejpː/
```

Repare em `/sr̩ˈkːl̩lpː/` e `/ˈpm̩qːenqʷ/`, também da saída bruta: palavras sem
nenhuma vogal plena, apoiadas só em sonorantes silábicas. É o efeito de §3.4
levado ao limite, e é legal pelo molde.

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
| `e eː` | idem | `*e *ē` |
| — | — | `*o *ō` são **derivados**: perda de acento, e `*-ē̆m` > `*-ō̆m` (§3.4) |
| `Ø` | `Ø` | grau zero, em sílaba átona |

**As vogais não têm correspondência unívoca.** Onde o PIE cita `*o`, o
Proto-Orogeniano tem `/e/`: o grau-o é posterior e condicionado. Formalizar as
duas leis que o produzem é trabalho da lição 4.

Aplicada de trás para a frente:

| PIE clássico | sentido | Proto-Orogeniano |
|---|---|---|
| `*steh₂-` | ficar de pé | `/ˈstːeqː/` |
| `*lewk-` | brilhante | `/ˈlewkː/` |
| `*weyd-` | ver | `/ˈwejʔt/` |
| `*bʰer-` | carregar | `/ˈper/` |
| `*bʰendʰ-` | atar | `/ˈpent/` |
| `*pent-` | trilha | `/ˈpːentː/` |
| `*dʰeh₁-` | amamentar | `/ˈteq/` |
| `*ǵenh₁-` | gerar | `/ˈʔḱenq/` |
| `*h₂weh₁-` | soprar | `/ˈqːweq/` |
| `*h₁eḱu-` | cavalo | `/ˈqeḱːw/` |
| `*welh₃-` | golpear | `/ˈwelqʷː/` |
| `*kʷekʷlos` | roda | `/ˈkʷːekʷːles/` |

Três coisas a notar.

`*h₁eḱu-` 'cavalo' sai **sem tema em `-o-`**, como exige o item 11 da lista de
inovações — a tematização é posterior à cisão, e o anatólio conserva a forma
atemática.

`*kʷekʷlos` 'roda' mostra a não-univocidade: os dois `*o` da forma do PIE — o
do radical e o da desinência temática `*-os` — não estão no Proto-Orogeniano.
Ambos surgem depois, por perda de acento e pela lei `*-ē̆m` > `*-ō̆m`.

E `*h₂` (`/qː/`) e `*h₃` (`/qʷː/`) são a mesma uvular, plana e labializada,
exatamente como `*k` está para `*kʷ`. A coloração que cada uma causa é
assimilação comum: `*h₂` recua e abaixa sem arredondar, `*h₃` recua e
arredonda.

---

## 6 | Divisão silábica

Cinco polissilábicas, pelo Princípio do Onset Máximo (M.O.P.), com a ressalva
de que o M.O.P. só se aplica quando o onset resultante for legal.

**1.** `/seˈkʷenq/` → `[se]σ[ˈkʷenq]σ`

```
      σ              σ
     / \          /  |  \
    C   V        C   V   C C
    s   e        kʷ  e   n q
```

**2.** `/ˈsepːeːmːtː/` → `[ˈse]σ[pːeːmːtː]σ` — o M.O.P. leva `pː` inteiro para
o onset, porque `/pː/` é monofonemática (§5.3 do documento 01: `/tː/` não é
`/t/`+`/t/`).

```
      σ                    σ
     / \            /   /  |  \
    C   V          C   V   C   C
    s   e          pː  eː  mː  tː
```

**3.** `/kʷːreˈnqʷenː/` → `[kʷːren]σ[ˈqʷenː]σ`

```
        σ                σ
    /  /  \  \        /  |  \
   C  C   V   C      C   V   C
   kʷː r   e   n     qʷ  e   nː
```

Aqui o M.O.P. **falha**. Levar `nqʷ` inteiro para o onset daria um onset que
desce em sonoridade (nasal → oclusiva), proibido por §4.1. O `n` fica na coda
da primeira sílaba, e o acento cai na segunda.

**4.** `/rːeˈrqʷes/` → `[rːer]σ[ˈqʷes]σ` — mesma razão: `rqʷ` não é onset
legal.

```
       σ              σ
    /  |  \        /  |  \
   C   V   C      C   V   C
   rː  e   r      qʷ  e   s
```

**5.** `/ˈlːerjesḱekː/` → `[ˈlːer]σ[jes]σ[ḱekː]σ`

```
       σ            σ           σ
    /  |  \      /  |  \     /  |  \
   C   V   C    C   V   C   C   V   C
   lː  e   r    j   e   s   ḱ   e   kː
```

---

## 7 | Conferência das regras

| Regra | Verificação |
|---|---|
| Onset ≤ 3, coda ≤ 3 | ✔ nenhuma forma de §5 excede |
| Sonoridade sobe no onset, desce na coda | ✔ com as exceções de `/s/` (§4.2), todas nas bordas |
| Máximo uma glotalizada por raiz | ✔ imposto pelo gerador; nenhuma forma de §5 viola |
| Sem `/ʔp/` | ✔ ausente do inventário, não filtrado depois |
| Junção medial ≤ 2 segmentos, sem geminação acidental | ✔ validado por `_bad_juncture` |
| Acento marcado em toda forma | ✔ |

Verificação automática sobre 800 formas geradas (400 raízes + 400 palavras,
sementes 0–399): zero violações de dissimilação glotálica, zero ocorrências de
`/ʔp/`.

### Conferência contra as restrições do documento 01

O teste que importa de verdade — o inventário alimenta o alvo de §9.1?

| Restrição (§9.1) | Estado |
|---|---|
| Oclusivas por duração + glotalização, não por voz | ✔ §3.1 |
| Laringais como oclusivas uvulares `/qː/`, `/qʷː/` | ✔ §3.1, coluna uvular |
| **Nenhum fonema `*a`** | ✔ ausente do inventário, e Kloekhorst rejeita `*a` para o PIE por completo — §3.4 |
| Acento livre condicionando lenição | ✔ §3.5 |
| `/tː/` monofonemática, distinta de `/t/`+`/t/` | ✔ §6, exemplo 2 |
| Contraste de duração em `/s/` e sonorantes | ✔ §3.3 |

| Restrição (§9.2) | Estado |
|---|---|
| Sem série de oclusivas sonoras | ✔ nenhuma sonora no inventário |
| Sem laringais fricativas | ✔ são oclusivas |
| Fonema `*a` | ✔ ausente |

Nada em conflito.

### As sete tarefas do enunciado

| # | Tarefa | Onde | Estado |
|---|---|---|---|
| 1 | Como a língua deve soar | §1 | ✔ |
| 2 | Transcrever uma frase | §2 | ✔ transcrita; **gravação não feita** — o enunciado a dispensa ("the transcription will be enough") |
| 3 | Tabela IPA e carta vocálica | §3.1b | ✔ |
| 4 | Definir regras silábicas | §4 | ✔ |
| 5 | Inventar palavras | §5 | ✔ |
| 6 | Desmontar as sílabas de 5 delas | §6 | ✔ cinco, com árvore em quatro |
| 7 | Conferir as regras | §7 | ✔ |

Além do enunciado, a lição recomenda checar o inventário contra bases
tipológicas (§3.7) — feito contra o BDPROTO.

**Fica pendente, e é da lição 3, não desta:** o **inventário fonético**. A
lição 2 distingue inventário fonêmico de fonético e observa que vale a pena
construir o segundo justamente quando "you are not just documenting a snapshot
of the language ... and want to have it evolve further down the line" — que é
exatamente o nosso caso. Alofonia e realizações ficam para a lição 3, junto com
a matriz de traços.

---

## O que fica em aberto para a lição 3

A lição 3 pede traços distintivos e notação de regras. Quatro coisas ficam
esperando por ela:

1. **A matriz de traços das obstruintes.** O contraste de três séries precisa
   de traços que o descrevam sem apelar a `[±voz]`: provavelmente `[±longo]` e
   `[±constrição glotal]`.
2. **As regras de alofonia.** Silabificação das sonorantes, realização de
   `/j w/` como `[i u]`, e a lenição condicionada pelo acento.
3. **A regra de assibilação.** `*-TT-` > `*-TsT-`, com `/tː/` imune por ser
   monofonemática. Melchert confirma que a regra é compartilhada entre PIE e
   anatólio — hit. `/eːdten/` → `ēz(zaš)ten` `[eːtsten]` — e registra que não
   conhece **nenhuma** regra fonológica sincrônica do PIE que seja
   demonstravelmente inovação não-anatólia.
4. **A regra de perda de vogal átona**, que é o que produz o grau zero e,
   portanto, o motor do sistema inteiro (§3.4).

E a lição 4, mudança sonora, é onde a tabela de §5.1 deixa de ser uma tabela e
vira um conjunto de regras ordenadas, aplicável às 873 raízes e conferível
contra elas. Duas leis já estão identificadas e esperando formulação:

- **Abtönung** — `*e` átono → `*o` (Brugmann; a origem do grau-o);
- **`*-ē̆m` > `*-ō̆m`** — coloração diante de `*-m` final (Kloekhorst 2024).

---

## Apêndice | O que as fontes entregam para as lições 04 e 05

Registro antecipado, porque saiu da mesma leitura e se perde se não for
anotado. Kloekhorst reconstrói, para um **pré-estágio do PIE**, um sistema
nominal com estas propriedades:

- **alinhamento ergativo** — o caso central é o **absolutivo**;
- **inventário de casos governado por animacidade**: casos centrais disponíveis
  para todos os nomes (absolutivo, i-locativo, Ø-locativo, instrumental) contra
  casos **restritos a animados** (acusativo, dativo, alativo, "ablativo");
- apenas **duas classes acentuais**: estática e móvel;
- na flexão móvel, **proterodinâmico = inanimado** e **hisserodinâmico =
  animado**;
- os seis paradigmas de acento-ablaut do PIE tardio reduzem-se a **três** do
  PIE inicial.

Isso confirma e amplia bastante duas linhas do §9.1 do documento 01 — "dois
gêneros, animado/inanimado" e "alinhamento sensível a animacidade" — e é o
ponto de partida pronto para a morfologia nominal do Proto-Orogeniano.
