# Proto-Orogeniano — mudança sonora

**Conlangs University · Phonology 4 — "Sound change"**

> **Em andamento.** Banco de provas, medição, ordenação, a tarefa 3 e as leis
> vocálicas estão feitos. Faltam o grau zero e a tarefa 4.

| | |
|---|---|
| Lição | Phonology 4 (Jasper, maio 2020) — a mais longa do curso |
| Ferramenta | [`tools/po-derivation/`](../tools/po-derivation/) |
| Estado | §1–§8 fechados; grau zero e tarefa 4 pendentes |

---

## 1 | Rodar teorias rivais em paralelo

A pergunta que abriu esta lição: dá para concorrer com duas teorias sobre as
apostas em aberto? **Quatro das cinco, sim.** Uma delas não é teoria.

| aposta | é teoria rival? | a métrica separa? |
|---|---|---|
| vocalismo: 1 ou 2 qualidades | sim | **sim** — ver §2 |
| oclusivas: duração / voz / aspiração | sim, três | **não como acurácia** — ver §2.3 |
| laringais: coluna uvular completa ou `*h₁` herdado | sim | **não** — indistinguíveis na métrica |
| schwa: `[əR]` ou `[R̩]` | sim, mas fonético | não — mesma saída na derivação |
| `C` como classe natural | **não** | não se aplica |

`C` não tem rival porque não é uma tese sobre a língua: é uma limitação do
sistema de traços da lição aplicado a um inventário com uvulares (documento 03
§3). Não há segunda teoria para rodar; há uma notação que não cobre o caso.

O schwa é teoria de verdade, mas as duas leituras produzem **a mesma sequência
de segmentos** na derivação — diferem só na realização fonética. A métrica é
cega a ela.

### Arquitetura

Combinar tudo daria 3 × 2 × 2 × 2 = 24 variantes, o que não se administra. O
desenho adotado é **uma linha de base mais variantes que diferem dela em
exatamente uma dimensão**, para isolar a variável:

```
tools/po-derivation/theories.py     as variantes, como configuração
tools/po-derivation/invert.py       o banco de provas
```

Nenhuma variante é um fork do código. Trocar de teoria é trocar um dicionário.

---

## 2 | O banco de provas

### 2.1 Por que "índice de acerto" seria fraude

O Proto-Orogeniano é *definido* pelas correspondências com o PIE. Aplicar as
regras para a frente devolve o PIE por construção — 100 % de acerto, zero de
informação. Qualquer métrica honesta tem que medir outra coisa.

Três medidas que não são circulares:

| medida | o que testa |
|---|---|
| **legalidade** | as formas proto-orogenianas obedecem à fonotática do documento 02 §4? Uma teoria que produz formas ilegais erra em algum lugar |
| **colisão** | quantas raízes distintas colapsam na mesma forma. É a pergunta 4 do exercício: *"does it merge grammatically distinct forms?"* |
| **ambiguidade** | quantos pontos da derivação não são invertíveis e precisam de condicionamento |

### 2.2 Primeira medição

766 raízes distintas (o dataset repete grafias para homógrafos; contá-las seria
medir o dataset, não a derivação).

| teoria | ilegais | colisões | sem corresp. |
|---|---|---|---|
| **baseline** — duração · coluna uvular · 1 vogal | 12 | 2 | 9 |
| voz (Simon 2020) | 7 | 2 | 9 |
| aspiração (Patri) | 11 | 2 | 9 |
| laringal mínima (`*h₁` herdado) | 12 | 2 | 9 |
| duas vogais | 12 | **0** | 9 |

### 2.3 Menos violações **não** é melhor teoria

É o achado metodológico da medição, e sem ele a tabela acima engana.

As 12 ilegalidades do baseline se decompõem assim:

| origem | n | o que é |
|---|---|---|
| raízes com `*b` | 5 | a lacuna `/ʔp/` **prevista** em §3.2 do documento 02 |
| raízes com `*a` | 6 | o conjunto não-nativo **previsto** em §3.4 |
| `*gʷeg-` | 1 | duas glotalizadas — o outlier conhecido, agora pego automaticamente |

Ou seja: **todas as 12 são previsões cumprindo-se**, não falhas. A teoria da
voz marca 7 apenas porque mapeia `*b` para `/b/` — ela não faz a previsão, e
por isso não pode falhá-la. Uma teoria que não prevê nada nunca erra.

