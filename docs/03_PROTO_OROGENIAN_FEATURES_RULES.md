# Proto-Orogeniano — traços distintivos e regras

**Conlangs University · Phonology 3 — "Distinctive features & rules notation"**

Aplicação da lição 10 do curso ao Proto-Orogeniano. Esta lição **não tem
arquivo de exercício** (`10a` não existe), então o enunciado é a própria
lição: ela ensina o conjunto de traços, a notação de regras e as variáveis
α/β, e o que se espera é que a língua seja descrita nesses termos.

| | |
|---|---|
| Lição | Phonology 3 (Slorany, maio 2020) |
| Pré-requisitos cumpridos | Phonology 1 (IPA) · Phonology 2 ([`02_…`](02_PROTO_OROGENIAN_PHONOLOGY.md)) |
| Ferramenta | [`tools/po-phonology/features.py`](../tools/po-phonology/features.py) — matriz e verificação |
| Próxima | Phonology 4 — mudança sonora |

Convenção da lição, adotada aqui: **`→` para mudança sincrônica** (alofonia
dentro do Proto-Orogeniano) e **`>` para mudança diacrônica** (Proto-Orogeniano
para o proto-indo-hitita). A distinção não é cosmética neste projeto — é a
fronteira entre esta lição e a próxima.

---

## 1 | O conjunto de traços adotado

A lição oferece cerca de vinte traços. Usamos os que fazem trabalho
distintivo nesta língua; os demais ficam de fora, com o motivo:

| grupo | usados | descartados, e por quê |
|---|---|---|
| classe maior | `[±cons]` `[±syll]` `[±son]` | — |
| modo | `[±cont]` `[±nas]` `[±lat]` | `[±DR]`: não há africada — ver §4.3 |
| laríngeos | `[±voice]` `[±c.g.]` | `[±s.g.]`: não há aspiradas nem murmúrio |
| lugar | `[±ant]` `[±cor]` `[±distr]` `[±front]` `[±back]` `[±high]` `[±low]` `[±round]` | `[±strid]` só para separar `/s/` de outra fricativa — e não há outra |
| prosódia | `[±stress]` `[±long]` | — |
| róticos | — | `[±trill]` `[±tap]`: só há um rótico, `/r/` |
| vogais | — | `[±tense]` `[±ATR]`: uma só qualidade vocálica |

`[±voice]` entra mas é **inerte nas obstruintes** — todas são `[−voice]`. Ele
ganha vida só na alofonia (§4.4), e é essa alofonia que a lição 4 vai
promover a fonêmica no PIE clássico.

### O ponto crítico

O documento 02 deixou esta pergunta em aberto: como descrever três séries de
obstruintes **sem apelar a `[±voice]`**? A resposta são dois traços cruzados:

| série | `[±long]` | `[±c.g.]` | exemplo |
|---|---|---|---|
| **fortis** | `+` | `−` | `/tː/` |
| **glotalizada** | `−` | `+` | `/ʔt/` |
| **lenis** | `−` | `−` | `/t/` |
| *(vazia)* | `+` | `+` | — |

A quarta célula está **vazia no Proto-Orogeniano**, e não por acaso: é
exatamente ela que o anatólio preenche depois, por fusão de `*T + h₁`
(Kloekhorst 2022, documento 01 §5.2). O sistema tem um buraco de forma
previsível, e a história o preenche.

`[±c.g.]` é o traço que a lição associa a implosivas, ejetivas e à oclusiva
glotal — precisamente a nossa série pré-glotalizada e o `/ʔ/` em que as
uvulares não-fortis vão colapsar.

### O traço que carrega o contraste é justamente o disputado

Convém encarar isto de frente, porque a matriz inteira depende da escolha. Há
**três** análises rivais do contraste fortis/lenis, e cada uma põe o peso num
traço diferente:

| análise | traço | quem |
|---|---|---|
| **duração** `/tː/` vs. `/t/` | `[±long]` | Kloekhorst; Melchert 1994; Vertegaal 2019–20 (para o lúvico) |
| voz `/t/` vs. `/d/` | `[±voice]` | Simon 2020; a visão tradicional dos manuais |
| aspiração `/tʰ/` vs. `/d/` | `[±s.g.]` | Patri 2009, 2019 |

E há uma segunda disputa, sobre **em que nó** a duração existe:

| posição | quem |
|---|---|
| só no hitita | Yates 2019 |
| já no proto-anatólio | Kloekhorst; apoiado por Vertegaal, que acha o contraste também no lúvico |
| já no PIH | Kloekhorst 2016 — rejeitado por Kümmel 2019 |

Kloekhorst (2021) responde a Simon e a Patri item por item e conclui que a
leitura por duração *"remains unsurpassed"*. Nós adotamos a duração **no nó do
PIH**, que é a posição mais exposta das três: Yates a negaria até no
proto-anatólio.

