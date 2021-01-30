# Calendrier Mathématique Mai 2020

## Vendredi 1 Mai

La mise en équation donne: 4 / 5 n + 4 / 5 = n

Soit n - 4 / 5 n = 4 / 5

D'où n = 4

> réponse: quatre chats

## Lundi 4 Mai

Soit a,b,c les dimensions de la cage. On a:

- x = ab ①
- y / 5 = ac  ⇔  y = 5ac ②
- 5xy = bc ③

En remplaçant dans ③ x et y tels que donnés par ① et ②:

5 ab × 5 ac = bc

D'où a = 1 / 5

Le volume de la cage est abc.

abc = bc / 5 = xy

> réponse: xy

## Mardi 5 Mai

Recherche avec [programme](05.py) Python.

```python
#!/usr/bin/env python3

import math


def divisors(n):
    divs = [1, n]
    for i in range(2, int(math.sqrt(n)) + 1):
        q, r = divmod(n, i)
        if r == 0:
            divs.extend([i, q])
    return list(sorted(divs))


n = 2
while True:
    u = [0] * 10
    nu = 0
    for d in divisors(n):

        if u[d % 10] == 0:
            u[d % 10] = 1
            nu += 1

        if nu == 10:
            print(n, divisors(n))
            exit()

    n += 1
```

> réponse: 270

## Mercredi 6 Mai

En triant selon l'énoncé, on obtient:

marie < sylvie < sophie < ana < elsa < pauline

Marie a 15€, Sylvie 30€, Sophie 45€, etc.

> réponse: Sophie 45€

## Jeudi 7 Mai

![schéma](07.png)

ADA' et ACA' sont deux triangles rectangles dont deux côtés ont pour longueur 1 et 4 (hypoténuse), d'où le troisième côté AA' = √(4² - 1) = √15

La distance DC recherchée est le double de la hauteur 𝒉 des triangles. On peut écrire (calcul de l'aire de deux façons différentes):

AD × DA' = 𝒉 × AA'

Soit DC = 2 𝒉    = AD × DA' / AA' × 2 = 1 × V15 / 4 × 2 = V15 / 2

> réponse: V15 / 2 cm

## Vendredi 8 Mai

Mise en équation (V volume de la piscine, Tᵢ le débit par jour du tuyau 𝑖):

- V = (T₁ + T₂) × 3
- V = (T₂ + T₃) × 4
- V = (T₁ + T₃) × 6

4V + 3V + 2V = 9V = 12 (T₁ + T₂) + 12 (T₂ + T₃) + 12 (T₁ + T₃) = 24 (T₁ + T₂ + T₃)

D'où V = 8 / 3 (T₁ + T₂ + T₃)

> réponse: 64h ou 2 jours et 16h

## Lundi 11 Mai

## Mardi 12 Mai

## Mercredi 13 Mai

## Jeudi 14 Mai

## Vendredi 15 Mai

## Lundi 18 Mai

## Mardi 19 Mai

## Mercredi 20 Mai

## Jeudi 21 Mai

## Vendredi 22 Mai

## Lundi 25 Mai

## Mardi 26 Mai

## Mercredi 27 Mai

## Jeudi 28 Mai

## Vendredi 29 Mai
