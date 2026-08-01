# Proto-Orogeniano — mudança sonora

**Conlangs University · Phonology 4 — "Sound change"**

> **Em andamento.** Banco de provas, medição, ordenação e a tarefa 3 do
> exercício estão feitos. Faltam as leis vocálicas e a tarefa 4.

| | |
|---|---|
| Lição | Phonology 4 (Jasper, maio 2020) — a mais longa do curso |
| Ferramenta | [`tools/po-derivation/`](../tools/po-derivation/) |
| Estado | §1–§5 fechados; leis vocálicas e tarefa 4 pendentes |

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

## O que falta

1. As duas leis que produzem `*o`: *Abtönung* e `*-ē̆m` > `*-ō̆m`. **Obstáculo
   conhecido:** as raízes do dataset são citadas sem acento, e a *Abtönung* é
   condicionada por acento. Sem dado acentual, essa regra não é testável neste
   corpus.
2. Tarefa 4 do exercício: dez palavras, dez mudanças aleatórias, e observar o
   que funde.
3. Tarefas 1 e 2 do exercício, que são drills genéricos sobre mudanças
   atestadas — sem relação com a conlang, como o exercício da Phonology 1.
