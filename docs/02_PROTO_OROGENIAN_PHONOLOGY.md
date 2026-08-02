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
lições 03 e 05, e nenhuma decisão morfológica foi tomada ainda. Todas as formas
são léxico real retro-construído (§5.1), nenhuma é preenchimento:

```
/ˈqːner   ˈʔkʷen   ˈʔte.ru   ˈwe.ʔtr̩   ˈse.qːl̩   ˈpːe.kːu/
  homem    mulher   árvore     água       sal        rebanho
```

Uma versão anterior desta amostra usava três formas inventadas com sufixos sem
valor gramatical (`-es`, `-mn̩`, `-eres`). Foram trocadas: se a língua é
definida por retro-construção, não há razão para preencher sílabas à mão.

Para ouvir o contraste central do sistema, o par mínimo que separa duração de
vozeamento:

| Proto-Orogeniano | → PIE clássico | sentido |
|---|---|---|
| `/ˈpːentː/` | `*pent-` | 'trilha, pisar' |
| `/ˈpent/` | `*bʰendʰ-` | 'atar' |

No Proto-Orogeniano essas duas palavras diferem **só em duração**. No PIE
clássico, depois do vozeamento e da degeminação de §5.2, elas diferem em
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
| vogais | `/e/` |
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

A duração não é um traço só das oclusivas. Ela atravessa **todo o
consonantismo**:

| classe | breve | longa |
|---|---|---|
| sibilante | `s` | `sː` |
| nasais | `m` `n` | `mː` `nː` |
| líquidas | `r` `l` | `rː` `lː` |
| glides | `w` `j` | — |
| **vogais** | `e` | **— (§3.4)** |

E para exatamente aí. `[±long]` é traço **consonantal** no Proto-Orogeniano:
as vogais não o exercem, e por isso a matriz do documento 03 dá à vogal
`long=0` — inaplicável — e não `[−long]`.

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

**Uma qualidade, uma duração. Uma vogal.**

| | |
|---|---|
| **média anterior** | `e` |

> **Executado.** Este documento registrava até aqui duas vogais (`/e eː/`) e uma
> proposta pendente de reduzi-las a uma. O documento 04 §8.3 mediu a proposta
> sobre o corpus de formas flexionadas e ela passou: dos **867 lemas**, nenhum
> tem duração vocálica invariável — 592 alternam longa~curta dentro do próprio
> paradigma, 275 não têm nenhuma longa, e **zero** são só-longa. Não há item
> lexical no PIE que exija duração subjacente.
>
> A medição também **corrigiu o mecanismo**. A versão anterior atribuía a
> duração ao alongamento compensatório por perda de laringal; esse caminho
> responde por **2 %** das formas longas. A fonte dominante é **contração em
> fronteira de morfema** — o subjuntivo é 17× mais longo que a linha de base,
> porque `*-e/o-` + `*-e-` contraem. É fusão, não alongamento compensatório.

As três fontes de duração vocálica do PIE, por peso:

| fonte | mecanismo | peso |
|---|---|---|
| contração em fronteira de morfema | fusão | dominante |
| perda de laringal | alongamento compensatório | 2 % |
| Lei de Szemerényi (`*-s` perdido) | alongamento compensatório | minoritária |

