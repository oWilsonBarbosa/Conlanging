# Lista de conceitos para o léxico

Seleção dos conceitos mais **comuns, menos emprestados e mais antigos** — a base mais
segura para cunhar raízes *nativas* e herdadas de uma língua, em vez de tratá-las como
empréstimos.

## Fonte e método

- **Lista:** Tadmor (2009), a *Leipzig-Jakarta list* — via Concepticon `Tadmor-2009-100`
  (`data/concepticon-data-3.4.0.zip`).
- **Base empírica:** 1.460 significados levantados em 41 línguas. Estes 100 conceitos
  são os mais **resistentes a empréstimo** e os mais **estáveis/reconstruíveis** no tempo.

### Colunas

| Coluna | Significado |
|--------|-------------|
| `borrowed_score` | Maior = **menos** emprestado entre línguas (mais resistente a empréstimo). |
| `age_score` | Maior = **mais antigo** / reconstruível a proto-estágios profundos. |
| `composite_score` | Estabilidade geral (combina os fatores acima) — define o ranking. |

> **`fire` (fogo) é o #1** — o conceito mais estável do mundo e também o #1 em idade
> (0.939). É o melhor candidato possível a raiz herdada.

A versão pronta para semear o léxico está em [`concept-list.csv`](concept-list.csv),
com colunas vazias `form` e `notes` para preencher conforme as raízes forem cunhadas.

## Os 100 conceitos (ordenados por estabilidade)