Isso não muda nada na execução — a escolha já estava declarada no documento 01
§2 — mas o leitor deve saber o tamanho da aposta. Se a leitura por aspiração
estivesse certa, a matriz trocaria `[±long]` por `[±s.g.]` e boa parte de §4
seria reescrita.

---

## 2 | A matriz

Completa e verificável em
[`features.py`](../tools/po-phonology/features.py); aqui o resumo por classe.
Valor **`0`** = impossível ou irrelevante, como na lição.

### Obstruintes — gabaritos de lugar

| | `ant` | `cor` | `distr` | `front` | `back` | `high` | `low` | `round` |
|---|---|---|---|---|---|---|---|---|
| labial | + | − | 0 | 0 | 0 | 0 | 0 | − |
| dental | + | + | + | 0 | 0 | 0 | 0 | − |
| palatal | − | − | 0 | + | − | + | − | − |
| velar | − | − | 0 | − | + | + | − | − |
| labiovelar | − | − | 0 | − | + | + | − | **+** |
| **uvular** | − | − | 0 | − | + | − | **+** | − |
| labiouvular | − | − | 0 | − | + | − | **+** | **+** |

Todas: `[+cons −syll −son −cont −nas −lat −voice −s.g.]`, mais o ajuste
laríngeo de §1.

Repare que **as uvulares são as únicas obstruintes `[+low]`**. É esse traço
sozinho que isola a coluna laringal — o que dá à classe "H" da fonotática uma
definição de um traço só (§3).

Labiais e dentais levam `0` em `front/back/high/low`: a posição do corpo da
língua é irrelevante nelas, como a lição explica para `p`.

### Sibilante, sonorantes, vogais

| segmentos | traços |
|---|---|
| `/s sː/` | `[+cons −syll −son +cont +strid −voice −c.g.]`, lugar dental |
| `/m mː n nː/` | `[+cons −syll +son −cont +nas +voice]` |
| `/r rː l lː/` | `[+cons −syll +son +cont −nas]`, `/l/` é `[+lat]` |
| `/w j/` | `[−cons −syll +son +cont +voice]`; `/j/` palatal, `/w/` labiovelar |
| `/e eː/` | `[−cons +syll +son +cont −high −low +front −back −round]` |

`/sː/` cai na classe fortis pela definição de §1 — e **deve cair**: Kloekhorst
inclui explicitamente as fricativas e sonorantes no contraste de duração
(documento 02 §3.3). A matriz reproduz isso sem estipulação extra.

---

## 3 | Classes naturais

A fonotática do documento 02 §4 usa quatro rótulos — `C`, `H`, `R`, `s`.
Traduzidos em traços, e **verificados** por `features.py`:

| rótulo | definição em traços | resolve para | n |
|---|---|---|---|
| `H` | `[−son −cont +low]` | `q qʷ qː qʷː ʔq ʔqʷ` | 6 |
| `R` | `[+son −syll]` | `m mː n nː r rː l lː w j` | 10 |
| `s` | `[−son +cont]` | `s sː` | 2 |
| `C` | `[−son −cont]` e **não** `[+low]` | as 14 oclusivas restantes | 14 |

Três dos quatro saem de duas features cada. E as séries também:

| classe | definição | n |
|---|---|---|
| fortis | `[−son +long −c.g.]` | 8 |
| glotalizada | `[+c.g.]` | 6 |
| lenis | `[−son −cont −long −c.g.]` | 7 |
| labializada | `[+round]` | 7 |
| núcleo possível | `[+syll]` | 2 |

### O problema do `0`, que é real

`C` é a única que **não** se define por traços positivos e negativos simples,
e a razão importa. Labiais e dentais têm `low = 0`, e `0` não satisfaz
`[−low]` — a lição é explícita em que `0` marca o irrelevante, não um valor
negativo. Então `[−son −cont −low]` deixa `p t pː tː ʔt` de fora e devolve
só 9 segmentos.

A saída honesta não é forçar `low = −` nos labiais, o que seria mentir sobre a
articulação. É reconhecer que **`C` não é classe natural em sentido estrito**:
é o complemento de `H` dentro das oclusivas. `features.py` implementa isso com
um valor `"¬+"` ("qualquer coisa menos `+`"), e a verificação passa.

Isso é uma limitação do sistema de traços da lição aplicado a um inventário com
uvulares, não um defeito do Proto-Orogeniano. Vale registrar: o rótulo `C` da
fonotática é uma abreviação de conveniência, e as regras que realmente
importam abaixo usam `H` e `R`, que são classes de verdade.

---

## 4 | Regras sincrônicas — a alofonia

O documento 02 deixou o **inventário fonético** pendente para esta lição.
Aqui está, em quatro regras.