Nenhuma delas precisa de `/eː/` no estágio anterior. E a primeira **não é uma
questão de fonologia**: ela exige que o Proto-Orogeniano tenha temas
terminados em vogal e desinências iniciadas por vogal — restrição de
morfologia, que passa às lições 5 e seguintes.

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
| `[o]` | derivado, posterior | perda de acento sobre `*e` — a *Abtönung* de Brugmann: *"mit dem Zurücktreten des Tons die Umfärbung von ē̆ zu ō̆ im Zusammenhang stand"*. E, diante de `*-m` final, a lei pré-PIE `*-ē̆m` > `*-ō̆m` (Kloekhorst 2024). **As duas medidas em separado — documento 04 §8.2** |
| `[eː]` `[oː]` | derivados, posteriores | contração em fronteira de morfema (dominante), perda de laringal, Lei de Szemerényi. Nenhum lema do corpus tem duração invariável — §3.4 acima |
| `[a]` | **não existe** | Kloekhorst rejeita `*a` e `*ā` para o PIE — *"I myself do not see any good reason for reconstructing the vowels \*a and \*ā for PIE"* — e reanalisa os casos clássicos com `*h₂`: 'sal' é `*sh₂-ḗl / *sh₂-él-m / *sh₂-l-és`, não `*sāl` |
| `[i]` `[u]` | alofones silábicos | de `/j/` e `/w/`; `*weyd-` 'ver' tem grau zero `*wid-`, onde o `*i` **é** o `*y` silabificado. Medido: 1 raiz com `*i`, 7 com `*u`, em 873 |
| `m̩ n̩ r̩ l̩` | núcleos alternativos | sonorantes silábicas (§3.3) |

Duas leis independentes derivam `[o]` de `*e`, e as duas são condicionadas —
uma pelo acento, outra pelo contexto segmental. Nenhuma delas precisa de um
`/o/` fonêmico no estágio anterior.

E porque são condicionadas por coisas diferentes, deixam **rastros
ortogonais** — o que as torna separáveis no corpus. O documento 04 §8.2 mede
as duas: fora do contexto `_m`, `*o` é 3,5× mais propenso a ser átono que `*e`
(*Abtönung*); dentro dele, o efeito do acento **desaparece** e `*o` fica tão
tônico quanto `*e` (79,3 % contra 80,1 %), que é a assinatura de uma lei
segmental. Não era desenho: as duas leis vieram das fontes, e a separação
apareceu na medição.

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
obstruintes  20    sibilantes   2    sonorantes  10    vogais  1
TOTAL        33
```

Perfil consonante-pesado ao extremo: **32 consoantes contra 1 vogal**. Confere
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
lição descreve.

#### O molde é do morfema, não da palavra

> ⚠ **Corrigido.** Esta seção declarava o molde acima e, logo abaixo, media
> uma distribuição que ele **não gera** — `RR` (12), `CC` (5) em onset, `HC`
> (35) e `CH` (7) em coda. O molde tem um vão de obstruinte só. As margens de
> duas obstruintes estavam medidas e não estavam licenciadas, e o
> `syllabify.py` remendou isso com uma lista escrita à mão.

Medido sobre as 34.658 formas flexionadas de
[`data/derived/po_formas.tsv.gz`](../data/derived/po_formas.tsv.gz) —
182.234 margens:

| camada | margens | % |
|---|---|---|
| **molde nuclear** `(s)(C)(R)` / `(R)(C)(s)` | 173.135 | **95,0 %** |
| **+ apêndice `H`** na borda externa (§4.2) | 6.077 | 3,3 % |
| **+ juntura de morfema** (margem medial, §4.5) | 506 | 0,3 % |
| resíduo | 2.516 | 1,4 % |

O molde acima é, portanto, o molde do **morfema** — descreve a raiz e o afixo,
e é o que o gerador impõe. A palavra é mais frouxa que o morfema, porque a
morfologia concatena. Isso não é peculiaridade nossa: é a razão de o inglês ter
`sixths` `[sɪksθs]` sem que `[ksθs]` seja um molde de coda do inglês.

**A evidência de que a folga é de juntura, não de raiz:** das margens que o
molde nuclear não gera, entre **81 % e 100 % são mediais na palavra** —
`RR` 88 %, `HC` 92 %, `CH` 83 %, `CC` 81 %, `HH` 100 %. E as ilegais que são
finais vêm de desinência consonantal colada a tema terminado em consoante:
`*teh₂h₁` (dual `*-h₁`), `*-swedʰh₂` (`*-dʰh₂`), `*-esh₁`.

**`máx. 3` é uma tendência, não um teto.** No corpus, 99,8 % dos onsets e
99,9 % das codas têm três segmentos ou menos; o resto chega a cinco
(`/pːqːstːqːer/`).

**O resíduo de 1,4 %** é nomeável: coda `sCH` (879, de `*-sdʰh₂`), onset `CC`
(349) e `CH` (297), e o tipo `CHC` de `*ph₂tḗr` 'pai' (279) — este último
genuinamente interno ao morfema, e a única falha real do molde.

### 4.2 As duas exceções: `/s/` e `H`

`sC` (60) e `sCR` (9) violam a sonoridade: a fricativa é mais sonora que a
oclusiva que a segue. É exatamente o caso que a lição levanta em inglês
(*"stretch"*, *"space"*). No Proto-Orogeniano, `/s/` é **extrassilábico** nas
bordas — anexa-se fora do molde, à esquerda do onset e à direita da coda
(`Rs`, 39; `Hs`, 6).

**A coluna uvular faz o mesmo, e isso faltava.** Medido sobre os segmentos em
margem nas 34.658 formas:

| classe | em margem | em margem que o molde nuclear não gera | enriquecimento |
|---|---|---|---|
| `H` | 30.371 | 34,7 % | **1,82×** |
| `C` | 48.253 | 23,6 % | 1,24× |
| `R` | 51.627 | 10,2 % | 0,54× |
| `s` | 22.519 | **8,6 %** | **0,45×** |

O `/s/` é o segmento que **menos** aparece em margem irregular — porque esta
seção já lhe deu saída. O `H` é o que mais aparece, e nunca teve. A correção é
tratá-los igual:

> `/s/` e `H` são **extrassilábicos** nas bordas da margem — à esquerda no
> onset, à direita na coda.

Isso tem nome na literatura, e chegamos a ele pelos dados antes de o encontrar.
Ewen & van der Hulst (*The Phonological Structure of Words*, §3.4) dão à sílaba
a estrutura:

```
σ:   prependix — onset — rima — apêndice (ESP)
                         núcleo  coda
