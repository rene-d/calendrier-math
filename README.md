# Calendrier Mathématique

Solutions personnelles aux questions du [Calendrier Mathématique 2022](https://www.pug.fr/produit/1944/9782706147852/calendrier-mathematique-2022)

[![source code](https://img.shields.io/static/v1?label=GitHub&message=code%20source&color=blue&style=for-the-badge&logo=github)](https://github.com/rene-d/calendrier-math)

J'essaie de vérifier au maximum l'exactitude et la précision des démonstrations. Elles sont pour la plupart d'ailleurs similaires à celles du livret. Cependant des erreurs peuvent subsister (erreur de raisonnement, théorème non cité ou trop compliqué, outils mathématiques trop évolués, etc.). Les solutions officielles sont uniquement celles publiées avec le calendrier.

Certains défis parmi ceux proposés peuvent se résoudre (ou plutôt se vérifier) à l'aide d'un petit programme en [Python](https://www.python.org) mais aussi en [Rust](http://rust-lang.org). Ils sont identifiés par l'icône 🖥. [WolframAlpha](https://www.wolframalpha.com) et [GeoGebra](https://www.geogebra.org/calculator) sont également très souvent utilisés.

Elles sont principalement rédigées en [Markdown](https://guides.github.com/features/mastering-markdown/) et [Unicode](https://en.wikipedia.org/wiki/Mathematical_operators_and_symbols_in_Unicode) qui offrent une mise en page suffisante. Cependant, quelques problèmes nécessitent des équations un peu plus complexes et les solutions utilisent [LaTeX](https://www.latex-project.org) (avec ce [hack](https://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b), référence [katex](https://katex.org), extension Visual Studio Code [Markdown+Math](https://marketplace.visualstudio.com/items?itemName=goessner.mdmath)). La mise en page est assurée par un _hook_ Git qui crée automatiquement les calendriers mensuels, ajoute ou enlève les scripts Python et l'encodage des équations LaTeX (`./readme.py -X -P` pour supprimer la mise en page Python/LaTeX).

Les programmes Python peuvent être lancés en script, interactivement, ou en ligne: [Python](https://www.python.org/shell/), [Rust](https://play.rust-lang.org), [programiz](https://www.programiz.com/python-programming/online-compiler/), [repl.it](https://repl.it/), etc.

Même si le recours à l'informatique n'est pas l'objectif du calendrier, cela a malgré tout deux intérêts:

- savoir passer d'un problème mathématique à un code informatique, notamment apprendre à utiliser des bibliothèques de programmation et scientifiques
- aider à la résolution d'un problème mathématique à l'aide d'outils, pouvoir tester et vérifier les formules et algorithmes

Par ailleurs, chaque semaine, le [CNRS](https://portail.math.cnrs.fr) propose un de ces défis: [Défis du calendrier mathématique](https://images.math.cnrs.fr/-Defis-du-Calendrier-mathematique-.html), et la solution de la semaine précédente.

## Années précédentes

[Calendrier Mathématique 2021](2021/README.md)

[Calendrier Mathématique 2020](2020/README.md)

## Solutions 2022

![148/260](https://img.shields.io/static/v1?label=solutions&message=148/260%20%2857%25%29&color=blueviolet&style=flat-square)

### Janvier

[![21/21](https://img.shields.io/static/v1?label=fini&message=21/21&color=success&style=flat-square)](2022/janvier/)

|Lundi|Mardi|Mercredi|Jeudi|Vendredi|Samedi|Dimanche|
|---|---|---|---|---|---|---|
|    |    |    |    |    | *01* | *02* |
| [03](2022/janvier/README.md#lundi-3-janvier) | [04](2022/janvier/README.md#mardi-4-janvier) | [05](2022/janvier/README.md#mercredi-5-janvier) | [06](2022/janvier/README.md#jeudi-6-janvier) | [07](2022/janvier/README.md#vendredi-7-janvier) | *08* | *09* |
| [10](2022/janvier/README.md#lundi-10-janvier) | [11](2022/janvier/README.md#mardi-11-janvier) | [12](2022/janvier/README.md#mercredi-12-janvier) | [13](2022/janvier/README.md#jeudi-13-janvier) | [14](2022/janvier/README.md#vendredi-14-janvier) | *15* | *16* |
| [17](2022/janvier/README.md#lundi-17-janvier) | [18](2022/janvier/README.md#mardi-18-janvier) 🖥 | [19](2022/janvier/README.md#mercredi-19-janvier) | [20](2022/janvier/README.md#jeudi-20-janvier) | [21](2022/janvier/README.md#vendredi-21-janvier) 🖥 | *22* | *23* |
| [24](2022/janvier/README.md#lundi-24-janvier) | [25](2022/janvier/README.md#mardi-25-janvier) | [26](2022/janvier/README.md#mercredi-26-janvier) | [27](2022/janvier/README.md#jeudi-27-janvier) | [28](2022/janvier/README.md#vendredi-28-janvier) | *29* | *30* |
| [31](2022/janvier/README.md#lundi-31-janvier) |    |    |    |    |    |    |

### Février

[![20/20](https://img.shields.io/static/v1?label=fini&message=20/20&color=success&style=flat-square)](2022/fevrier/)

|Lundi|Mardi|Mercredi|Jeudi|Vendredi|Samedi|Dimanche|
|---|---|---|---|---|---|---|
|    | [01](2022/fevrier/README.md#mardi-1-février) | [02](2022/fevrier/README.md#mercredi-2-février) | [03](2022/fevrier/README.md#jeudi-3-février) | [04](2022/fevrier/README.md#vendredi-4-février) 🖥 | *05* | *06* |
| [07](2022/fevrier/README.md#lundi-7-février) | [08](2022/fevrier/README.md#mardi-8-février) | [09](2022/fevrier/README.md#mercredi-9-février) | [10](2022/fevrier/README.md#jeudi-10-février) | [11](2022/fevrier/README.md#vendredi-11-février) 🖥 | *12* | *13* |
| [14](2022/fevrier/README.md#lundi-14-février) | [15](2022/fevrier/README.md#mardi-15-février) 🖥 | [16](2022/fevrier/README.md#mercredi-16-février) | [17](2022/fevrier/README.md#jeudi-17-février) | [18](2022/fevrier/README.md#vendredi-18-février) | *19* | *20* |
| [21](2022/fevrier/README.md#lundi-21-février) | [22](2022/fevrier/README.md#mardi-22-février) | [23](2022/fevrier/README.md#mercredi-23-février) 🖥 | [24](2022/fevrier/README.md#jeudi-24-février) | [25](2022/fevrier/README.md#vendredi-25-février) | *26* | *27* |
| [28](2022/fevrier/README.md#lundi-28-février) |    |    |    |    |    |    |

### Mars

[![23/23](https://img.shields.io/static/v1?label=fini&message=23/23&color=success&style=flat-square)](2022/mars/)

|Lundi|Mardi|Mercredi|Jeudi|Vendredi|Samedi|Dimanche|
|---|---|---|---|---|---|---|
|    | [01](2022/mars/README.md#mardi-1-mars) | [02](2022/mars/README.md#mercredi-2-mars) | [03](2022/mars/README.md#jeudi-3-mars) | [04](2022/mars/README.md#vendredi-4-mars) | *05* | *06* |
| [07](2022/mars/README.md#lundi-7-mars) | [08](2022/mars/README.md#mardi-8-mars) | [09](2022/mars/README.md#mercredi-9-mars) | [10](2022/mars/README.md#jeudi-10-mars) | [11](2022/mars/README.md#vendredi-11-mars) | *12* | *13* |
| [14](2022/mars/README.md#lundi-14-mars) | [15](2022/mars/README.md#mardi-15-mars) | [16](2022/mars/README.md#mercredi-16-mars) | [17](2022/mars/README.md#jeudi-17-mars) | [18](2022/mars/README.md#vendredi-18-mars) | *19* | *20* |
| [21](2022/mars/README.md#lundi-21-mars) | [22](2022/mars/README.md#mardi-22-mars) | [23](2022/mars/README.md#mercredi-23-mars) 🖥 | [24](2022/mars/README.md#jeudi-24-mars) | [25](2022/mars/README.md#vendredi-25-mars) | *26* | *27* |
| [28](2022/mars/README.md#lundi-28-mars) | [29](2022/mars/README.md#mardi-29-mars) | [30](2022/mars/README.md#mercredi-30-mars) | [31](2022/mars/README.md#jeudi-31-mars) |    |    |    |

### Avril

[![21/21](https://img.shields.io/static/v1?label=fini&message=21/21&color=success&style=flat-square)](2022/avril/)

|Lundi|Mardi|Mercredi|Jeudi|Vendredi|Samedi|Dimanche|
|---|---|---|---|---|---|---|
|    |    |    |    | [01](2022/avril/README.md#vendredi-1-avril) | *02* | *03* |
| [04](2022/avril/README.md#lundi-4-avril) | [05](2022/avril/README.md#mardi-5-avril) | [06](2022/avril/README.md#mercredi-6-avril) | [07](2022/avril/README.md#jeudi-7-avril) | [08](2022/avril/README.md#vendredi-8-avril) | *09* | *10* |
| [11](2022/avril/README.md#lundi-11-avril) | [12](2022/avril/README.md#mardi-12-avril) | [13](2022/avril/README.md#mercredi-13-avril) | [14](2022/avril/README.md#jeudi-14-avril) | [15](2022/avril/README.md#vendredi-15-avril) | *16* | *17* |
| [18](2022/avril/README.md#lundi-18-avril) | [19](2022/avril/README.md#mardi-19-avril) 🖥 | [20](2022/avril/README.md#mercredi-20-avril) | [21](2022/avril/README.md#jeudi-21-avril) 🖥 | [22](2022/avril/README.md#vendredi-22-avril) 🖥 | *23* | *24* |
| [25](2022/avril/README.md#lundi-25-avril) | [26](2022/avril/README.md#mardi-26-avril) | [27](2022/avril/README.md#mercredi-27-avril) | [28](2022/avril/README.md#jeudi-28-avril) | [29](2022/avril/README.md#vendredi-29-avril) 🖥 | *30* |    |

### Mai

[![22/22](https://img.shields.io/static/v1?label=fini&message=22/22&color=success&style=flat-square)](2022/mai/)

|Lundi|Mardi|Mercredi|Jeudi|Vendredi|Samedi|Dimanche|
|---|---|---|---|---|---|---|
|    |    |    |    |    |    | *01* |
| [02](2022/mai/README.md#lundi-2-mai) | [03](2022/mai/README.md#mardi-3-mai) | [04](2022/mai/README.md#mercredi-4-mai) | [05](2022/mai/README.md#jeudi-5-mai) | [06](2022/mai/README.md#vendredi-6-mai) | *07* | *08* |
| [09](2022/mai/README.md#lundi-9-mai) | [10](2022/mai/README.md#mardi-10-mai) | [11](2022/mai/README.md#mercredi-11-mai) | [12](2022/mai/README.md#jeudi-12-mai) | [13](2022/mai/README.md#vendredi-13-mai) | *14* | *15* |
| [16](2022/mai/README.md#lundi-16-mai) | [17](2022/mai/README.md#mardi-17-mai) | [18](2022/mai/README.md#mercredi-18-mai) | [19](2022/mai/README.md#jeudi-19-mai) | [20](2022/mai/README.md#vendredi-20-mai) | *21* | *22* |
| [23](2022/mai/README.md#lundi-23-mai) | [24](2022/mai/README.md#mardi-24-mai) | [25](2022/mai/README.md#mercredi-25-mai) | [26](2022/mai/README.md#jeudi-26-mai) | [27](2022/mai/README.md#vendredi-27-mai) | *28* | *29* |
| [30](2022/mai/README.md#lundi-30-mai) | [31](2022/mai/README.md#mardi-31-mai) |    |    |    |    |    |

### Juin

[![22/22](https://img.shields.io/static/v1?label=fini&message=22/22&color=success&style=flat-square)](2022/juin/)

|Lundi|Mardi|Mercredi|Jeudi|Vendredi|Samedi|Dimanche|
|---|---|---|---|---|---|---|
|    |    | [01](2022/juin/README.md#mercredi-1-juin) | [02](2022/juin/README.md#jeudi-2-juin) | [03](2022/juin/README.md#vendredi-3-juin) | *04* | *05* |
| [06](2022/juin/README.md#lundi-6-juin) | [07](2022/juin/README.md#mardi-7-juin) | [08](2022/juin/README.md#mercredi-8-juin) | [09](2022/juin/README.md#jeudi-9-juin) | [10](2022/juin/README.md#vendredi-10-juin) | *11* | *12* |
| [13](2022/juin/README.md#lundi-13-juin) | [14](2022/juin/README.md#mardi-14-juin) | [15](2022/juin/README.md#mercredi-15-juin) | [16](2022/juin/README.md#jeudi-16-juin) | [17](2022/juin/README.md#vendredi-17-juin) | *18* | *19* |
| [20](2022/juin/README.md#lundi-20-juin) | [21](2022/juin/README.md#mardi-21-juin) | [22](2022/juin/README.md#mercredi-22-juin) | [23](2022/juin/README.md#jeudi-23-juin) | [24](2022/juin/README.md#vendredi-24-juin) | *25* | *26* |
| [27](2022/juin/README.md#lundi-27-juin) | [28](2022/juin/README.md#mardi-28-juin) | [29](2022/juin/README.md#mercredi-29-juin) | [30](2022/juin/README.md#jeudi-30-juin) |    |    |    |

### Juillet

[![19/21](https://img.shields.io/static/v1?label=en%20cours&message=19/21&color=informational&style=flat-square)](2022/juillet/)

|Lundi|Mardi|Mercredi|Jeudi|Vendredi|Samedi|Dimanche|
|---|---|---|---|---|---|---|
|    |    |    |    | [01](2022/juillet/README.md#vendredi-1-juillet) | *02* | *03* |
| [04](2022/juillet/README.md#lundi-4-juillet) | [05](2022/juillet/README.md#mardi-5-juillet) | [06](2022/juillet/README.md#mercredi-6-juillet) | [07](2022/juillet/README.md#jeudi-7-juillet) | [08](2022/juillet/README.md#vendredi-8-juillet) | *09* | *10* |
| [11](2022/juillet/README.md#lundi-11-juillet) | [12](2022/juillet/README.md#mardi-12-juillet) | [13](2022/juillet/README.md#mercredi-13-juillet) | [14](2022/juillet/README.md#jeudi-14-juillet) | [15](2022/juillet/README.md#vendredi-15-juillet) | *16* | *17* |
| [18](2022/juillet/README.md#lundi-18-juillet) | [19](2022/juillet/README.md#mardi-19-juillet) | [20](2022/juillet/README.md#mercredi-20-juillet) | [21](2022/juillet/README.md#jeudi-21-juillet) | 22 | *23* | *24* |
| [25](2022/juillet/README.md#lundi-25-juillet) | [26](2022/juillet/README.md#mardi-26-juillet) | 27 | [28](2022/juillet/README.md#jeudi-28-juillet) | [29](2022/juillet/README.md#vendredi-29-juillet) | *30* | *31* |