### 4.1 Silabificação de sonorantes

Uma sonorante vira núcleo quando a sílaba não tem vogal:

```
[+son −syll] → [+syll] / [+cons] _ {[+cons], #}
```

Produz `[m̩ n̩ r̩ l̩]`, e é o que sustenta formas como `/sr̩ˈkːl̩lpː/` e
`/ˈpm̩qːenqʷ/`, palavras inteiras sem vogal plena.

**Mas a realização provavelmente tem schwa.** Kloekhorst & Mens (2021) mostram
que o hitita distingue `/ə/` de `/a/` de modo etimologicamente determinado —
grafia consistente `CaR` reflete PIE `*CR̥` e `*CeR[C]`, alternância `CaR` ~
`Ca-aR` reflete `*CoR` — e o par quase mínimo `/ˈpərsːtsi/` 'ele foge' <
`*bʰérs-ti` contra `/paˈpːarsːtsi/` 'ele asperge' < `*pV-pórs-ti` prova que a
distinção é fonêmica. A conclusão deles: **PIE `*R̥` > hit. `/əR/`**, com
exemplos como `ḫappar` `/χā́pːər/` < `*h₃ép-r̥` e `ḫalzai-` `/χəltsái-/` <
`*h₂l̥toi-`.

Duas leituras, e a escolha muda o inventário fonético:

| leitura | consequência |
|---|---|
| **(a)** a vocalização da sonorante *é* um schwa: `[əR]` | `[ə]` entra no inventário fonético como alofone; nada muda no fonêmico |
| (b) o PIH tinha `[R̩]` puro e o anatólio inseriu o schwa | `[ə]` é inovação anatólia e não nos toca |