A métrica de legalidade, portanto, **não ordena as três teorias de oclusivas**.
O que ela faz é confirmar que as três previsões do baseline caem exatamente
onde deveriam. Isso é um resultado, mas não é o resultado que a coluna sugere.

*(Nota técnica: a variante da aspiração marca 11 e não 12 porque usa símbolos
que o detector de glotalizadas não reconhece — artefato do banco de provas, não
da teoria.)*

### 2.4 Onde a métrica **discrimina de verdade**

**O vocalismo.** Duas colisões contra zero, e as duas são:

```
/qepː/   ←  *h₁ep,   *h₁op
/kːrews/ ←  *krews,  *krows
```

Ambas são **grau-e e grau-o da mesma raiz**. Ou seja: a única fusão que a
teoria de uma vogal provoca é entre variantes de grau do mesmo lexema — que é
precisamente o que "o grau-o é derivado" significa. A teoria de duas vogais
evita as duas colisões, mas só porque se recusa a derivar o que a literatura
diz ser derivado.

Duas colisões em 766, ambas previstas e ambas do tipo certo. É o resultado mais
favorável ao vocalismo mínimo que o projeto produziu até agora — e vale contra
o alerta tipológico do documento 02 §3.7, que continua de pé.

### 2.5 Onde a métrica é cega, e o custo que ela expõe

A **laringal mínima** dá números idênticos ao baseline em tudo. A escolha entre
a coluna uvular completa e um `*h₁` herdado não deixa marca aqui.

Mas a medição expôs um custo da nossa invenção que eu não tinha quantificado:

| | raízes | % |
|---|---|---|
| com `*h₁` — 4 origens possíveis (`/q ʔq qʷ ʔqʷ/`) | 115 | 15 % |
| com `*H` — laringal indeterminada na própria filologia | 71 | 9 % |
| **total com ponto ambíguo** | **186** | **24 %** |

Um quarto das raízes tem pelo menos um ponto onde a derivação não é
invertível. Os 71 de `*H` não são culpa nossa — a filologia não decide. Mas os
115 de `*h₁` são: a coluna uvular completa transforma cada `*h₁` numa escolha
de quatro. A teoria da laringal mínima paga zero por isso.

O documento 02 §3.2 justifica a invenção por três consequências verificáveis.
Agora há um preço do outro lado da balança, e ele está medido.

---

## 3 | A taxonomia da lição

A lição classifica mudanças em assimilação (regressiva, progressiva,
coalescência, nasalização), dissimilação, *unpacking*, epêntese (excrescência,
anaptixe), elisão, lenição (**abertura** e **sonorização**), fortição, metátese
e rotacismo.

Duas entradas dessa taxonomia importam desproporcionalmente para nós, e a
lição as descreve sem saber que estava descrevendo o nosso caso:

> **Abertura:** *"At the least sonorous side, we find geminate stops — solely
> by losing their gemination, they become more sonorous."*

> **Sonorização:** *"happens particularly often intervocalically, in which
> sense the adoption of voicing could be seen as assimilation to the
> surrounding vowels. ... the first step is the voicing of voiceless
> consonants."*

Isto é a cadeia de arraste de Kloekhorst, item por item: degeminação de
`*/tː/` e vozeamento de `*/t/` entre vogais. **As duas são lenições de
manual, no ambiente onde mais comumente ocorrem.**

---

## 4 | A derivação, ordenada

Cinco regras levam do Proto-Orogeniano ao PIE clássico. Implementadas em
[`derive.py`](../tools/po-derivation/derive.py).

| # | regra | categoria da lição |
|---|---|---|
| **U1** | debucalização das uvulares não-fortis → `*h₁` | lenição · abertura (debucalização) |
| **K1** | vozeamento de lenis e glotalizadas | lenição · **sonorização** |
| **K2** | degeminação das oclusivas fortis | lenição · **abertura** |
| **K4** | degeminação de sibilante e sonorantes | lenição · abertura — **com fusão** |
| **K3** | espirantização das uvulares fortis → `*h₂ *h₃` | lenição · abertura (espirantização) |

**A perna inteira é lenição.** Não há uma única fortição, assimilação ou
metátese na derivação: são cinco pontos da mesma escala de abertura e
sonorização que a lição descreve. Uma língua que atravessa alguns séculos de
contato e sai do outro lado tendo apenas *enfraquecido* é exatamente o que se
espera — e é o oposto de uma reconstrução que precisa de mudanças exóticas para
funcionar.