```

**Prependix** é o material extrassilábico à esquerda, **apêndice** o da
direita. É exatamente a geometria que a medição impôs. O `/s/` do
Proto-Orogeniano é prependix no onset e apêndice na coda; o `H` faz o mesmo.

A geometria importa e não é decorativa. Retirar `H` do **meio** da margem
licenciaria a coda `HR` de `/seqːl/` 'sal', que sobe em sonoridade — e é
justamente a ilegalidade dessa coda que força o `/l/` a virar núcleo,
`[ˈse]σ[qːl̩]σ` (§6). O apêndice ancora na borda externa ou a regra se
autodestrói.

Motivação independente: `H` é a única obstruinte `[+low]` do sistema
(documento 03 §2), isto é, uma classe natural de **um traço só**. Não é um
recorte inventado para salvar o molde.

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

### 4.5 Peso silábico

Ewen & van der Hulst (§3.4) definem peso por **ramificação da rima**: pesada é
a sílaba cuja rima tem mais de um segmento. No Proto-Orogeniano isso simplifica
de um jeito que nenhuma outra língua permite — como não há vogal longa (§3.4)
nem ditongo no núcleo, o núcleo é **sempre** de um segmento. Logo:

> **Sílaba pesada = sílaba com coda.** Não há terceira possibilidade.

E isso torna a pergunta testável. O acento é livre (§3.5); é livre *mesmo*, ou
é sensível a peso? Medido sobre as 34.658 formas classificadas, contando só as
que trazem acento marcado:

| | sílabas | tônicas | % |
|---|---|---|---|
| **pesada** (com coda) | 34.880 | 17.604 | **50,5 %** |
| **leve** (sem coda) | 45.165 | 11.953 | **26,5 %** |

**Razão de chances 2,83.** E o efeito não é artefato de "o acento cai na
primeira sílaba": excluindo a inicial, pesadas ficam em 47,9 % contra 29,0 %
das leves.

O acento do Proto-Orogeniano é livre quanto à posição, mas **atraído por
peso**. Isso não estava no documento e não é decorativo: é o elo que faltava
entre a fonotática e o ablaut, já que o grau zero é condicionado por acento
(documento 04 §8.2).

### 4.6 Junção silábica

Segmentos idênticos não se encostam (`*nnː`, `*tːt`, `*ss`) — nem entre
sílabas nem dentro da mesma margem, e é `_repeated()` que impõe isso no
gerador (§7).

Quanto ao tamanho, esta seção dizia que o encontro coda + onset "não passa de
dois segmentos". Isso vale para o que o **gerador** produz, e é uma escolha
conservadora dele; **não** vale para a língua. É na juntura que aparecem as
margens de duas obstruintes que o molde nuclear não gera (§4.1), e elas são
81–100 % mediais justamente por isso.

A regra correta, então, é assimétrica: o molde nuclear de §4.1 governa o
morfema; a juntura tolera o que a concatenação produzir, dentro do teto de
três segmentos que 99,8 % das margens respeitam.

---

## 5 | Palavras

Uma versão anterior desta seção abria com dez formas do gerador. Estavam
erradas de método: uma palavra sorteada é legal pelo molde e mais nada, e
não há como conferi-la contra coisa alguma. **O material primário desta seção
passou a ser léxico real retro-construído** — palavras do PIE invertidas pela
tabela de §5.2, onde cada forma é verificável por quem discorde. O gerador
continua em §5.4, no papel para o qual serve: mostrar o que a fonotática
licencia, não o que a língua tinha.

Um filtro de cronologia governa a escolha, e ele descarta muita coisa
bonita. As formações **pós-anatólias** da lista de inovações do documento 01
§3 não podem aparecer como palavra do Proto-Orogeniano:

| formação | item | exemplo que fica de fora |
|---|---|---|
| tematização (`-o-`) | 11, 12, 13 | `*h₁éteros`, `*kʷóteros`, `*oḱtṓwos` |
| `*-e/o-` como sufixo verbal | 15 | presentes temáticos em `*-eti` |
| causativos `*CoC-éye/o-` | 34 | `*moréyeti`, `*bʰoréyeti`, `*logʰéyeti` |
| perfeito reduplicado | 24 (fraco) | `*memóne`, `*tetóne` — evitados por precaução |

Sobra o que o anatólio de fato conserva: **substantivos atemáticos**, e é
com eles que a seção trabalha.

### 5.1 Léxico

Substantivos atemáticos, invertidos pela tabela de §5.2. Todos verificados
com `invert.py`, todos legais pela fonotática de §4:

| PIE | sentido | Proto-Orogeniano |
|---|---|---|
| `*pṓds` | pé | `/ˈpːeʔts/` |
| `*dóru` | árvore | `/ˈʔte.ru/` |
| `*ǵónu` | joelho | `/ˈʔke.nu/` |
| `*médʰu` | mel | `/ˈme.tu/` |
| `*wódr̥` | água | `/ˈwe.ʔtr̩/` |
| `*h₂ṓws` | orelha | `/ˈqːews/` |
| `*néh₂s` | nariz | `/ˈneqːs/` |
| `*yókʷr̥` | fígado | `/ˈje.kʷːr̩/` |
| `*h₂nḗr` | homem | `/ˈqːner/` |
| `*sḗh₂l` | sal | `/ˈse.qːl̩/` |
| `*gʷṓws` | gado | `/ˈʔkʷews/` |
| `*péḱu` | rebanho | `/ˈpːe.kːu/` |
| `*gʷḗn` | mulher | `/ˈʔkʷen/` |
| `*dóm` | casa | `/ˈʔtem/` |
| `*ǵʰmṓ` | humano | `/ˈkme/` |

Note que **nenhuma tem `[o]`**, embora quase todas sejam citadas com `*o` na
convenção da indo-europeística. É o §3.4 em funcionamento: o grau-o é
posterior, e a forma de citação do PIE já o traz.

#### Onde as polissilábicas realmente vêm

Não do léxico — as raízes e temas do PIE são curtos. Vêm do **paradigma**, e
é aí que o Proto-Orogeniano fica interessante, porque a alternância de grau
reorganiza a palavra inteira:

**`*sḗh₂l` 'sal'** — o paradigma que Kloekhorst usa para dispensar `*ā`
(§3.4):

| caso | PIE | Proto-Orogeniano |
|---|---|---|
| nom.sg | `*sḗh₂l` | `/ˈse.qːl̩/` |
| voc.sg | `*sh₂él` | `/ˈsqːel/` |
| ac.sg | `*sh₂élm̥` | `/ˈsqːe.l̩m/` |
| gen.sg | `*sh₂lés` | `/ˈsqːles/` |
| dat.sg | `*sh₂léy` | `/ˈsqːlej/` |

**`*wódr̥` 'água'** — o heteroclítico `r`/`n`, que o anatólio conserva:

| caso | PIE | Proto-Orogeniano |
|---|---|---|
| nom.sg | `*wódr̥` | `/ˈwe.ʔtr̩/` |
| nom.col | `*wédōr` | `/ˈwe.ʔter/` |
| gen.sg | `*wédn̥s` ⚠ | `/ˈwe.ʔtn̩s/` |
| dat.sg | `*wédney` | `/ˈwe.ʔtnej/` |
| gen.col | `*udnés` | `/u.ˈʔtnes/` |

> ⚠ **A forma `*wédn̥s` é disputada, e Kloekhorst a rejeita.** Ela vem da
> reconstrução acrostática de Schindler (1975a), com acento fixo na raiz.
> Kloekhorst (2014, *Das Nomen im Indogermanischen*, 154–5) mostra que o hitita
> grafa `ú-i-te-e-ni` com acento no **sufixo**, e que o `e/i` da raiz pode ser
> vogal epentética `[ə]` em vez de `*e` pretônico. Ele reconstrói o oblíquo
> como **`*ud-én-`** — grau zero na raiz — e conclui que 'água' *"cannot be
> used as an argument anymore in favor of reconstructing an ó/é-ablauting
> acrostatic inflection type"*.
>
> Na nossa tabela isso significa que a linha `gen.col` `*udnés` → `/u.ˈʔtnes/`
> é a forma **boa**, e a `gen.sg` é a que herda uma reconstrução contestada. O
> dataset traz as duas porque o Wiktionary segue a análise antiga. Mantidas
> ambas, com a etiqueta.

**`*dóru` 'árvore'** — grau pleno contra grau zero na mesma raiz:

| caso | PIE | Proto-Orogeniano |
|---|---|---|
| nom.sg | `*dóru` | `/ˈʔte.ru/` |
| gen.sg | `*dréws` | `/ˈʔtrews/` |
| dat.sg | `*dréwey` | `/ˈʔtre.wej/` |
| abl.pl | `*drúmos` | `/ˈʔtru.mes/` |

Três coisas ficam visíveis aqui que nenhuma palavra sorteada mostraria:

1. **O acento se move**, e é ele que decide onde cai o grau zero — `/ˈseqːl/`
   contra `/sqːˈles/`, com a raiz esvaziada na segunda.
2. **`/w/` e `/j/` alternam entre consoante e núcleo.** Em `/ˈʔterw/` o `/w/`
   é coda; em `/ˈʔtrews/` a mesma raiz o tem em ditongo e o `/r/` é que se
   consoantiza. É a regra 4.2 do documento 03, na prática.
3. **Palavras sem vogal plena existem de verdade**, não só na saída do
   gerador: `/wʔtˈnes/` e `/sqːˈles/` apoiam-se em sonorante silábica e no
   único `/e/`.

### 5.2 A tabela de correspondências

| Proto-Orogeniano | PIH | PIE clássico |
|---|---|---|
| `pː tː ḱː kː kʷː` | idem | `*p *t *ḱ *k *kʷ` |
| `— ʔt ʔḱ ʔk ʔkʷ` | idem | `*b *d *ǵ *g *gʷ` |
| `p t ḱ k kʷ` | idem | `*bʰ *dʰ *ǵʰ *gʰ *gʷʰ` |
| `qː` | `qː` | `*h₂` |
| `qʷː` | `qʷː` | `*h₃` |
| `q ʔq qʷ ʔqʷ` | `ʔ` | `*h₁` |
| `sː mː nː rː lː` **e** `s m n r l` | idem | `*s *m *n *r *l` — **fusão**, ver abaixo |
| `e` | idem | `*e` |
| — | — | `*o` é **derivado**: perda de acento, e `*-ē̆m` > `*-ō̆m` (§3.4) |
| — | — | `*ē *ō` são **derivados**: contração em fronteira de morfema, perda de laringal, Lei de Szemerényi (§3.4) |
| `Ø` | `Ø` | grau zero, em sílaba átona |

**As vogais não têm correspondência unívoca — e a coluna do PO tem uma linha
só.** Onde o PIE cita `*o`, o Proto-Orogeniano tem `/e/`; onde cita `*ē` ou
`*ō`, tem `/e/` também. Qualidade e duração são ambas posteriores e
condicionadas. As leis que as produzem estão formalizadas no documento 04 §8.

**A linha das sonorantes também não é unívoca, e a versão anterior desta
tabela escondia isso.** Ela dizia `sː mː nː rː lː → *s *m *n *r *l
(degeminadas)`, o que sugere uma origem só. Mas a regra **K4** da derivação
(documento 04 §4) degemina sonorantes e sibilante, e o PO tem as duas durações
— logo `/l/` **e** `/lː/` dão `*l`. É fusão, e portanto a inversão de um `*l`
do PIE é uma escolha entre duas fontes.

Isso vale para `*s *m *n *r *l`, que estão em **560 das 766 raízes (73 %)**.
Nas formas deste documento a inversão escolhe sempre a **lenis**, por ser a
opção mais simples — não porque haja evidência. Onde a evidência existiria é
na grafia geminada do hitita, que Kloekhorst (2016) lê como fortis; cruzar o
dataset com um léxico hitita decidiria caso a caso, e é trabalho que o projeto
ainda não fez.

Consequência para o documento 04 §2.5, onde estava subcontada: a ambiguidade
da inversão não é de 24 % das raízes, é de **80 %**.

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

Duas coisas a notar.

`*h₁eḱu-` 'cavalo' sai **sem tema em `-o-`**, como exige o item 11 da lista de
inovações — a tematização é posterior à cisão, e o anatólio conserva a forma
atemática.

*(Uma versão anterior desta lista fechava com `*kʷekʷlos` 'roda' →
`/ˈkʷːekʷːles/`, para ilustrar que os `*o` do PIE não estão no
Proto-Orogeniano. O exemplo estava errado pelo mesmo motivo que o texto acabara
de dar para `*h₁eḱu-`: `*kʷekʷlos` é uma formação **temática**, e a tematização
é pós-anatólia. Foi retirado — a não-univocidade das vogais já está dita na
tabela, sem precisar de uma palavra anacrônica.)*

E `*h₂` (`/qː/`) e `*h₃` (`/qʷː/`) são a mesma uvular, plana e labializada,
exatamente como `*k` está para `*kʷ`. A coloração que cada uma causa é
assimilação comum: `*h₂` recua e abaixa sem arredondar, `*h₃` recua e
arredonda.

### 5.3 O que a fonotática licencia

O gerador [`tools/po-phonology/gen.py`](../tools/po-phonology/gen.py)
implementa §4 e sorteia formas legais. O que ele produz **não é vocabulário** —
é a demonstração de que o molde tem extensão, e o instrumento com que a tarefa
7 se verifica. Saída com `--seed 4400`, curada:

```
/ˈqːer/     /ˈsmeqʷː/    /ˈtːel/      /ˈkʷenq/
/ˈnːem/     /ˈkːeqʷ/     /ˈḱejpː/     /ˈpeqʷ/
/ˈkːwem/    /ˈʔḱewp/     /ˈkːekʷː/    /ˈqʷmeḱ/
```

Comparadas com o léxico de §5.1, essas formas são indistinguíveis em molde —
`/ˈqːer/` tem a forma de `/ˈqːner/` 'homem', `/ˈkːwem/` a de `/ˈʔkʷen/`
'mulher'. É o que se queria mostrar: a fonotática de §4 não é apertada demais
nem frouxa demais para o léxico que a língua de fato tem.

O que elas **não** têm é sentido, etimologia ou testemunho. Por isso saíram da
frente do documento.

### 5.4 Como isso soa

O inventário assusta no papel — 32 consoantes contra uma vogal — mas a fala que
sai da retro-construção é menos extrema do que a tabela sugere, por três
razões que só aparecem nas formas reais:

1. **A vogal única quase nunca é a única sílaba.** Em `/ˈʔte.ru/` 'árvore' e
   `/ˈpːe.kːu/` 'rebanho', a segunda sílaba tem núcleo `[u]` — um glide
   vocalizado. Foneticamente há duas qualidades vocálicas na palavra; só uma
   delas é fonema.
2. **As sonorantes silábicas quebram os aglomerados.** `/ˈse.qːl̩/` 'sal' não é
   `[seqːl]` com três consoantes empilhadas: é `[se.qːl̩]`, duas sílabas, com
   o `[l̩]` fazendo núcleo.
3. **O contraste de duração é o que se ouve primeiro.** `/ˈpːeʔts/` 'pé' abre
   com uma oclusiva longa e fecha com uma pré-glotalizada — a distância entre
   as três séries é de tempo e de ataque, não de vozeamento, e é isso que dá o
   caráter "cortado" descrito em §1.

O efeito somado: uma língua de sílabas curtas e pesadas, com contraste de
quantidade fazendo o trabalho que o vozeamento faz nas filhas. O paralelo do
Cáucaso Noroeste (§1) vale mais para o inventário do que para o ritmo.

---

## 6 | Divisão silábica

Cinco formas reais do §5.1, pelo Princípio do Onset Máximo (M.O.P.), com a
ressalva de que o M.O.P. só se aplica quando o onset resultante for legal.

Computado por
[`tools/po-phonology/syllabify.py`](../tools/po-phonology/syllabify.py), que
implementa o molde de §4.1 — `python3 syllabify.py --doc` reproduz esta seção.
Antes, a divisão era feita à mão; a ferramenta pegou dois erros meus.

**1.** `*wédney` 'água', dat.sg. → `[ˈwe]σ[ʔtnej]σ`

```
      σ                σ
     / \        /   /  |  \
    R   V      C   R   V   R
    w   e     ʔt   n   e   j
