# Estudo — Perfis de Urheimat: Orogen ↔ Terra ↔ dados tipológicos

Passo *Study* da Aula 01. Material de pesquisa, **não** decisões de design.

**Fontes consultadas** (em `data/`):
- `dev-master.zip` = **PHOIBLE** (repo `phoible/dev`), 105.485 linhas de segmentos,
  2.176 glottocodes com inventário
- `wals-master.zip` = **WALS**, 3.574 línguas com coordenadas
- `grambank-master.zip` = **Grambank**, usado para ampliar a cobertura geográfica
- Índice geográfico unificado: **3.523 línguas** com lat/lon

Scripts: `scratchpad/regions.py`, `scratchpad/features.py`

---

## Ressalvas metodológicas

Registradas porque afetam a leitura dos números:

1. **Rótulos de família divergem entre WALS e Grambank** — `Austro-Asiatic`/`Austroasiatic`,
   `Niger-Congo`/`Atlantic-Congo`, `Trans-New Guinea`/`Nuclear Trans New Guinea`
   contam em dobro. As contagens de família estão **infladas**, sobretudo na Nova Guiné.
2. **`Altaic` é rótulo legado do WALS.** Túrcico, mongólico e tungúsico não são
   hoje aceitos como família única.
3. **Regiões são caixas lat/lon retangulares**, não fronteiras reais. A caixa da
   "estepe" inclui o Cáucaso Noroeste, o que infla ejetivas e uvulares ali.
4. **Tamanho de inventário no PHOIBLE depende da análise da fonte.** Hindi aparece
   com 71 consoantes porque a fonte trata aspiradas e retroflexas como fonemas
   independentes. Comparar médias entre regiões é válido; comparar línguas
   individuais entre fontes diferentes, não.
5. **Cobertura desigual**: Rift africano tem 67 línguas em PHOIBLE, Taiwan tem 5,
   Ártico tem 5. Percentuais em n pequeno são indicativos, não estatística.

---

## Tabela mestra

| Perfil (Orogen) | Análogo terrestre | Línguas | Famílias | fam/Mkm² | Inventário médio | Marca fonológica |
|---|---|---|---|---|---|---|
| Bacia Interior Seca de Selvana | **Estepe ponto-cáspia + Ásia Central** | 27 | 7 | 1,22 | 34,0C + 8,9V = 42,9 | uvulares 69%, ejetivas 44% *(inflado pelo Cáucaso NO na caixa)*, tom 0% |
| Corredor do Rio do Norte de Sirocca | **Vale do Nilo** | 15 | 5 | 2,17 | 32,5C + 9,0V = 41,8 | uvulares 67%, faringais 50%, tom 17% |
| Rio-Tronco SO de Meridia + delta | **Bacia do Indo** | 30 | 4 | 2,84 | 36,5C + 13,8V = 50,5 | retroflexas 80%, aspiradas 80%, vogais nasais 40% |
| Deltas NE/N de Selvana | **Deltas de monção do SE asiático** | 105 | 7 | 2,62 | 23,9C + 15,6V = 40,6 | aspiradas 91%, tom 28%, implosivas 28% |
| Interior Subártico de Borea | **Taiga Volga-Kama / Sibéria oc.** | 25 | 5 | 0,84 | 24,8C + 10,2V = 35,0 | retroflexas 38%, uvulares 23%, **tom 0%, ejetivas 0%** |
| Terras Altas Geladas de Borea | **Costa ártica** | 22 | 3 | 0,23 | 30,6C + 8,2V = 39,8 | uvulares 80%, **obstruintes laterais 80%**, ejetivas 60% |
| Lagos NO de Meridia | **Lagos do Rift africano** | 138 | 9 | 3,59 | 26,0C + 10,6V = 38,4 | **tom 55%**, implosivas 37%, cliques 3% |
| Refúgios montanos (todos) | **Cáucaso** | 49 | 8 | **18,20** | **41,3C** + 8,9V = 50,2 | **ejetivas 91%, uvulares 91%, faringais 57%**, tom 0% |
| Refúgios montanos (todos) | **Terras altas da Nova Guiné** | 239 | 40* | **54,36** | **14,5C** + 7,5V = 22,3 | quase nada marcado — o oposto do Cáucaso |
| Refúgios montanos (todos) | **Encosta himalaia** | 103 | 4 | 3,64 | 27,9C + 13,3V = 41,8 | aspiradas 82%, retroflexas 52%, vogais nasais 48% |
| *(lacuna em Orogen)* | **Taiwan** | 20 | 3 | 32,09 | 22,4C + 6,4V = 28,8 | retroflexas 80%, uvulares 60% *(n=5)* |
| Coração Árido de Sirocca | **Coração do Saara** | 6 | 2 | 0,42 | 23,7C + 14,7V = 38,3 | uvulares 67% — **e quase nenhuma língua** |

