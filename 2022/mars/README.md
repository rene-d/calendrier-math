# Calendrier Mathématique Mars 2022

[Solutions 2022](../README.md) - [Homepage](../../README.md)

## Mardi 1 Mars

Sur une quantité totale de 1, la quantité de garçons est 4/5 et celle des filles 1/5.

Après expulsion de 2/3 des garçons, il en reste 1/3, soit 4/5 × 1/3 =  4/15.

Il reste une quantité totale de = 4/15 + 1/5 = 7/15

La proportion de filles est: ![latex](https://render.githubusercontent.com/render/math?math=%5Cfrac%7B%5Cfrac%201%205%7D%7B%5Cfrac%207%20%7B15%7D%7D%20%3D%20%5Cfrac%7B3%7D%7B7%7D&mode=inline)

> réponse: 3/7

## Mercredi 2 Mars

![02](02.png)

réponse: en prenant la symétrique par rapport à l'axe des abscisses jusqu'à 4

## Jeudi 3 Mars

A faire de tête ou avec un papier, sinon pas beaucoup d'intérêt... ([factordb](http://factordb.com/index.php?query=112266) [wa](https://www.wolframalpha.com/input/?i=112266) etc.)

- 112266 ÷ 2 = 56133
- 56133 ÷ 9 = 6237
- 6237 ÷ 9 = 693
- 693 ÷ 9 = 77

On en déduit la décomposition en facteurs premiers: 2 × 3⁶ × 7 × 11

> réponse: n = 6

## Vendredi 4 Mars

En commençant par le sommet A, on peut choisir un sommet parmi B C D E puis un troisième parmi I H F G, ce qui permet de dessiner 16 triangles.

En partant de G E I, on obtient en tout 64 triangles différents.

> réponse: 64

## Lundi 7 Mars

105 = 3 × 5 × 7

- on ne peut pas enlever 0 sinon plus multiple de 5
- on ne peut pas enlever ni 4 ni 2 sinon plus multiple de 3
- il reste 4320 et 4620 comme possibilités

Test [divisibilité par 7](https://fr.wikipedia.org/wiki/Liste_de_critères_de_divisibilité#Lemmes_de_divisibilité_par_7):

- 4320 → 432 + 5 × 0 = 432 → 43 + 5 × 2 = 53 → non divisible par 7
- 4620 → 462 + 5 × 0 = 462 → 46 + 5 × 2 = 56 = 7 × 8 → divisible par 7

Il faut enlever le 3 de 43620 car 4620 est un multiple de 105.

> réponse: 3

## Mardi 8 Mars

## Mercredi 9 Mars

## Jeudi 10 Mars

## Vendredi 11 Mars

## Lundi 14 Mars

Soient ![latex](https://render.githubusercontent.com/render/math?math=x&mode=inline) ![latex](https://render.githubusercontent.com/render/math?math=y&mode=inline) entiers tels que ![latex](https://render.githubusercontent.com/render/math?math=x%5E2%2By%5E2%3D50&mode=inline)

Les solutions entières sont (±1, ±7) et (±5, ±5).

### x, y entiers naturels

Deux valeurs possibles: 8 et 10

### x, y entiers relatifs

Sept valeurs possibles: 8, 6, -6, -8, 10, -10, 0

> réponse: 2 (entiers naturels) ou 7 (entiers relatifs)

## Mardi 15 Mars

## Mercredi 16 Mars

## Jeudi 17 Mars

## Vendredi 18 Mars

Soit 𝑥 = EF

Aire triangle ABC: (𝑥 + 2) × (5 + 10) ÷ 2

Aire partie colorée: (10 + 5) × 2 + 5 × 𝑥

Equation:

- 15 / 2 (𝑥 + 2) = 30 + 5 𝑥
- 5 / 2 𝑥 = 30 - 15
- 𝑥 = 6

> réponse: 6 cm

## Lundi 21 Mars

En noir le chemin qui passe par tous les sommets, une seule fois (donc impossible de faire plus court).

![21](21.png)

> réponse: 7

## Mardi 22 Mars

> réponse: 18 ans

## Mercredi 23 Mars

La somme des nombres de 1 à 9 est 45.

La somme des trois côtés du triangle fait donc 45 + 7 + a où a est le nombre placédans le troisème sommet. Cette somme doit être divisible par 3.

Les valeurs 1, 3, 4, 6, 7, 9 ne conviennent pas. 2 et 5 sont déjà prises. Il reste donc 8.

La somme des côtés est donc 20.

Programme [Python](23.py) pour énumérer toutes les solutions.

```python
#!/usr/bin/env python3

from itertools import permutations

for a, b, c, d, e, f, g in permutations([1, 3, 4, 6, 7, 8, 9]):
    if 5 + a + b + 2 == 5 + c + d + e == e + f + g + 2:
        print(5, a, b, 2, "-", 5, c, d, e, "-", e, f, g, 2, "=", 5 + a + b + 2)
```

> réponse: 20

## Jeudi 24 Mars

## Vendredi 25 Mars

![latex](https://render.githubusercontent.com/render/math?math=5%5E%7B2n%2B1%7D%20-%201&mode=inline) est disible par 4 mais par 8.

En effet :

![latexml](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Baligned%7D%0A5%5E%7B2n%2B1%7D%20-%201%0A%26%3D%205%20%5Ctimes%205%5E%7B2n%7D%20-%201%20-%204%20%2B%204%0A%5C%5C%0A%26%3D%205%20%5Ctimes%20%5Cleft%28%205%5E%7B2n%7D%20-%201%20%5Cright%29%20%2B%204%0A%5C%5C%0A%26%3D%205%20%5Ctimes%20%5Cleft%28%205%5En%20%2B%201%20%5Cright%29%20%5Cleft%28%205%5En%20-%201%20%5Cright%29%20%2B%204%0A%5Cend%7Baligned%7D)

Le premier terme est multiple de 4 (au moins) puisque ![latex](https://render.githubusercontent.com/render/math?math=5%5En-1&mode=inline) et ![latex](https://render.githubusercontent.com/render/math?math=5%5En%2B1&mode=inline) sont pairs. Mais le deuxième terme n'est multiplque que de 4, et pas de 8.

Il y a donc deux puissances de 2 par facteur. Il y a 100 facteurs.

> réponse: 200

## Lundi 28 Mars

Les possibilités de triplets de chiffres sont:

- 1 3 9
- 1 2 4 car √(1 × 4) = √4 = 2
- 2 4 8 car √(2 × 8) = √16 = 4
- 4 6 9 car √(4 × 9) = √36 = 6
- tous les triplets avec le même chiffre (sauf 0) : ccc car c = √c × √c
- toutes les centaines : c00 car 0 = √c × 0

Soit au total, 6 + 6 + 6 + 6 + 9 + 9 = 42 possibilités.

> réponse: 42

## Mardi 29 Mars

a, b distincts, a=x et b=x sont impossibles.

![latex](https://render.githubusercontent.com/render/math?math=%28x-a%29%5E2%3D%28x-b%29%5E2&mode=inline)

![latex](https://render.githubusercontent.com/render/math?math=-2xa%2Ba%5E2%3D-2bx%2Bb%5E2&mode=inline)

![latexml](https://render.githubusercontent.com/render/math?math=x%20%3D%20%5Cfrac%20%7Bb%5E2-a%5E2%7D%20%7B2b%20-%202a%7D%0A%3D%20%5Cfrac%20%7B%28b-a%29%28b%2Ba%29%7D%20%7B2%28b-a%29%7D%0A%3D%20%5Cfrac%20%7Ba%2Bb%7D%202)

> réponse: (a+b)/2

## Mercredi 30 Mars

Les nombres suivants sont:

- a = 2020
- b = 2021
- c = 2022
- d = 2100

La différence est donc 80.

Une manière de faire le calcul en Python est la suivante, en utilisant la base 3:

```python
import numpy
int(numpy.base_repr(int("2012", 3) + 4, base=3)) - int(numpy.base_repr(int("2012", 3) + 1, base=3))
```

> réponse: 80

## Jeudi 31 Mars

Aire PQR : 3𝑥4÷2

Aire XYZ : 4𝑥7÷2

> réponse: 3/7