```

O M.O.P. leva `ʔtn` inteiro para o onset — sobe em sonoridade, é legal.

**2.** `*sḗh₂l` 'sal', nom.sg. → `[ˈse]σ[qːl̩]σ`

```
      σ            σ
     / \         / \
    s   V       C   V
    s   e      qː  l̩
```

Aqui está o caso que a mão erra. `/seqːl/` **não** é uma sílaba com coda
`qːl`: a coda desce em sonoridade (§4.1), e `qːl` sobe. Sem coda possível, o
`/l/` é forçado a ser núcleo — a regra 4.1 do documento 03 caindo do molde,
não estipulada à parte.

**3.** `*dóru` 'árvore', nom.sg. → `[ˈʔte]σ[ru]σ`

```
      σ            σ
     / \         / \
    C   V       R   V
   ʔt   e       r   u
```

O segundo erro que a ferramenta pegou: qual sonorante vira núcleo. Em `/ʔterw/`
tanto `/r/` quanto `/w/` poderiam, mas a saída correta é `[ru]` e não `[r̩w]`
— **a mais sonora vence**, e glides são mais sonoras que líquidas. É por isso
que o PIE tem `*dóru` e não `*dór̥w`.

**4.** `*udnés` 'água', gen.col. → `[u]σ[ˈʔtnes]σ`

```
     σ              σ
     |        /   /  |  \
     V       C   R   V   s
     u      ʔt   n   e   s
