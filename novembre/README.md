# Calendrier Mathématique Novembre 2021

## Lundi 1 Novembre

Comme 13 est premier, on doit avoir 3a - b = 1 et 3b - a = 13 ou vice-versa.

```text
3a - b = 1      9a - 3b = 3     3a - b = 1          6 - b = 1   b = 5
3b - a = 13     3b - a = 13     9a - a = 3 + 13     a = 2       a = 2
```

a - b = ±3

> réponse: ±3

## Mardi 2 Novembre

Sens anti-horaire: 4⇄2 3⇄4 5⇄6 : 3 mouvements

Sens anti-horaire: 4⇄1 4⇄6 : 2 mouvements

Le sens horaire sera plus long, puisque 2 va nécessiter 3 interversions.

> réponse: 2

## Mercredi 3 Novembre

aire triangle = aire// + aireXX + 1 - aire bleu

- aire// = 2 × 3 / 2 = 3
- aireXX = 2 × 1 / 2  = 1
- aire bleu = 3 × 1 / 2 = 3 / 2

3 + 1 + 1 - 3 / 2 = 7 / 2

> réponse: 7 / 2 cm²

## Jeudi 4 Novembre

Pour que la moyenne soit un nombre entier, il faut que la somme soit multiple de 5, donc qu'elle se termine par 0 ou 5. Comme elle peut se terminer par les 10 chiffres, il y a 2 / 10 de chance que la somme se termine par 0 et 5.

> réponse: 1 / 5

## Vendredi 5 Novembre

```text
    5 ★ ★
 ×  ★ ★ ★
 --------
    ★ ★ ★
  ★ 3 ★
★ ★ ★
---------
★ ★ 0 ★ ★
```

Il faut que e = 1 sinon la première ligne intemédiaire manque d'une étoile. De la même façon c = d = 1. Donc a = 3.

```text
    5 3 ★
 ×  1 1 1
 --------
    5 3 ★
  5 3 ★
5 3 ★
---------
★ ★ 0 ★ ★
```

5 + 3 + ★ = 0 ⇒ ★ = 1 ou 2

Ca ne peut pas être 1 car pas de retenue pour faire 0. Donc c'est 2.

> réponse: 532 × 111 = 59052

## Lundi 8 Novembre

Supposons le quadrilatère non croisé. La somme de ses angles fait 360°. On a alors:

a + (a + d) + (a + 2d) + (a + 3d) = 4a + 6d = 360°

La somme du plus petit et du plus grand angle vaut donc:

a + (a + 3d) = 2a + 3d = 180°

> réponse: 180°

## Mardi 9 Novembre

Rappel: angle aigu = angle entre 0° et 90°

- 3 isocèles, 2 rectangles par coin → 20
- 2 isocèles, 4 rectangles par milieu côté → 24
- 4 isocèles, 4 rectangles pour le centre → 8

> réponse: 52

Vérification avec [programme](09.py) en Python.

```python
#!/usr/bin/env python3

from math import degrees, atan2


def angle(a, b, c):
    """ Calcule l'angle ABC non signé non orienté. """

    ang = degrees(atan2(c[1] - b[1], c[0] - b[0]) - atan2(a[1] - b[1], a[0] - b[0]))

    ang = round(abs(ang))
    if ang > 180:
        ang = 360 - ang

    return ang


# calcule les coordonnées des 9 points
points = []
for x in range(-1, 2):
    for y in range(-1, 2):
        points.append((x, y))

triangles = set()

for a in points:

    for b in points:
        if a == b:
            # deux points confondus: à ignorer
            continue

        for c in points:
            if a == c or b == c:
                # deux points confondus: à ignorer
                continue

            # calcule les 3 angles du triangles
            angles = angle(b, a, c), angle(c, b, a), angle(a, c, b)
            if min(angles) == 0 or max(angles) > 90:
                continue

            # on a un triangle, dont tous les angles sont aigus
            # on mémorise l'identification unique du triangle
            triangles.add(str(sorted((a, b, c))))

print("réponse:", len(triangles))
```

