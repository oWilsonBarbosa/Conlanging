# Proto-Orogeniano — mudança sonora

**Conlangs University · Phonology 4 — "Sound change"**

> **Em andamento.** Este documento começou com a montagem do banco de provas e
> a primeira medição. A derivação ordenada ainda não foi escrita.

| | |
|---|---|
| Lição | Phonology 4 (Jasper, maio 2020) — a mais longa do curso |
| Ferramenta | [`tools/po-derivation/`](../tools/po-derivation/) |
| Estado | §1 e §2 fechados; §3 em diante pendente |

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
manual, no ambiente onde mais comumente ocorrem.** A derivação
Proto-Orogeniano → PIE clássico não precisa de nenhuma mudança exótica — só
das duas mais banais da taxonomia, na ordem certa.

---

## O que falta

1. **Ordenar as regras** e escrever a derivação completa.
2. Classificar as regras sincrônicas do documento 03 §4 nas categorias da
   lição — tarefa 3 do exercício.
3. As duas leis que produzem `*o`: *Abtönung* e `*-ē̆m` > `*-ō̆m`. **Obstáculo
   conhecido:** as raízes do dataset são citadas sem acento, e a *Abtönung* é
   condicionada por acento. Sem dado acentual, essa regra não é testável neste
   corpus.
4. Tarefa 4 do exercício: dez palavras, dez mudanças aleatórias, e observar o
   que funde.
