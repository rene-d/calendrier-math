# Calendrier Mathématique Novembre 2020

[Solutions 2020](../README.md) - [Homepage](https://rene-d.github.io/calendrier-math/)

## Lundi 2 Novembre

> réponse: 8

## Mardi 3 Novembre

√2 + √3 - 1 - √6

= √2 + √3 - 1 - √2 √3

= a + b - ab - 1

= (1 - a)(b - 1)

= (1 - √2)(√3 - 1) < 0

> réponse: 1 + 1 / √6

## Mercredi 4 Novembre

![latexml](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Baligned%7D%0Ax%5E3%2By%5E3%20%3D%2040%20%5C%5C%0Ax%5E2y%2Bxy%5E2%3D8%0A%5Cend%7Baligned%7D)

Développons le polynome ![latex](https://render.githubusercontent.com/render/math?math=%28x%2By%29%5E3&mode=inline):

![latexml](https://render.githubusercontent.com/render/math?math=%28x%2By%29%5E3%3Dx%5E3%2B3x%5E2y%2B3xy%5E2%2By%5E3%3D40%2B3%5Ctimes8%3D64)

On peut calculer ![latex](https://render.githubusercontent.com/render/math?math=xy&mode=inline):

![latexml](https://render.githubusercontent.com/render/math?math=x%5E2y%2Bxy%5E2%3Dxy%28x%2By%29%3Dxy%5Ctimes%5Csqrt%5B3%5D%7B64%7D%3D4xy%3D8)

D'où: ![latex](https://render.githubusercontent.com/render/math?math=xy%3D2&mode=inline)

> réponse: 2

## Jeudi 5 Novembre

Comme la droite DF est tangente au petite cercle, ∠DFB est droit.

L'angle ∠DEC est également droit puisque DC est un diamètre du cercle sur lequel est E.

Ainsi, les droite BF et CE sont parallèles.

Par le théorème de Thalès: DB / DC = DF / DE

Calculons les trois valeurs pour trouver DE:

- DB = 12 - 12 / 4 = 9
- DC = 12
- DF = √(9² - 3²) = √72 = 6 √2

D'où: DE = 6 √2 / 9 × 12 = 8 √2

> réponse: 8 √2 cm

## Vendredi 6 Novembre

1 2 3 4 5 6 7 8 9

8 doit être le chiffre des dizaines pour que le nombre qu'il compose soit premier. On a le choix entre  83 et 89. De même pour 6 et 4 avec respectivement comme choix 61 67 et 41 43 47.

Il y a donc au maximum 2 × 2 × 3 = 12 solutions. Il y en a en fait maoins car des chiffres sont en commun entre les nombres.

| choix pour 8 6 4 | chiffres restants | somme |
| -----------------|-------------------|-------|
| 83 61 47 |  9 5 2 ❌ | 207 |
| 83 67 41 |  9 5 2 ❌ | 207 |
| 89 61 43 |  5 7 2 ✅ | 207 |
| 89 61 47 |  3 5 2 ✅ | 207 |
| 89 67 41 |  3 5 2 ✅ | 207 |
| 89 67 43 |  5 1 2 ❌ | 207 |

Toutes ces solutions ne sont pas valides (9 et 1 non premiers). Mais on ne pourra pas les combiner pour faire une somme inférieure à 207.

207 est donc la somme minimale à trouver.

> réponse: 207

## Lundi 9 Novembre

On prend les nombres dans l'ordre et on élimine. 1 élimine les nombres que se terminent par 4 et 9, 2 élimine 3 et 8, etc. 5 élimine 0 et les autres nombres qui se terminent par 5.

Il reste: 1 2 5 6 7 11 12 16 17 21 22 26 27

On pourrait remplacer 1, 11, 21 par 4, 14, 24. Etc.

> réponse: 13

## Mardi 10 Novembre

Si on place E à l'opposé de A, le triangle AEC est rectangle en C et on a ∠AEC = 90 - ∠BAC = 30°.

D'une manière générale, le [théorème de l'angle au centre](https://fr.wikipedia.org/wiki/Théorème_de_l%27angle_inscrit_et_de_l%27angle_au_centre) dit que l'angle ∠ABC est le double de l'angle ∠AEC.

![schéma](10.png)

> réponse: 30°

## Mercredi 11 Novembre

Pierre a quatre visites à faire. Si on fixe la position des visites à André et Bruno, celle des visites de Charles et Denis est déterminée (les deux places libres, puisque l'ordre est imposé). La réponse est donc ![latex](https://render.githubusercontent.com/render/math?math=%7B4%5Cchoose%202%7D%3D6&mode=inline).

Illustration de la solution en Python:

```python
from itertools import permutations
for z in permutations("ABCD"):
    if z.index("A") < z.index("B") and z.index("C") < z.index("D"):
        print("".join(z))
```

> réponse: 6

## Jeudi 12 Novembre

Comme 1 n'est pas solution de l'équation, on peut factoriser le terme de gauche:

1 + x + x² + x³ = (x⁴ - 1) / (x - 1)

L'équation devient alors:

(x⁴ - 1) / (x - 1) = x⁴ + x⁵

Or:

(x⁴ + x⁵) (x - 1) = x⁶ - x⁴

L'équation s'écrit alors:

x⁶ - x⁴ = x⁴ - 1

x⁴ (x² - 1) = (x² - 1) (x² + 1)

Pour x ≠ 1, x² = 1 est solution, d'où la première racine: x = -1.

Il faut trouver les autres. En simplifiant par x² - 1 devenu non nul à partir d'ici:

x⁴ = x² + 1

x² = (1 ± √5) / 2

On cherche les valeurs réelles (et non complexes). Donc les autres racines sont:

x = ± √((1 + √5) / 2)

> réponse: -1, -√((1 + √5) / 2), √((1 + √5) / 2)

## Vendredi 13 Novembre

Il y a 2⁴ nombres écrits avec des 3 et des 5 (deux possibilités par chiffre). Chaque chiffre de la moitié de ces nombres est un 3, l'autre moitié un 5. Donc la somme de chaque chiffre est (3 + 5) × 8 = 64.

La réponse est 64 + 640 + 6400 + 64000 = 64 × 1111 = 71104

> réponse: 71104

## Lundi 16 Novembre

| tour  | perdant | Adèle | Louis | Camille |
|-------|---------|-------|-------|---------|
| final |         |    27 |    27 |      27 |
|     3 | Camille |     9 |     9 |      63 |
|     2 |  Louis  |     3 |    57 |      21 |
|     1 |  Adèle  |    55 |    19 |       7 |

> réponse: 55 €

## Mardi 17 Novembre

12 = 1 × 2 × 2 × 3

Donc les produits de chiffres qui font 12 sont:

- 1 × 2 × 6 → 6 possibilités
- 2 × 2 × 3 → 3 possibilités
- 1 × 4 × 3 → 6 possibilités

> réponse: 15 nombres

## Mercredi 18 Novembre

Soir ![latex](https://render.githubusercontent.com/render/math?math=r%3DCB%3DBC&mode=inline) le rayon du cercle. Comme la droite AD est tangente en D au cercle, CD et AD sont perpendiculaires et Pythagore permet d'écrire:

![latex](https://render.githubusercontent.com/render/math?math=AD%5E2%20%2B%20DC%5E2%20%3D%20AC%5E2%20%3D%20%28AB%20%2B%20BC%29%5E2&mode=inline)

![latex](https://render.githubusercontent.com/render/math?math=10%5E2%20%2B%20r%5E2%20%3D%20%287%20%2B%20r%29%5E2&mode=inline)

![latex](https://render.githubusercontent.com/render/math?math=100%20%3D%2049%2B14r&mode=inline)

![latexml](https://render.githubusercontent.com/render/math?math=r%20%3D%20%5Cfrac%20%7B51%7D%20%7B14%7D%20cm)

> réponse: 51 / 14 cm

## Jeudi 19 Novembre

Tous les nombres pairs ont 2 en diviseur commun, et il y en a 10 entre 1 et 20.

> réponse: 10

## Vendredi 20 Novembre

> a ⭑ b = ab + 3

La première opération est: 1 ⭑ 1 = 4

Si b = 1: a ⭑ 1 = a + 3

Ainsi l'imbrication de l'opération ⭑ est la suite arithmétique uₙ₊₁ = uₙ + 3 avec u₁ = 1.

uₙ = 1 + 3n

2020 = 1 + 3n ⇔ n = 673

Il faut donc 673 opérations ⭑ pour arriver à 2020, et donc 673 + 1 = 674 nombres 1 (deux pour la première opération, et un de plus par opération suivante).

> réponse: 674

## Lundi 23 Novembre

![schéma](23.png)

Aire BEC = 90 - 8 × 8 = 26

Donc GE × GC = 26, soit GE = 13 / 2

Aire ACE = aire AFE + aire CFE

aire CFE = FE × CG / 2 = (4 + 13 / 2) × 4 / 2 = 21

aire AFE = FE × AH / 2 = FE × CG / 2 = aire CFE = 21

Donc l'aire recherchée est 21 + 21 = 42

> réponse: 42 cm²

## Mardi 24 Novembre

![latex](https://render.githubusercontent.com/render/math?math=%28a%5E2%2Bb%5E2%29%5E2-%28a%5E2-b%5E2%29%5E2%3D144&mode=inline)

On peut factoriser en utilisant la formule ![latex](https://render.githubusercontent.com/render/math?math=A%5E2-B%5E2%3D%28A-B%29%28A%2BB%29&mode=inline).

![latex](https://render.githubusercontent.com/render/math?math=%5Cleft%28%28a%5E2%2Bb%5E2%29-%28a%5E2-b%5E2%29%5Cright%29%5Cleft%28%28a%5E2%2Bb%5E2%29%2B%28a%5E2-b%5E2%29%5Cright%29%3D144&mode=inline)

![latex](https://render.githubusercontent.com/render/math?math=%5Cleft%282b%5E2%5Cright%29%5Cleft%282a%5E2%5Cright%29%3D144&mode=inline)

![latex](https://render.githubusercontent.com/render/math?math=%28ab%29%5E2%3D36&mode=inline)

![latex](https://render.githubusercontent.com/render/math?math=a%5Ctimes%20b%3D6&mode=inline) car a et b sont positifs.

Les possibilités sont (1,6) (2,3).

![latex](https://render.githubusercontent.com/render/math?math=a%5E2%2Bb%5E2&mode=inline) peut donc valoir ![latex](https://render.githubusercontent.com/render/math?math=1%2B6%5E2%3D37&mode=inline) et ![latex](https://render.githubusercontent.com/render/math?math=2%5E2%2B3%5E3%3D13&mode=inline).

> réponse: 13

## Mercredi 25 Novembre

Reste division par 5 égal à 4 => ce sont les nombres x4 et y9.

Il faut que le reste de la division par 3 soit 1, donc x3 et y8 doivent être divisibles par 3.

Pour x, les possibilités sont 3 6 9 (somme des chiffres multiple de 3). Pour y, les possibilités sont: 1 4 7.

x4 ne peut pas être premier. Il reste 19 49 79. Il n'y a que 19 et 79 qui soient premiers.

> réponse: 19 et 79

## Jeudi 26 Novembre

Soit l'équation :

![latexml](https://render.githubusercontent.com/render/math?math=x%5E3y%2Bx%2By%3Dxy%2B2xy%5E2)

Elle peut s'écrire ainsi:

![latexml](https://render.githubusercontent.com/render/math?math=x%5E3y%2Bx%2By-xy-2xy%5E2%3D0)

Ou encore de ces deux manières différentes:

![latexml](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Bcases%7D%0A%26x%20%2By%20%28x%5E3%2B1-x-2xy%29%3D0%20%5C%5C%0A%26y%20%2B%20x%20%28x%5E2y%2B1-y-2y%5E2%29%3D0%0A%5Cend%7Bcases%7D)

On en déduit que ![latex](https://render.githubusercontent.com/render/math?math=x&mode=inline) divise ![latex](https://render.githubusercontent.com/render/math?math=y&mode=inline) et ![latex](https://render.githubusercontent.com/render/math?math=y&mode=inline) divise ![latex](https://render.githubusercontent.com/render/math?math=x&mode=inline) si ![latex](https://render.githubusercontent.com/render/math?math=x&mode=inline) et ![latex](https://render.githubusercontent.com/render/math?math=y&mode=inline) sont non nuls. Or, ![latex](https://render.githubusercontent.com/render/math?math=x&mode=inline) et ![latex](https://render.githubusercontent.com/render/math?math=y&mode=inline) sont entiers, donc ![latex](https://render.githubusercontent.com/render/math?math=x%20%3D%20y&mode=inline). Par ailleurs la solution ![latex](https://render.githubusercontent.com/render/math?math=x%20%3D%20y%20%3D%200&mode=inline) est valide.

L'équation devient, pour ![latex](https://render.githubusercontent.com/render/math?math=x&mode=inline) non nul:

![latex](https://render.githubusercontent.com/render/math?math=x%5E4%2B2x-x%5E2-2x%5E3%3D0&mode=inline)

![latex](https://render.githubusercontent.com/render/math?math=x%5E3-2x%5E2-x%2B2%3D0&mode=inline)

![latex](https://render.githubusercontent.com/render/math?math=%28x%5E3-2x%5E2%2Bx%29-2x%2B2%3D0&mode=inline)

![latex](https://render.githubusercontent.com/render/math?math=x%28x-1%29%5E2%3D2%28x-1%29&mode=inline)

![latex](https://render.githubusercontent.com/render/math?math=x%3D1&mode=inline) est une solution. Les autres doivent vérifier:

![latex](https://render.githubusercontent.com/render/math?math=x%28x-1%29%3D2&mode=inline)

Ce polynome a deux solutions, -1 et 2. Donc ![latex](https://render.githubusercontent.com/render/math?math=x%3D2&mode=inline) puisque ![latex](https://render.githubusercontent.com/render/math?math=x&mode=inline) doit être positif.

En conclusion, les seules solutions entières et positives à l'équation sont:

> réponse: x=0 y=0, x=1 y=1, x=2 y=2

## Vendredi 27 Novembre

La distance AC est égale à 2 √2 × √2 = 4 cm. Donc le rayon du cercle de centre vaut 4 - 2 √ 2. Ainsi la zone coloriée a pour aire:

(2 √2)² - π (4 - 2 √2)² / 4 - π (2 √2)² / 4 = 8 + 4 (√2 - 2) π

> réponse: 8 + 4 (√2 - 2) π cm²

## Lundi 30 Novembre

Affichage de la tresse en Python avec [programme](30.py). On remarque le cycle tous les six rangs.

```python
#!/usr/bin/env python3

rang = ("\033[91ma", "\033[92mb", "\033[93mc", "\033[94md")
for i in range(1, 21):
    a, b, c, d = rang
    if i % 2 == 1:
        rang = (b, c, a, d)
    else:
        rang = (a, d, b, c)
    print(f"\033[2m{i:2}\033[0m {' '.join(rang)} \033[0m")
```

> réponse: b d c a