## Mercredi 10 Novembre

- D: 2021 × 2 = 4042
- T: 4042 / 10 = 404
- D: 404 × 2 = 808
- T: 808 / 10 = 80

> réponse: 80

Vérification avec [programme](10.py) en Python.

```python
#!/usr/bin/env python3

def D(x):
    return x*2

def T(x):
    return x//10

x = 2021

x=D(x)
x=T(x)
x=D(x)
x=T(x)

print(x)
```

## Jeudi 11 Novembre

La moyenne des nombres est 80. On va d'abord chercher avec 80 comme dernier nombre entré, la moyenne ne bougera pas.

On est obligé de commencer par deux nombres de même parité, sinon la première moyenne ne sera pas entière (impair+pair=impair, impair/2 pas entier).

Si on commence par les deux impairs, la première moyenne est 81 et la moyenne suivante ne pourra pas être entière: il n'y a aucun multiple de 3 pair et donc 81×2+pair ne pourra pas être divisible par 3.

Donc on va essayer de commencer par 76 et 82: (76 + 82) / 2 = 79

Puis un nombre imapir: (79×2 + 71) = 229, (79×2 + 91) = 249. 71 ne convient pas, 229 n'est pas divisible par 3. C'est donc 91 et la moyenne est 83.

Puis 71: 83×3 + 71 = 320, moyenne 80. C'est donc le bon ordre.

Il y a deux solutions (normal, l'ordre des deux premiers ne compte pas):

1. (76, 82, 91, 71, 80)
2. (82, 76, 91, 71, 80)

> réponse: 80

Vérification avec [programme](11.py) en Python.

```python
#!/usr/bin/env python3

import itertools

saisie = [71, 76, 80, 82, 91]

for nb in itertools.permutations(saisie):
    for i in range(2, len(nb) + 1):

        s = sum(nb[:i])
        if s % i != 0:
            break

        if i == len(nb):
            print(nb[:i], [sum(nb[:j]) / j for j in range(2, len(nb) + 1)])
```

## Mardi 16 Novembre

Procédons par élimination.

Ca ne peut pas être 57603, il est disible par 3 mais pas par 9.

Ca ne peut pas être 57122, il est divisible par 2 mais pas par 4.

Ca ne peut pas être 58088, il est divisble par 8 mais par 16.

Reste deux nombres, 56167 et 56644. Commençons par 56644, c'est plus simple.

- 56644 / 4 = 14161  divisible par 7 ? 1416+5×1 = 1421   142+5×1 = 147 = 21×7 oui
- 14161 / 7 = 2023  divisible par 7 ? 202+3×5 = 217 = 31×7 oui
- 2023 / 7 = 289  or 289 = 17²

C'est donc 56644 = (2 × 7 × 17)² = 238²

> réponse: 56644

Nota: 56167 est premier

## Mercredi 17 Novembre

Calcul avec [programme](17.py) en Python.

```python
#!/usr/bin/env python3

a, b = 1, 1

unites = set()
while len(unites) < 10:
    # print(f"{a:5}+{b:5}={a+b:6}")
    b, a = a + b, b
    unites.add(b % 10)

print("réponse:", b % 10)
```

> réponse: 6

## Jeudi 18 Novembre

Il y a 100 tirages possibles.

Si on tire 1 en premier, il faut tirer 10.
Si on tire 2 en premier, il faut tirer 9 ou 10.
…
Si on tire 10 en dernier, il faut tirer 1 à 10.

1+2+3+…+10 = 10 × 11 / 2 = 55

Vérification en Python:

```python
sum(1 for i in range(1,11) for j in range(1,11) if i+j>10)
```

> réponse: 55 / 100

## Lundi 22 Novembre

Pierre a dépensé 25€ dans la dernière boutique, il avait donc 50€ en y rentrant. Etc.

25 * 2⁴ = 400€

> réponse: 400€