### 4.1 A ordem é forçada — e dá para medir

A lição avisa que *"the order may be important!"*. Aqui isso foi medido, não
afirmado. Rodando as 690 formas proto-orogenianas utilizáveis nas duas ordens:

| ordem | saídas distintas | fusões | contrastes perdidos |
|---|---|---|---|
| **vozeamento antes da degeminação** | **688** | **0** | **0** |
| degeminação antes do vozeamento | 644 | 44 | 44 |

A ordem errada destrói **44 contrastes**. O mecanismo é visível nos exemplos:

```
*bʰed-   ←  /peʔt/  e  /pːeʔt/
*bʰel-   ←  /pel/   e  /pːel/
```

Se `/tː/` degemina antes de `/t/` vozear, os dois viram `/t/` e se fundem;
depois o vozeamento leva ambos ao mesmo lugar. O contraste triplo vira duplo.
Se o vozeamento vem primeiro, `/t/` sai de cena virando `[d]` e a degeminação
encontra o espaço vazio.

É a *pull chain* de Kloekhorst, e agora ela não é uma metáfora: é uma
ordenação com custo numérico.

### 4.2 U1 antes de K1 — argumentada, não medida

As uvulares não-fortis têm de sair **antes** do vozeamento. Se ainda
estivessem lá, K1 as vozearia para `[ɢ]`, e `*h₁` carregaria efeito de voz.
Não carrega: `*h₁` é a laringal incolor e surda. Ela saiu cedo.

Este argumento é explanatório, não numérico — a métrica não o testa.

### 4.3 O que é livre

**K4 em relação a K1 e K2** e **K3 em relação a K2** são ordem-indiferentes: a
degeminação de sibilante e sonorantes não toca as oclusivas, e a coluna uvular
já foi isolada por U1. Distinguir o que é forçado do que é livre é metade do
exercício.

### 4.4 A assimetria que cai de graça

K4 é **a única regra da cadeia que é pura fusão**. E é isso que explica um
fato do PIE que nunca tínhamos justificado:

| classe | o que acontece com a duração | resultado no PIE |
|---|---|---|
| oclusivas | é **recodificada** como voz (K1 + K2) | **três** séries |
| sibilante, sonorantes | é simplesmente **perdida** (K4) | **um** `*s`, **um** `*m`… |

O PIE tem três séries de oclusivas e uma só sibilante porque as oclusivas
tinham para onde recodificar o contraste e as sibilantes não.

**Custo:** essa fusão é **irrecuperável por inversão**. De um `*s` do PIE não
há como saber se o Proto-Orogeniano tinha `/s/` ou `/sː/`. O banco de provas
nunca gera `/sː/`, `/mː/` etc. a partir do PIE — a duração nas sonorantes está
no inventário (documento 02 §3.3) mas fora do alcance deste corpus.

---

## 5 | Tarefa 3 do exercício

> *"Have a look at the allophones you decided for on your conlang and in which
> environments they appear. Can you classify them under any of the categories
> above?"*

As cinco regras sincrônicas do documento 03 §4, classificadas:

| regra | ambiente | categoria |
|---|---|---|
| 4.1 silabificação de sonorantes | `[+cons] _ {[+cons], #}` | lenição · sonorização (**vocalização**) + **anaptixe** para o schwa |
| 4.2 `/j w/` → `[i u]` | idem — é a mesma regra | vocalização |
| 4.3 assibilação | entre coronais | epêntese · **excrescência** |
| 4.4 vozeamento das lenis | entre núcleos | lenição · **sonorização**, passo 1 |
| 4.5 assimilação de lugar nas nasais | antes de oclusiva | **assimilação regressiva** |

Todas as cinco caem em categorias da lição, o que é um bom sinal: nenhuma
precisou de uma categoria inventada.

Três convergências valem registro, porque a lição dá os nossos casos como
exemplos dela própria:

- **Vocalização.** A lição fecha a escala da sonorização com a
  l-vocalização — *"[l] vocalises into [i] or [w]"*. As nossas 4.1 e 4.2 são
  exatamente isso, e a 4.2 explica por que o PIE tem `*i` e `*u` sem tê-los no
  inventário.