Adotamos **(a)**, porque Kloekhorst & Mens tratam o schwa como a própria
vocalização (*"cross-linguistically such vowels are very often centralized
ones"*), e porque ela não custa nenhum fonema: `[ə]` é o que
`[+syll]` soa numa sonorante. A regra fica, então, com realização explícita:

```
[+son −syll] → [ə] + [+son]   /  [+cons] _ {[+cons], #}
```

Registrado como escolha, não como fato: (b) continua disponível.

### 4.2 As altas

A mesma regra, aplicada aos glides, produz as duas vogais altas:

```
/j/ → [i]      /w/ → [u]        (quando [+syll])
```

Não é regra separada: `/j/` e `/w/` são `[+son −syll]` como qualquer sonorante,
e 4.1 os alcança. **`[i]` e `[u]` não são fonemas** — são o que a
silabificação faz com os glides. É a formulação em traços da observação do
documento 02 §3.4, e a razão de o PIE ter `*i` e `*u` sem tê-los no inventário.

### 4.3 Assibilação

Um sibilante epentético entre duas oclusivas coronais:

```
Ø → s / [−son −cont +cor] _ [−son −cont +cor]
```

Reconstruída já para o proto-indo-hitita (documento 01 §5.3), e Melchert
confirma que é regra compartilhada entre PIE e anatólio: hit. `/eːdten/` →
`ēz(zaš)ten` `[eːtsten]`.

**A imunidade de `/tː/` não precisa ser estipulada.** A regra exige *dois*
segmentos coronais adjacentes; `/tː/` é **um** segmento, monofonemático
(documento 01 §5.3). A regra simplesmente não se aplica — a exceção cai fora
de graça, o que é um bom sinal de que a análise monofonemática está certa.

**A saída é um aglomerado, não uma africada** — e isso é uma correção. A
primeira versão desta seção dizia que `[ts]` era `[+DR]`. Kloekhorst (2019)
abandonou explicitamente essa análise para o hitita: *"I no longer believe that
Hittite possessed a monophonemic affricate /ts/. Instead, I think that z in all
its occurrences represents a consonantal cluster of dental stop + sibilant."*

A regra de epêntese acima já produz exatamente isso — um `/s/` **inserido como
segmento próprio**, entre duas oclusivas. Nada a consertar na regra; só na
descrição. E `[±DR]` sai do conjunto de traços (§1), porque nada na língua o
usa.

O mesmo artigo dá um reforço independente do sistema de duração: Kloekhorst
distingue **quatro** aglomerados no hitita intervocálico, pela duração de cada
membro separadamente —

| aglomerado | grafia |
|---|---|
| `/t/` + `/s/` | `Vz-zV` |
| `/t/` + `/sː/` | `Vz-šV` |
| `/tː/` + `/s/` | `Vz-zV` |
| `/tː/` + `/sː/` | `Vt-šV` |

Quatro combinações em três grafias. Que a duração seja contrastiva
*independentemente em cada membro de um aglomerado* é difícil de explicar sob
uma análise por voz ou por aspiração.

### 4.4 Vozeamento alofônico das lenis

```
[−son −cont −long −c.g.] → [+voice] / [+syll] _ [+syll]
```

As lenis vozeiam entre núcleos. Kloekhorst (2016: 216 n.12) descreve isso para
o hitita e insiste que é **subfonêmico**: *"this voicing is sub-phonemic only,
and the real phonemic distinction between fortis and lenis stops is not one in
voice, but in consonantal length"*.

Esta é a regra mais importante do documento para o que vem depois. O
`[±voice]` que em §1 declarei inerte está aqui, alofônico — e é exatamente
esse vozeamento que o PIE clássico **fonemiza** quando a duração se perde. A
mecânica é da lição 4; a semente está aqui.

### 4.5 Assimilação de lugar nas nasais

Motivada pela fonotática: `RC` é o tipo de coda mais comum das raízes (227
ocorrências, documento 02 §4.1), e nasal + oclusiva é o caso central.

Com as variáveis da lição:

```
[+nas] → [αant βcor γhigh δback] / _ [−son −cont, αant βcor γhigh δback]
```

"Uma nasal assume o lugar da oclusiva que a segue." As quatro variáveis são
necessárias porque o inventário tem sete lugares, e dois traços não os separam.

### O inventário fonético

Fonemas de §2, mais o que as regras acima produzem:

```
[ə]                      vocalização das sonorantes          (4.1)
[m̩] [n̩] [r̩] [l̩]      as sonorantes nessa posição         (4.1)
[i] [u]                  glides silábicos                    (4.2)
[t.s]                    aglomerado de assibilação           (4.3)
[b] [d] [ɟ] [ɡ] [ɡʷ] [ɢ] [ɢʷ]   lenis vozeadas               (4.4)
[ɱ] [ɲ] [ŋ] [ɴ]          nasais assimiladas                  (4.5)
```

O inventário fonético é **substancialmente maior** que o fonêmico — 34 fonemas
contra ~52 fones. E note o que a coluna de 4.4 mostra: **a série sonora do PIE
clássico já existe no Proto-Orogeniano, como alofonia.** Nada precisa ser
criado; basta a duração cair.

---

## 5 | Regras diacrônicas — só a notação

A derivação completa é a lição 4. Aqui, duas regras a título de demonstração
da notação, com `>`:

**Colapso das uvulares não-fortis** (invenção do projeto, documento 02 §3.2):

```
[−son −cont +low −long] > ʔ
```

Uma linha. As uvulares fortis (`[+low +long]` = `*h₂ *h₃`) não são alcançadas;
as demais viram `*h₁`. A economia da formulação é um argumento a favor da
proposta — e o §3.2 registra que ela é a única invenção estrutural do projeto.

**Perda de vogal átona** — o motor do grau zero:

```
[+syll] > Ø / [−stress]
```

É a formulação em traços do que Brugmann descreve: no PIE inicial "todas as
formas mostram um só morfema acentuado, com grau-e, e todos os demais átonos,
com grau zero" (documento 02 §3.4). Ordená-la em relação às outras é trabalho
da lição 4.

---

## 6 | Estado da lição

| item da lição | onde |
|---|---|
| Traços de classe maior, modo, laríngeos, lugar, prosódia | §1, §2 |
| Matriz completa do inventário | §2 + `features.py` |
| Uso de `0` para o irrelevante | §2, §3 |
| Classes naturais em traços | §3 |
| Notação de regras (`→`, `/`, `_`) | §4 |
| Fronteiras (`#`, `σ`, `$`) | §4.1 |
| Conjuntos `{}` e conjunto vazio `Ø` | §4.1, §4.3 |
| Regras com traços em vez de símbolos | §4 inteiro |
| Variáveis α/β | §4.5 |
| `→` sincrônico vs. `>` diacrônico | §4 vs. §5 |
| **Inventário fonético** (pendência da lição 2) | §4, quadro final |

**Não usados, por não haver o que descrever:** índices subscritos para
elementos distintos (`C₁_C₂`), parênteses de opcionalidade, fronteira de
morfema `+` — esta última porque não há morfologia ainda. Reaparecerão nas
lições 04 e 05.

## O que fica para a lição 4

1. **Ordenar as regras.** Quatro sincrônicas e duas diacrônicas já escritas; a
   derivação precisa de ordem relativa, e a ordem é falseável.
2. **A fonemização do vozeamento** — §4.4 vira contraste quando a duração cai.
   É o coração da tese de Kloekhorst 2016 e o teste central do projeto.
3. **As duas leis que produzem `*o`**: a *Abtönung* (perda de acento) e
   `*-ē̆m` > `*-ō̆m` (Kloekhorst 2024).
4. **Rodar tudo contra as 873 raízes** de `PIE_roots` e contar os acertos. É a
   primeira vez que o projeto terá uma métrica de sucesso, e não só coerência.
