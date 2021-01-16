# Calendrier Mathématique Octobre 2021

## Vendredi 1 Octobre

![schéma](01.png)

Les centres O₁ et O₂ des petits cercles sont nécessairement sur le cercle de centre O et de rayon 8 - 2 = 6 cm pour que les cercles soient tangents.

De plus, par construction, ils sont opposés, sur le même diamètre.

Ils sont donc distants de 2 × 6 = 12 cm

> réponse: 12 cm

## Lundi 4 Octobre

Le plus petit nombre à deux chiffres est 10 et le plus grand à trois chiffres 999. Cela tombe bien puisque 999 - 10 = 989. On ne peut obtenir de différence plus grande, tout autre nombre donnerait une différence inférieure.

La somme est 999 + 10 = 1009.

> réponse: 1009

## Mardi 5 Octobre

La somme des dix nombres peut s'écrire ainsi:

𝑥 × (1 + 2 + 4 + 8 + 3 + 6 + 12 + 9 + 18 + 27) = 90 𝑥

Pour que 90 𝑥 soit un carré d'un nombre entier, on va décomposer en facteurs premiers et faire en sorte que chaque facteur soit un carré.

90 = 2 × 3 × 3 × 5

Il manque donc 2 × 5 pour que chaque facteur soit à une puissance paire. D'où 𝑥 = 2 × 5 = 10.

> réponse: 𝑥 = 10

## Mercredi 6 Octobre

![schéma](06.png)

Surface hachurée: 6 × 6 × 2/3 = 36 × 2 / 3 = 24 cm²

Surface triangle: 𝑥 × 0.6 = 24

𝑥 = 24 / 0.6 = 40 cm²

> réponse: 40 cm²

## Jeudi 7 Octobre

![schéma](07.png)

[Théorème de Thalès](https://fr.wikipedia.org/wiki/Théorème_de_Thalès):

DF / AE = GD / GE = GF / GA = 1 / 2

De la même façon, on a:

DG / DE = HG / AE = DH / DA = 1 / 3

Donc, l'aire du triangle DGF est:  DF × GK / 2 = 1 × 1 / 2 = 1 / 2 cm²

L'aire du triangle GAE est: (DA - GK) × AE / 2 = 2 × 2 / 2 = 2 cm²

L'aire du triangle DEC est: 3 × 3 / 2 = 9 / 2 cm²

L'aire du parallèlogramme hachuré est: DEC - DGF - GAE = 9 / 2 - 1 / 2 - 2 = 2 cm²

> réponse: 2 cm²

## Vendredi 8 Octobre

x < 2 donc | x - 2 | = 2 - x

2 - x = p

x - 2 = -p

x - p = -2 p + 2

> réponse: -2 p + 2

## Lundi 11 Octotbre

Il y a 3⁴ opérations possibles: on peut soustraire, additionner ou soustraire chaque nombre.

Il y a donc au maximum 81 nombres, la moitié étant négative et un nul. Donc au maximum 40 nombres.

Le programme [Python](11.py) vérifie qu'il y en a bien 40 différents, soit tous les nombres de 1 à 40.

```python
#!/usr/bin/env python3

import itertools

results = set()
for ops in itertools.product("0-+", repeat=4):
    result = 0
    for op, nb in zip(ops, [1, 3, 9, 27]):
        if op == "+":
            result += nb
        elif op == "-":
            result -= nb
    if result > 0:
        results.add(result)

print(len(results))
```

```python
#!/usr/bin/env python3

import itertools

results = set()
for ops in itertools.product("0-+", repeat=4):
    result = 0
    for op, nb in zip(ops, [1, 3, 9, 27]):
        if op == "+":
            result += nb
        elif op == "-":
            result -= nb
    if result > 0:
        results.add(result)

print(len(results))
```

```python
#!/usr/bin/env python3

import itertools

results = set()
for ops in itertools.product("0-+", repeat=4):
    result = 0
    for op, nb in zip(ops, [1, 3, 9, 27]):
        if op == "+":
            result += nb
        elif op == "-":
            result -= nb
    if result > 0:
        results.add(result)

print(len(results))
```

> résultat: 40

# Mardi 12 Octobre

Recherche triviale avec [programme](12.py) Python.

```python
#!/usr/bin/env python3

import itertools

for a00, a02, a10, a11, a21 in itertools.permutations([2, 5, 6, 8, 9]):
    if a00 + 1 + a02 == a10 + a11 + 7 == 4 + a21 + 3 == a00 + a10 + 4 == 1 + a11 + a21 == a02 + 7 + 3:
        break

print("réponse:")
print(f"{a00} 1 {a02}")
print(f"{a10} {a11} 7")
print(f"4 {a21} 3")
```

```python
#!/usr/bin/env python3

import itertools

for a00, a02, a10, a11, a21 in itertools.permutations([2, 5, 6, 8, 9]):
    if a00 + 1 + a02 == a10 + a11 + 7 == 4 + a21 + 3 == a00 + a10 + 4 == 1 + a11 + a21 == a02 + 7 + 3:
        break

print("réponse:")
print(f"{a00} 1 {a02}")
print(f"{a10} {a11} 7")
print(f"4 {a21} 3")
```

```python
#!/usr/bin/env python3

import itertools

for a00, a02, a10, a11, a21 in itertools.permutations([2, 5, 6, 8, 9]):
    if a00 + 1 + a02 == a10 + a11 + 7 == 4 + a21 + 3 == a00 + a10 + 4 == 1 + a11 + a21 == a02 + 7 + 3:
        break

print("réponse:")
print(f"{a00} 1 {a02}")
print(f"{a10} {a11} 7")
print(f"4 {a21} 3")
```

> réponse:

```text
9 1 5
2 6 7
4 8 3
```

## Mardi 19 Octobre

ADEF rectangle ⇒ FE = AD et FE // AC

Théorème de Thalès: FE / AC = BF / BA = BE + BC

Ici: 𝑥 / 14 = (4 - 2.5) / 4

> réponse: 𝑥 = 5.25