- **O schwa.** A lição diz que a vogal de apoio *"is not inserted at the end
  but slightly before, **especially in the case of sonorants**"*, e dá
  proto-germânico `*akraz` > inglês `acre` `[-ər]`. É estruturalmente idêntico
  ao `*R̥ > /əR/` de Kloekhorst & Mens que o documento 03 §4.1 adotou.
- **Excrescência.** Definida na lição como consoante inserida para **ligar um
  aglomerado**. A nossa assibilação insere `/s/` entre duas oclusivas
  coronais — o caso exato.

### O elo entre as duas colunas

A regra sincrônica **4.4** e a diacrônica **K1** são o mesmo vozeamento. A
diferença é o ambiente: 4.4 vale entre núcleos, K1 vale em toda posição.

A transição, então, não inventa nada. Ela **generaliza** uma alofonia que já
existia, e a generalização se torna possível justamente quando a duração deixa
de carregar o contraste. É por isso que o documento 03 §4.4 diz que a série
sonora do PIE já existe no Proto-Orogeniano: ela existe como alofone, e a
mudança só lhe tira a condição.

---

## 6 | Conferência contra o PBase

Dois textos externos entraram no projeto nesta altura: *Patterns of Allophony*
(Annis, Fiat Lingua 2019) e um handout de linguística histórica, *Types of
Sound Change* (Moore 2013). O primeiro não é útil pelo conteúdo — são gráficos,
e a extração perdeu a estrutura — mas é útil por dizer **de onde vem**: o
**PBase**, que está em `data/pbasefiles.zip` desde o primeiro dia e nunca havia
sido aberto. 21.794 padrões de alofonia em 625 línguas.

É a comparação certa para as regras sincrônicas, do mesmo modo que o BDPROTO
foi a comparação certa para o inventário.

| nossa regra | padrões no PBase | línguas | veredito |
|---|---|---|---|
| **4.4 / K1** vozeamento intervocálico de oclusiva surda | **72** | **25** | bem atestado |
| **4.1** sonorante silábica na saída | 66 | 14 | atestado |
| **K3** `/q/` → `[χ]` (espirantização) | 4 | — | atestado |
| **U1** debucalização (C → `[ʔ]`) | **10** | **6** | **o mais raro dos nossos** |

Alofonia de `/q/` no PBase, saídas mais frequentes: `qʰ` (12), `∅` (6),
**`ɢ` (5)**, `qʷ` (4), `k` (4), **`χ` (4)**.

### O que isso confirma

O argumento de §4.2 — que as uvulares não-fortis tiveram de sair antes do
vozeamento, porque senão `*h₁` carregaria efeito de voz — deixou de ser
especulação: **`/q/` → `[ɢ]` é padrão atestado**, com cinco ocorrências. Era
exatamente o que aconteceria se a ordem fosse outra.

E o vozeamento intervocálico, o passo mais importante da derivação, está entre
os padrões bem representados: 25 línguas.

### O que isso complica

**A debucalização é a nossa regra mais fraca.** Dez padrões em seis línguas,
contra 72 em 25 do vozeamento. E a debucalização é precisamente a **U1**, a
regra que implementa a única invenção estrutural do projeto — a coluna uvular
completa colapsando em `*h₁`.

Somando o que já se sabia:

| custo da coluna uvular completa | medida |
|---|---|
| ambiguidade que introduz (§2.5) | 24 % das raízes com ponto não-invertível |
| a métrica de legalidade a distingue da alternativa? | não (§2.5) |
| suporte tipológico do mecanismo que ela exige | 6 línguas no PBase |

A justificativa continua de pé — três consequências verificáveis, documento 02
§3.2 — mas a conta do outro lado cresceu de novo. Registro, não veredito.

*(Ressalva: o PBase cataloga alofonia sincrônica, não mudança diacrônica. A
debucalização como mudança histórica — o `/t/` > `[ʔ]` do inglês — é
comuníssima; o que a tabela mede é sua raridade como alternância sincrônica
listada. A assimetria com o vozeamento é real, mas não é tão dura quanto os
números crus sugerem.)*

## 7 | Alongamento compensatório, e uma vogal a menos

O handout de Moore lista uma categoria que a lição do curso não enfatiza:

> **(16) Compensatory lengthening** — *"C deletion results in a lengthening of
> the preceding vowel"*, com antigo irlandês `*magl > máːl`, `*etn > éːn`.

Isso levanta uma pergunta sobre o nosso inventário. De onde vêm as vogais
longas? Medido no corpus:

| | raízes | % |
|---|---|---|
| citadas com vogal longa (`*ē`, `*ō`) | **0** | 0 % |
| com sequência `V + laringal` | 120 | 15,7 % |

**Nenhuma raiz do corpus tem vogal longa própria.** A fonte padrão de
alongamento — vogal seguida de laringal — está em 120. E as vogais longas que
aparecem nas fontes primárias são todas derivadas: os `*sḗm`, `*dḗm`, `*dʰǵḗm`
de Kloekhorst (2024) vêm da Lei de Szemerényi, que é alongamento compensatório
por perda de `*-s`.

**Proposta:** o Proto-Orogeniano não precisa de `/eː/`. O inventário vocálico
cai de dois fonemas para **um**, e toda duração vocálica passa a ser derivada —
por perda de laringal ou de sibilante, com alongamento compensatório.

> ⚠ **Corrigido e executado em §8.3.** Duas coisas desta seção não sobreviveram
> ao corpus de formas flexionadas. A frase "o corpus não pode testar isso" era
> falsa — ele podia, com o corpus certo. E o **mecanismo** apontado aqui está
> errado: o alongamento por perda de laringal responde por **2 %** das vogais
> longas, não pela maioria. A *proposta* saiu reforçada, foi executada, e o
> inventário do documento 02 caiu para **33 fonemas**.

**Mas o corpus não pode testar isso.** Com zero raízes exercendo o contraste, a
variante "vogal longa derivada" produziria números idênticos ao baseline. Fica
registrada como proposta com evidência, não executada — a mesma disciplina
aplicada ao schwa no documento 03 §4.1.

Nota para a tipologia: isso **não** agrava o alerta do documento 02 §3.7. A
contagem lá é de *qualidades* vocálicas, e ela já era 1.

---

## 8 | O corpus errado

A pergunta que abriu esta seção foi do usuário: *"não seria melhor testar com
palavras ou stems?"*

Sim. E o erro era mais caro do que parecia. Tudo o que §7 e a lista de
pendências declararam **intestável** era intestável só porque o corpus estava
errado — não porque a evidência não existisse.

### 8.1 O corpus

Uma raiz do PIE é uma abstração: citada em grau-e, sem flexão e sem acento.
Três coisas ficam fora de alcance por construção — a *Abtönung* (condicionada
por acento), as vogais longas (que raízes não carregam) e o grau zero (que
precisa de paradigma).

Mas as 1.891 entradas do `PIE_roots` não são só raízes. **1.018 são outra
coisa** — substantivos, verbos, adjetivos, sufixos — e trazem tabelas de
flexão:

| | |
|---|---|
| formas flexionadas limpas | **40.894** |
| **com acento marcado** | **38.128 (93 %)** |
| com `*o` | 14.945 |
| com vogal longa | 3.167 |
| por classe | verbo 14.480 · subst. 9.417 · adj. 8.559 · sufixo 6.759 · pron. 776 |

53 vezes o corpus de raízes, e com o dado acentual que faltava.

*(Uma armadilha de codificação custou a primeira contagem: o agudo do dataset é
**pré-composto** — `é` é U+00E9, não `e` + U+0301. Uma varredura ingênua por
caractere combinante acha 470 formas acentuadas em vez de 38.128. `stems.py`
normaliza para NFD antes de contar.)*

### 8.2 A *Abtönung*, medida

A tese de Brugmann: `*o` é o que sobra de um `*e` que perdeu o acento. Se ela
vale, `*o` tem de aparecer átono com mais frequência que `*e`.

| recorte | `*e` tôn / át | `*o` tôn / át | razão de chances | χ² |
|---|---|---|---|---|
| todas as posições | 25.817 / 20.460 | 9.228 / 20.766 | **2,84** | 4588 |
| **só a 1ª vogal (raiz)** | 21.078 / 5.207 | 7.153 / 5.603 | **3,17** | 2494 |
| não-primeiras (sufixos) | 4.739 / 15.253 | 2.075 / 15.163 | 2,27 | 843 |

Na linha de cima o efeito é forte, mas há um artefato óbvio à espreita: a
**vogal temática** é sufixal e átona quase por definição, e sozinha produziria
esse número. Por isso o recorte do meio, que só olha a vogal da raiz e portanto
a exclui.