| # | Conceito | Concepticon | Menos-emprest. | Idade | Composto |
|--:|----------|------------:|---------------:|------:|---------:|
| 1 | fire | `FIRE` (221) | 0.965 | 0.939 | 0.901 |
| 2 | nose | `NOSE` (1221) | 0.973 | 0.906 | 0.864 |
| 3 | to go | `GO` (695) | 0.963 | 0.887 | 0.832 |
| 4 | water | `WATER` (948) | 0.909 | 0.926 | 0.831 |
| 5 | mouth | `MOUTH` (674) | 0.920 | 0.904 | 0.817 |
| 6 | tongue | `TONGUE` (1205) | 0.934 | 0.908 | 0.808 |
| 7 | blood | `BLOOD` (946) | 0.904 | 0.890 | 0.805 |
| 8 | bone | `BONE` (1394) | 0.918 | 0.904 | 0.805 |
| 9 | 2sg pronoun | `THOU` (1215) | 0.958 | 0.893 | 0.798 |
| 10 | root | `ROOT` (670) | 0.944 | 0.869 | 0.798 |
| 11 | to come | `COME` (1446) | 0.968 | 0.876 | 0.796 |
| 12 | breast | `BREAST` (1402) | 0.947 | 0.856 | 0.783 |
| 13 | rain | `RAIN (PRECIPITATION)` (658) | 0.916 | 0.898 | 0.782 |
| 14 | 1sg pronoun | `I` (1209) | 0.970 | 0.875 | 0.776 |
| 15 | louse | `LOUSE` (1392) | 0.950 | 0.861 | 0.774 |
| 16 | name | `NAME` (1405) | 0.915 | 0.886 | 0.774 |
| 17 | wing | `WING` (1257) | 0.884 | 0.904 | 0.773 |
| 18 | flesh/meat | `FLESH OR MEAT` (2615) | 0.877 | 0.892 | 0.771 |
| 19 | arm/hand | `ARM OR HAND` (2121) | 0.881 | 0.903 | 0.768 |
| 20 | fly | `FLY (INSECT)` (1504) | 0.948 | 0.858 | 0.766 |
| 21 | night | `NIGHT` (1233) | 0.931 | 0.880 | 0.766 |
| 22 | ear | `EAR` (1247) | 0.896 | 0.888 | 0.764 |
| 23 | far | `FAR` (1406) | 0.944 | 0.850 | 0.760 |
| 24 | neck | `NECK` (1333) | 0.895 | 0.881 | 0.760 |
| 25 | to do/make | `DO OR MAKE` (2575) | 0.947 | 0.877 | 0.759 |
| 26 | house | `HOUSE` (1252) | 0.893 | 0.876 | 0.758 |
| 27 | stone/rock | `STONE OR ROCK` (2125) | 0.895 | 0.882 | 0.756 |
| 28 | bitter | `BITTER` (887) | 0.975 | 0.872 | 0.755 |
| 29 | to say | `SAY` (1458) | 0.972 | 0.837 | 0.755 |
| 30 | tooth | `TOOTH` (1380) | 0.882 | 0.877 | 0.755 |
| 31 | hair | `HAIR` (1040) | 0.944 | 0.871 | 0.754 |
| 32 | big | `BIG` (1202) | 0.889 | 0.864 | 0.753 |
| 33 | one | `ONE` (1493) | 0.870 | 0.893 | 0.753 |
| 34 | 3sg pronoun | `HE OR SHE OR IT` (262) | 1.000 | 0.893 | 0.749 |
| 35 | who? | `WHO` (1235) | 0.968 | 0.838 | 0.749 |
| 36 | to hit/beat | `STRIKE OR BEAT` (2133) | 0.955 | 0.827 | 0.748 |
| 37 | leg/foot | `FOOT OR LEG` (2098) | 0.856 | 0.897 | 0.747 |
| 38 | fish | `FISH` (227) | 0.855 | 0.885 | 0.745 |
| 39 | horn | `HORN (ANATOMY)` (1393) | 0.840 | 0.898 | 0.745 |
| 40 | this | `THIS` (1214) | 1.000 | 0.851 | 0.745 |
| 41 | yesterday | `YESTERDAY` (1174) | 0.958 | 0.843 | 0.744 |
| 42 | black | `BLACK` (163) | 0.951 | 0.866 | 0.741 |
| 43 | navel | `NAVEL` (1838) | 0.878 | 0.860 | 0.741 |
| 44 | to drink | `DRINK` (1401) | 0.904 | 0.877 | 0.741 |
| 45 | to stand | `STAND` (1442) | 0.981 | 0.847 | 0.738 |
| 46 | back | `BACK` (1291) | 0.918 | 0.868 | 0.736 |
| 47 | to bite | `BITE` (1403) | 0.964 | 0.861 | 0.736 |
| 48 | wind | `WIND` (960) | 0.828 | 0.900 | 0.736 |
| 49 | smoke | `SMOKE (EXHAUST)` (778) | 0.916 | 0.863 | 0.734 |
| 50 | what? | `WHAT` (1236) | 0.971 | 0.804 | 0.732 |
| 51 | child (kin term) | `CHILD (DESCENDANT)` (1801) | 0.929 | 0.866 | 0.730 |
| 52 | egg | `EGG` (744) | 0.910 | 0.846 | 0.728 |
| 53 | new | `NEW` (1231) | 0.920 | 0.860 | 0.727 |
| 54 | to burn (intr.) | `BURNING` (1428) | 0.951 | 0.860 | 0.727 |
| 55 | to give | `GIVE` (1447) | 0.913 | 0.878 | 0.727 |
| 56 | good | `GOOD` (1035) | 0.893 | 0.860 | 0.726 |
| 57 | not | `NOT` (1240) | 0.965 | 0.880 | 0.726 |
| 58 | to know | `KNOW` (3626) | 0.933 | 0.856 | 0.725 |
| 59 | knee | `KNEE` (1371) | 0.911 | 0.862 | 0.724 |
| 60 | sand | `SAND` (671) | 0.901 | 0.866 | 0.724 |
| 61 | to hear | `HEAR` (1408) | 0.953 | 0.848 | 0.723 |
| 62 | to laugh | `LAUGH` (1355) | 0.942 | 0.844 | 0.723 |
| 63 | soil | `EARTH (SOIL)` (1228) | 0.900 | 0.883 | 0.722 |
| 64 | leaf | `LEAF` (628) | 0.897 | 0.823 | 0.721 |
| 65 | red | `RED` (156) | 0.926 | 0.864 | 0.721 |
| 66 | liver | `LIVER` (1224) | 0.869 | 0.857 | 0.720 |
| 67 | skin/hide | `SKIN` (763) | 0.889 | 0.875 | 0.718 |
| 68 | to hide | `HIDE` (2486) | 0.928 | 0.847 | 0.718 |
| 69 | to suck | `SUCK` (1421) | 0.940 | 0.860 | 0.718 |
| 70 | to carry | `CARRY` (700) | 0.919 | 0.838 | 0.717 |
| 71 | ant | `ANT` (587) | 0.865 | 0.850 | 0.716 |
| 72 | heavy | `HEAVY` (1210) | 0.911 | 0.874 | 0.716 |
| 73 | to take | `TAKE` (1749) | 0.900 | 0.898 | 0.716 |
| 74 | old | `OLD` (1229) | 0.896 | 0.867 | 0.715 |
| 75 | to eat | `EAT` (1336) | 0.920 | 0.840 | 0.714 |
| 76 | thick | `THICK` (1244) | 0.950 | 0.827 | 0.712 |
| 77 | thigh | `UPPER LEG (THIGH)` (471) | 0.906 | 0.856 | 0.712 |
| 78 | long | `LONG` (1203) | 0.956 | 0.824 | 0.707 |
| 79 | to blow | `BLOW (OF WIND)` (175) | 0.962 | 0.857 | 0.706 |
| 80 | wood | `WOOD` (1803) | 0.860 | 0.871 | 0.705 |
| 81 | to fall | `FALL` (1280) | 0.946 | 0.825 | 0.704 |
| 82 | to run | `RUN` (1519) | 0.976 | 0.833 | 0.704 |
| 83 | eye | `EYE` (1248) | 0.904 | 0.847 | 0.703 |
| 84 | ash | `ASH` (646) | 0.853 | 0.891 | 0.699 |
| 85 | dog | `DOG` (2009) | 0.838 | 0.869 | 0.699 |
| 86 | tail | `TAIL` (1220) | 0.883 | 0.813 | 0.699 |
| 87 | to cry/weep | `CRY` (1839) | 0.871 | 0.871 | 0.698 |
| 88 | to tie | `TIE` (1917) | 0.879 | 0.836 | 0.697 |
| 89 | sweet | `SWEET` (717) | 0.914 | 0.857 | 0.695 |
| 90 | to see | `SEE` (1409) | 0.918 | 0.842 | 0.695 |
| 91 | bird | `BIRD` (937) | 0.842 | 0.857 | 0.694 |
| 92 | rope | `ROPE` (1218) | 0.848 | 0.824 | 0.694 |
| 93 | salt | `SALT` (1274) | 0.848 | 0.838 | 0.694 |
| 94 | shade/shadow | `SHADE` (1388) | 0.887 | 0.840 | 0.694 |
| 95 | small | `SMALL` (1246) | 0.909 | 0.790 | 0.694 |
| 96 | wide | `WIDE` (1243) | 0.955 | 0.819 | 0.692 |
| 97 | in | `IN` (1460) | 0.948 | 0.856 | 0.691 |
| 98 | star | `STAR` (1430) | 0.830 | 0.859 | 0.691 |
| 99 | hard | `HARD` (1884) | 0.918 | 0.833 | 0.690 |
| 100 | to crush/grind | `GRIND` (1033) | 0.919 | 0.845 | 0.688 |

