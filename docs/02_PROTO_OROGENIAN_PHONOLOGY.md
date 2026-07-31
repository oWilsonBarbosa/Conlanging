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
- **Pobreza vocálica com riqueza consonantal.** Duas qualidades de vogal contra
  36 fonemas no total. A informação lexical mora nas consoantes.

**Comparação com línguas reais.** O perfil mais próximo é o do **Cáucaso
Noroeste** — abkhaz, ubykh — pela combinação de inventário consonantal denso,
uvulares e sistema vocálico mínimo. A glotalização aproxima dos sistemas
ejetivos caucasianos. E o contraste de duração consonantal fazendo trabalho
lexical lembra o finlandês ou o italiano.

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

```
/ˈqːweq  ˈstːeqː  wejˈʔt-os  ˈlewkː-mn̩  pːenˈtː-eros/
```

As quatro primeiras são derivadas de raízes reais (§3.4); os elementos após o
hífen são preenchimento silábico, sem valor gramatical.

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

Três consequências verificáveis, e é por isso que essa é a única invenção
estrutural do documento:

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

`/sː/` é exigido pelo hitita `e-eš-ši` `/ʔésːi/` < PIH `*h₁éssi`, contra o PIE
clássico degeminado `*h₁ési`. `/mː/` é exigido pelo item 21 da lista de
inovações: `*h₁mm-` > cl.PIE `*h₁m-`.

Sonorantes silábicas servem de núcleo: `m̩ n̩ r̩ l̩`. E — ponto que resolve
sozinho a pobreza vocálica — **`[i]` e `[u]` são os alofones silábicos de
`/j/` e `/w/`**. É daí que saem `*i` e `*u` do PIE.

### 3.4 Vogais

| | anterior | posterior |
|---|---|---|
| **médias** | `e` `eː` | `o` `oː` |

Duas qualidades, com contraste de duração. **Não existe `/a/`** — restrição
dura, consequência última da teoria laringal (Lubotsky 1989, Pronk 2019),
confirmada no dataset: 9 raízes em 873.

Um sistema de duas vogais é tipologicamente extremo. A lição observa que a
maioria das línguas fica entre 5 e 8, que 3 já é raro, e que o sistema
trivocálico usual é `/i a u/` — nenhum dos quais nos serve. Mas a lição também
diz, duas vezes: *"These generalities are not rules, and twisting or breaking
them is allowed."* Aqui não se está quebrando por gosto: o alvo obriga.

A carga funcional que as vogais não carregam se distribui em três lugares:
os núcleos sonorantes silábicos, o contraste de duração consonantal, e o
**acento livre** com o ablaut que ele condiciona.

### 3.5 Acento

**Livre** — pode cair em qualquer sílaba, e é contrastivo. Herdado direto do
alvo: a língua-mãe tinha acento livre pelos reflexos em védico, grego,
balto-eslavo e germânico, e o lídio tinha acento tônico livre.

É o acento que condiciona a lenição — no anatólio, entre moras átonas — e é
ele que vai alimentar o ablaut. As regras ficam para a lição 3.

### 3.6 Total

```
obstruintes  20    sibilantes   2    sonorantes  10    vogais  4
TOTAL        36
```

Perfil consonante-pesado: 32 consoantes contra 4 vogais. Confere com o retrato
de §1.

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

### 4.4 Dissimilação glotálica

A restrição mais forte do sistema, e a mais interessante. Contando as séries
de oclusivas que coocorrem nas 216 raízes com duas ou mais:

| par | n | % |
|---|---|---|
| fortis + fortis | 72 | 33,3 % |
| glotalizada + fortis | 49 | 22,7 % |
| lenis + lenis | 45 | 20,8 % |
| glotalizada + lenis | 30 | 13,9 % |
| lenis + fortis | 19 | 8,8 % |
| **glotalizada + glotalizada** | **1** | **0,5 %** |

Fortis com fortis: livre. Lenis com lenis: livre. **Duas glotalizadas na mesma
raiz: praticamente proibido** — uma única exceção em 216, `*gʷeg-`.

Essa é a conhecida restrição do PIE contra duas oclusivas sonoras simples numa
raiz. Sob a leitura tradicional ela é difícil de motivar: por que uma língua
proibiria duas sonoras e permitiria livremente duas surdas e duas aspiradas?
Sob a leitura glotálica ela é banal — é dissimilação de glotalização, do mesmo
tipo atestado nos sistemas ejetivos semíticos e caucasianos.