**O efeito sobrevive, e cresce.** Em posição de raiz, `*o` é **3,2 vezes** mais
propenso a ser átono que `*e`, sobre 39.041 vogais. A *Abtönung* deixou de ser
uma regra que herdamos de fé.

Duas ressalvas, e são sérias:

- **Circularidade parcial.** As reconstruções do Wiktionary são feitas por
  indo-europeístas que *já assumem* a *Abtönung*. O corpus não é uma observação
  independente da tese; é a tese aplicada com consistência. O que o número mede
  de verdade é que a aplicação é **consistente** — o que não é nada, mas não é
  confirmação.
- **56 % do `*o` em posição de raiz continua tônico** (7.153 de 12.756) — a
  maioria. Para o relato de Brugmann isso é muita analogia a absorver. O que a
  medida mostra é uma **tendência forte**, não uma regra sem exceção: `*o` é
  três vezes mais propenso a ser átono que `*e`, e ainda assim é tônico na
  maior parte das vezes em que ocorre.

Para o projeto, o que importa é o sinal: a regra tem direção e magnitude
mensuráveis, e o Proto-Orogeniano pode implementá-la como perda de
arredondamento sob acento em vez de herdá-la pronta.

#### A segunda lei, e por que ela é separável

O documento 02 §3.4 não postula uma lei produzindo `*o`, postula **duas**:

1. a *Abtönung*, condicionada por **acento**;
2. `*-ē̆m` > `*-ō̆m` (Kloekhorst 2024), condicionada por **segmento** — diante
   de `*-m` final.

Isso é uma previsão forte, e não foi feita para ser testada: se as duas leis
existem e são condicionadas por coisas diferentes, elas têm de deixar
**rastros ortogonais**. A segunda, sendo segmental, deve ser *cega ao acento*.

Separando o contexto `_m` do resto, ainda só na 1ª vogal:

| 1ª vogal (raiz) | tônico | átono | % tônico |
|---|---|---|---|
| `*e` diante de `*m` | 445 | 89 | 83,3 % |
| `*e` em outro lugar | 20.633 | 5.118 | 80,1 % |
| **`*o` diante de `*m`** | **1.017** | **266** | **79,3 %** |
| **`*o` em outro lugar** | **6.136** | **5.337** | **53,5 %** |

**Diante de `*m` o efeito do acento desaparece.** `*o` fica tão tônico quanto
`*e` — 79,3 % contra 80,1 %, uma diferença de menos de um ponto. Fora desse
contexto, despenca para 53,5 %. E `*o` tônico é **6,8× enriquecido** diante de
`*m`: 14,2 % dos `*o` tônicos estão nesse contexto, contra 2,1 % dos `*e`
tônicos.

É exatamente a assinatura prevista. Uma lei segmental produz `*o` sem
consultar o acento, e é por isso que o contexto `_m` é o único onde `*o`
tônico é a norma e não a exceção.

Duas consequências:

- **A *Abtönung* fica mais nítida quando se controla pela outra lei.** Excluído
  o contexto `_m`, a razão de chances sobe de 3,17 para **3,51**. As duas leis
  estavam se contaminando na medição anterior.
- **Parte do débito dos 56 % é absorvida.** A segunda lei explica 14 % do `*o`
  tônico — e é precisamente o pedaço que ela foi postulada para cobrir. O resto
  continua sem explicação e continua sendo o ponto fraco do relato.

Vale registrar o que isso **não** é: as duas leis vieram das fontes (Brugmann e
Kloekhorst), não do corpus. A separação apareceu ao medir. É o caso mais
próximo de uma previsão fora da amostra que o projeto produziu até aqui — com a
mesma ressalva de circularidade da subseção anterior, que vale para as duas.

### 8.3 De onde vêm as vogais longas — correção do §7

§7 respondeu com raízes e acertou o veredito pelo motivo errado.

Confirmado, e agora com força muito maior:

> **Nenhum lema do corpus tem vogal longa invariável.** De 867 lemas, 592
> alternam longa~curta dentro do próprio paradigma e 275 não têm nenhuma longa.
> **Zero** são só-longa. E 2.025 das formas longas têm irmã curta de esqueleto
> idêntico no mesmo paradigma.

Não há um único item lexical que exija duração subjacente. Isso é o que §7
propôs, agora sobre 40.894 formas em vez de zero.

**O mecanismo, porém, não é o que §7 disse.** Cruzando cada forma longa com o
seu lema:

