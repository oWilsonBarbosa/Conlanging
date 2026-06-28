# Validação contra o Glottolog (estágio 1)

Confronto de `fire-by-family.md` com o **Glottolog** (CLDF `languages.csv`, `glottolog/glottolog-cldf`). Anexa o **glottocode**, confere a família atribuída à mão
e sinaliza divergências. **Não-destrutivo** — nada nos arquivos curados foi alterado.
Mapeamento completo (inclusive não-casados) em [`glottolog-map.csv`](glottolog-map.csv).

- Nomes confrontados: **531**
- Casaram por nome: **408** (76%) — sem match: **123**
- Dos casados: **346** família OK · **5** DIFERE · **0** AMBÍGUO (homônimo) · **57** rótulo areal

> Match por nome exato (normalizado), **sensível ao contexto**: entre homônimos escolhe-se
> a candidata cuja família bate com a nossa; pseudo-famílias do Glottolog (*Bookkeeping*,
> *Spurious*…) são descartadas. O Glottolog costuma **dividir** o que listamos como uma
> língua (Armenian → Eastern/Western Armenian), o que explica a cauda de não-casados.

## Divergências de família (revisar)

Casamento confiável (nome único), mas família difere. Pode ser (a) erro nosso, ou (b)
só **nomenclatura** do Glottolog — ex.: ele aposentou *Niger-Congo* (usa **Atlantic-Congo**),
chama *Kra-Dai* de **Tai-Kadai**, *NW Caucasian* de **Abkhaz-Adyge**, e trata *Omótico*,
*Mande* e *Pama-Nyungan* como famílias independentes.

| Língua | nossa família | família no Glottolog | glottocode |
|---|---|---|---|
| Wolaytta | Afro-Asiatic | Ta-Ne-Omotic | `wola1242` |
| Wu | Sino-Tibetan | Austroasiatic | `wuuu1240` |
| Isan | Kra-Dai (Tai-Kadai) | Nuclear Trans New Guinea | `isan1244` |
| Duun | Niger-Congo | Mande | `duun1245` |
| Samo | Niger-Congo | East Strickland | `samo1303` |

## Casamentos ambíguos (0) — homônimos, conferir manualmente

O nome existe em mais de um languoid e **nenhum** está na família esperada; a candidata
escolhida (abaixo) pode ser homônimo não-relacionado. Verificar antes de confiar no glottocode.


## Não-casados (123) — pendentes de mapeamento manual

Maioria por granularidade/alternância de nome no Glottolog. Resolver depois (estágio 2).

Zealandic, Alemannic German, East Central German (Silesian), Luxembourgish, Vilamovian, Yiddish, North Frisian (Föhr-Amrum), Saterland Frisian, West Frisian, Norn, Franco-Provençal, Old Occitan, Emilian, Piedmontese, Venetan, Neapolitan, Tarantino, Sardinian, Old East Slavic, Carpathian Rusyn, Pannonian Rusyn, Old Slovak, Old Church Slavonic, Serbo-Croatian, Slovene, Latgalian, Punjabi, Sinhalese, Middle Persian, Iranian Persian, Zazaki, Talysh, Tat, Baluchi, Ossetian, Yaghnobi, Yazghulami, Ancient Greek, Armenian, Luwian, Tocharian A, Tocharian B, Syriac, Hebrew, Central Atlas Tamazight, Tarifit, Oromo, Livonian, Akkala Sami, Inari Sami, Kildin Sami, Lule Sami, Northern Sami, Pite Sami, Skolt Sami, Southern Sami, Ter Sami, Ume Sami, Eastern Khanty, Azerbaijani, Kyrgyz, Uyghur, Yakut, Shor, Tuvan, Buryat, Daur, Mandarin, Eastern Min, Hokkien, Hakka, Sherpa, Nuosu, Lutuv, Zhuang, White Hmong, Khmer, Asi, Central Bikol, Rinconada Bikol, Ilocano, Waray-Waray, Indonesian, Bakung, Karo Batak, Toba Batak, Bau Bidayuh, Old Javanese, Rapa Nui, Tokelauan, Tongan, Makasae, East Circassian (Kabardian), Dargwa, Kaitag, Lezgi, Itelmen, Greenlandic, Inuktitut, Sotho, Chichewa, Kitembo, Lingala, Moore, Nafaanra, Kanuri, ǃXóõ, Mohegan-Pequot, Ojibwe, Quechua, Aymara, Amondawa, Old Tupi, Canela, Lushootseed (Salishan), Ngarrindjeri, Antillean Creole, Haitian Creole, Guinea-Bissau Creole, Korlai Creole Portuguese, Kristang, Jamaican Creole, Yilan Creole