\* inflado por rótulos duplicados; a Nova Guiné continua sendo o lugar mais
fragmentado da Terra mesmo após correção.

### Linha de base global (PHOIBLE, n=2.176)

| ejetivas | implosivas | cliques | uvulares | faringais | retroflexas | aspiradas | vogais nasais | tom | obstr. laterais |
|---|---|---|---|---|---|---|---|---|---|
| 8% | 12% | 1% | 12% | 3% | 27% | 20% | 22% | 23% | 7% |

---

## Três achados que importam para o design

### 1. A geografia prevê densidade de famílias, não fonologia

O intervalo é de duas ordens de grandeza:

```
Nova Guiné (montanha)  54,4 fam/Mkm²   ┃████████████████████████
Taiwan (ilha)          32,1            ┃██████████████
Cáucaso (montanha)     18,2            ┃████████
Rift (lagos)            3,6            ┃█
Indo (rio)              2,8            ┃█
Nilo (rio)              2,2            ┃
Estepe (corredor)       1,2            ┃
Taiga (corredor)        0,8            ┃
Saara (barreira)        0,4            ┃
Ártico (barreira)       0,2            ┃
```

Refúgio montano é **15–50× mais denso** em famílias que corredor. Isso confirma
o item 5 do perfil recorrente: montanha preserva diversidade, corredor a apaga.

### 2. Mas "montanha" não prevê nada sobre os sons

Cáucaso e Nova Guiné são **ambos** refúgios montanos de altíssima densidade, e
são opostos fonológicos:

| | Cáucaso | Nova Guiné |
|---|---|---|
| consoantes médias | **41,3** | **14,5** |
| extremo | Archi 81C | Abau 9C |
| ejetivas | 91% | 0% |
| uvulares | 91% | 2% |
| faringais | 57% | 0% |

**Conclusão: a intuição de que "povo de montanha tem consoantes ásperas" não tem
apoio nos dados.** O que prevê o inventário é herança de família e contato areal,
não terreno. Para uma conlang naturalista *a priori*, isso é libertador: o
ambiente escolhido **não** obriga a nenhuma fonologia. Ele obriga a uma *história*.

### 3. Os traços marcados são areais, não geográficos

Todos os picos da tabela são *Sprachbünde* — espalham-se por contato, cruzando
fronteiras de família:

- **Ejetivas**: 8% global → 91% no Cáucaso, 60% no Ártico NO
- **Tom**: 23% global → 55% no Rift, 28% no SE asiático
- **Aspiração**: 20% global → 91% no SE asiático, 82% no Himalaia, 80% no Indo
- **Retroflexas**: 27% global → 80% no Indo, 52% no Himalaia
- **Faringais**: 3% global → 57% no Cáucaso, 50% no Nilo
- **Obstruintes laterais**: 7% global → 80% no Ártico
- **Cliques**: 1% global → sobrevivem só no Rift (3%) e na África austral

Consequência direta para uma conlang: **um traço marcado isolado parece
arbitrário; um bloco de traços marcados compartilhados com vizinhos parece
história.** É a diferença entre *kitchen sink* e área linguística.

---

## A lacuna do Saara

Seis línguas em 4,73 Mkm². O deserto profundo não é berço nem refúgio — é vazio
com corredores nas bordas. Aplicado a Orogen: o **Coração Árido de Sirocca** (46%
Köppen B) deve ser lido como *barreira*, e toda a vida linguística do continente
se concentra no **Corredor do Rio do Norte** e na costa SO úmida. `INTERPRETED`

O mesmo vale para a costa ártica: 0,23 fam/Mkm², a mais baixa da amostra. As
**Terras Altas Geladas do Norte** de Borea sustentam no máximo uma família
especialista e pequena — como o esquimó-aleúte.

---

## Implicação para Orogen

Orogen tem **32% da terra acima de 2 km** e **~25% Köppen B** `MEASURED`. Pelos
números acima, isso projeta um planeta com:

- muitas famílias pequenas nos cinturões montanhosos (perfil Nova Guiné/Cáucaso)
- poucas famílias grandes, restritas aos corredores fluviais e à Bacia Interior
  Seca de Selvana
- vazios linguísticos no Coração Árido de Sirocca e na franja polar de Borea
- fronteira genealógica profunda entre o par Ocidental e o par Oriental, dada
  pela travessia *Hard* do Oceano Oriental

`INTERPRETED` — nada disso é canon; é o que os dados terrestres projetariam sobre
a geografia travada.