**Nosso dataset sustenta independentemente a leitura glotálica que o sistema de
Kloekhorst exige.** É a única verificação empírica que este documento produz,
e ela saiu a favor.

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
/ˈkːen/      /ˈmoḱ/       /ˈkrenː/     /ˈsmoqʷː/
/ˈkʷːolk/    /ˈqonːpː/    /ˈʔkeːtː/    /ˈqːoʔkʷ/
/ˈpeḱːqː/    /ˈkʷmow/     /ˈmːeːmḱː/   /ˈʔkʷem/
```

**Polissilábicas:**

```
/soˈkʷonq/        /ˈsepːeːmːtː/     /kʷːroˈnqʷenː/
/rːeˈrqʷes/       /ˈlːerjosḱekː/    /ʔkʷeˈqʷn̩tːejpː/
```

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
| `e o eː oː` | idem | `*e *o *ē *ō` |

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
| `*kʷekʷlos` | roda | `/ˈkʷːekʷːlos/` |

Note `*h₁eḱu-` 'cavalo': a forma sai **sem tema em `-o-`**, como exige o item
11 da lista de inovações — a tematização é posterior à cisão, e o anatólio
conserva a forma atemática.

---

## 6 | Divisão silábica

Cinco polissilábicas, pelo Princípio do Onset Máximo (M.O.P.), com a ressalva
de que o M.O.P. só se aplica quando o onset resultante for legal.

**1.** `/soˈkʷonq/` → `[so]σ[ˈkʷonq]σ`

```
      σ              σ
     / \          /  |  \
    C   V        C   V   C C
    s   o        kʷ  o   n q
```

**2.** `/ˈsepːeːmːtː/` → `[ˈse]σ[pːeːmːtː]σ` — o M.O.P. leva `pː` inteiro para
o onset da segunda sílaba, porque `/pː/` é monofonemática (§4.5 do documento
01: `/tː/` não é `/t/`+`/t/`).

**3.** `/kʷːroˈnqʷenː/` → `[kʷːron]σ[ˈqʷenː]σ`

Aqui o M.O.P. **falha**. Levar `nqʷ` inteiro para o onset daria um onset que
desce em sonoridade (nasal → oclusiva), proibido por §4.1. O `n` fica na coda
da primeira sílaba, e o acento cai na segunda.

**4.** `/rːeˈrqʷes/` → `[rːer]σ[ˈqʷes]σ` — mesma razão: `rqʷ` não é onset
legal.

**5.** `/ˈlːerjosḱekː/` → `[ˈlːer]σ[jos]σ[ḱekː]σ`

```
       σ            σ           σ
    /  |  \      /  |  \     /  |  \
   C   V   C    C   V   C   C   V   C
   lː  e   r    j   o   s   ḱ   e   kː
```

---

## 7 | Conferência das regras

| Regra | Verificação |
|---|---|
| Onset ≤ 3, coda ≤ 3 | ✔ nenhuma forma de §5 excede |
| Sonoridade sobe no onset, desce na coda | ✔ com as exceções de `/s/` (§4.2), todas nas bordas |
| Máximo uma glotalizada por raiz | ✔ imposto pelo gerador; nenhuma forma de §5 viola |
| Sem `/ʔp/` | ✔ ausente do inventário, não filtrado depois |
| Sem `/a/` | ✔ ausente do inventário |
| Junção medial ≤ 2 segmentos, sem geminação acidental | ✔ validado por `_bad_juncture` |
| Acento marcado em toda forma | ✔ |

### Conferência contra as restrições do documento 01

O teste que importa de verdade — o inventário alimenta o alvo de §9.1?

| Restrição (§9.1) | Estado |
|---|---|
| Oclusivas por duração + glotalização, não por voz | ✔ §3.1 |
| Laringais como oclusivas uvulares `/qː/`, `/qʷː/` | ✔ §3.1, coluna uvular |
| Nenhum fonema `*a` | ✔ §3.4 |
| Acento livre condicionando lenição | ✔ §3.5 |
| `/tː/` monofonemática, distinta de `/t/`+`/t/` | ✔ §6, exemplo 2 |
| Contraste de duração em `/s/` e sonorantes | ✔ §3.3 |

| Restrição (§9.2) | Estado |
|---|---|
| Sem série de oclusivas sonoras | ✔ nenhuma sonora no inventário |
| Sem laringais fricativas | ✔ são oclusivas |
| Sem fonema `*a` | ✔ |

Nada em conflito.

---

## O que fica em aberto para a lição 3

A lição 3 pede traços distintivos e notação de regras. Três coisas ficam
esperando por ela:

1. **A matriz de traços.** O contraste de três séries precisa de traços que o
   descrevam sem apelar a `[±voz]`: provavelmente `[±longo]` e
   `[±constrição glotal]`.
2. **As regras de alofonia.** Silabificação das sonorantes, realização de
   `/j w/` como `[i u]`, e a lenição condicionada pelo acento.
3. **A regra de assibilação.** `*-TT-` > `*-TsT-`, com `/tː/` imune por ser
   monofonemática — está reconstruída já para o PIH e precisa de formulação
   formal.

E a lição 4, mudança sonora, é onde a tabela de §5.1 deixa de ser uma tabela e
vira um conjunto de regras ordenadas, aplicável às 873 raízes e conferível
contra elas.