| origem da vogal longa | formas | % |
|---|---|---|
| lema tem laringal, a forma **perdeu** (alongamento compensatório) | 63 | **2 %** |
| lema tem laringal, a forma manteve | 1.017 | 32 % |
| lema **sem nenhuma laringal** | 2.087 | **66 %** |

Dois terços das vogais longas estão em palavras onde não há laringal alguma
para perder. A fonte está em outro lugar — e as etiquetas gramaticais dizem
onde:

| categoria | formas longas / total | taxa |
|---|---|---|
| **subjuntivo** | 1.653 / 3.686 | **44,8 %** |
| dual | 763 / 7.838 | 9,7 % |
| todo o resto | 751 / 29.370 | **2,6 %** |

O subjuntivo é **17 vezes** mais longo que a linha de base. É exatamente o que
se espera: o subjuntivo do PIE se forma acrescentando `*-e-` ao tema, e num tema
temático a vogal temática mais o `*-e-` **contraem** — `*-e/o-` + `*-e-` →
`*-ē/ō-`. O mesmo em `*-o-es` → `*-ōs` (nom.pl.), `*-o-eys` → `*-ōys`
(instr.pl.), `*-o-h₁` → `*-ō` (dual).

A categoria certa não é *compensatory lengthening* (Moore §16) — é **fusão**
(Moore §14), na fronteira de morfema. O alongamento compensatório existe, e a
Lei de Szemerényi é real, mas juntos são a minoria.

**Efeito sobre a proposta: executada.** `/eː/` saiu do inventário do
Proto-Orogeniano, que cai de **34 para 33 fonemas** com uma única vogal `/e/`.
A duração vocálica do PIE passa a ser inteiramente derivada, por **três**
mecanismos ordenados por peso: contração em fronteira de morfema (dominante),
perda de laringal, Lei de Szemerényi.

A execução tem duas consequências que valem registro:

- **`[±long]` vira traço exclusivamente consonantal.** O documento 02 §3.3
  vendia a duração como propriedade transversal do sistema; ela atravessa todo
  o consonantismo e para aí. A vogal recebe `[0long]` — inaplicável — e não
  `[−long]`. Nenhuma classe natural se perde: as três que citam `long` exigem
  `[−son]`.
- **A restrição migra da fonologia para a morfologia.** A fonte dominante de
  duração é contração em fronteira de morfema, o que não é questão de
  inventário: exige que o Proto-Orogeniano tenha temas terminados em vogal e
  desinências iniciadas por vogal. Isso passa às lições 5 e seguintes.

E o custo medido é zero: reinvertidas as 766 raízes sem `/eː/`, as três métricas
não se movem — 12 ilegais, 2 colisões, 9 sem correspondência, idênticas ao
baseline anterior. Era o previsto, já que nenhuma raiz exercia o contraste.

### 8.4 O que o corpus certo mudou

| pendência | estado antes | agora |
|---|---|---|
| *Abtönung* | "não testável neste corpus" | medida — razão **3,51** em posição de raiz, controlada pela lei segmental |
| `*-ē̆m` > `*-ō̆m` | postulada, nunca isolada | **isolada** — §8.2: diante de `*m` o efeito do acento some |
| vogais longas | "o corpus não pode testar isso" | medida, e a proposta **executada**: `/eː/` fora, 33 fonemas |
| grau zero | fora de alcance (precisa de paradigma) | **em alcance** — 592 paradigmas com alternância; não medido ainda |

A lição metodológica é a segunda deste documento a ter o mesmo formato do erro
da "supressão de 90 %" (§2.4): as duas vezes, o número não estava errado — a
**população** estava. Lá, o denominador; aqui, o corpus.

---

## O que falta

1. **Tarefa 4 do exercício**: dez palavras, dez mudanças aleatórias, e observar
   o que funde. É o único item do enunciado ainda em aberto.
2. **Grau zero.** Agora ao alcance (§8.4) e ainda não medido: 592 paradigmas
   exibem alternância. A pergunta é se a distribuição do grau zero é previsível
   pelo acento do mesmo modo que a da *Abtönung*. Não é exigência desta lição —
   é material da 5 em diante, onde a morfologia entra.
3. Tarefas 1 e 2 do exercício, que são drills genéricos sobre mudanças
   atestadas — sem relação com a conlang, como o exercício da Phonology 1.