```

Grau zero na raiz: a primeira sílaba é uma vogal só, e ela é o `/w/` de
`/ˈwe.ʔtr̩/` vocalizado. A mesma raiz, dois graus, dois destinos do mesmo
segmento.

**5.** `*drúmos` 'árvore', abl.pl. → `[ˈʔtru]σ[mes]σ`

```
        σ              σ
    /  /  \         /  |  \
   C   R   V       R   V   s
  ʔt   r   u       m   e   s
```

---

## 7 | Conferência das regras

| Regra | Verificação |
|---|---|
| Onset ≤ 3, coda ≤ 3 | ✔ nenhuma forma de §5 excede; no corpus, 99,8 % e 99,9 % (§4.1) |
| Sonoridade sobe no onset, desce na coda | ✔ com as exceções de `/s/` (§4.2), todas nas bordas |
| Máximo uma glotalizada por raiz | ✔ imposto pelo gerador; nenhuma forma de §5 viola |
| Sem `/ʔp/` | ✔ ausente do inventário, não filtrado depois |
| Junção medial ≤ 2 segmentos, sem geminação acidental | ✔ validado por `_bad_juncture` |
| Segmentos idênticos não se encostam **dentro** do aglomerado | ✔ validado por `_repeated` |
| Margens cabem no molde nuclear + apêndices | ✔ 98,3 % do corpus (§4.1); `syllabify.py` deriva a regra em vez de tabelá-la |
| Nenhuma vogal longa | ✔ `/eː/` fora do inventário (§3.4) |
| Acento marcado em toda forma | ✔ |

Verificação automática sobre 800 formas geradas (400 raízes + 400 palavras,
sementes 0–399): zero violações de dissimilação glotálica, zero ocorrências de
`/ʔp/`, zero vogais longas.

*(A linha do `_repeated` é nova. A regra do §4.5 estava enunciada para a
junção silábica e implementada só ali, então um onset `RR` podia sortear duas
vezes a mesma sonorante e produzir `*/nnek/`. O gerador agora aplica a mesma
proibição dentro de onset e coda, e ao núcleo sonorante que segue a sua
própria sonorante — `*/mːm̩.../`.)*

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
| 5 | Inventar palavras | §5 | ✔ **léxico retro-construído** (§5.1) mais o que a fonotática licencia (§5.3) |
| 6 | Desmontar as sílabas de 5 delas | §6 | ✔ cinco, com árvore, computadas por `syllabify.py` |
| 7 | Conferir as regras | §7 | ✔ |

Além do enunciado, a lição recomenda checar o inventário contra bases
tipológicas (§3.7) — feito contra o BDPROTO.

*(A tarefa 5 diz "inventar", e a resposta deste documento é deliberadamente
outra: as palavras do §5.1 não são inventadas, são retro-construídas de léxico
real do PIE, com filtro de cronologia para excluir formações pós-anatólias.
Numa conlang *a posteriori* definida pelo alvo, inventar vocabulário sem
etimologia é o único movimento que o método não licencia. O gerador de §5.3
cobre a leitura literal da tarefa.)*

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

E a lição 4, mudança sonora, é onde a tabela de §5.2 deixa de ser uma tabela e
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
