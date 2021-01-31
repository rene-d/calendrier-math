# Calendrier Mathématique Novembre 2021

[Solutions 2021](../../README.md)

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

Rappel: angle aigu = angle entre 0° et 90° strictement

- 1 isocèle par coin → 4
- 1 isocèle par milieu côté → 4

> réponse: 8

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
            if min(angles) == 0 or max(angles) >= 90:
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
    return x * 2


def T(x):
    return x // 10


x = 2021

x = D(x)
x = T(x)
x = D(x)
x = T(x)

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

## Vendredi 12 Novembre

- Il y a les trois barres horizontales et verticales: 6 possibilités.
- quatre formes en ⎣
- quatre formes en ⎡
- quatre formes en ⎦
- quatre formes en ⎤

Soit 6 + 4 + 4 + 4 + 4 = 22 positions en tout.

> réponse: 22

## Lundi 15 Novembre

On a GH / AB = FH / FB = FG / FA par le théorème de Thalès.

Or, comme DF = AE, DFEA est un rectangle et G est sur la médiatrice de DA. Donc FG / FA = 1 / 2.

Donc AB = 2 GH = 2 × 3 = 6 cm et la surface du rectangle: 6 × 3 = 18 cm²

> réponse: 18 cm²

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

> réponse: 55 / 100 = 11 / 20

## Vendredi 19 Novembre

O étant le centre du cercle, il est sur la bissectrice des quatre angles. Donc chaque angle marqué est la moitié de l'angle entre les deux côtés.

La somme des angles d'un quadrilatère étant 360°, la moitié vaut 180°.

> réponse: 180°

## Lundi 22 Novembre

Pierre a dépensé 25€ dans la dernière boutique, il avait donc 50€ en y rentrant. Etc.

25 * 2⁴ = 400€

> réponse: 400€

## Mardi 23 Novembre

Le chiffre des unités de a² + b² est le même que celui de la somme des carrés des unités de a² et b².

a² peut se terminer par 0, 1, 4, 5, 6, 9. Comme b².

Pour faire 3, il n'y a que 4 + 9. Les antécédents de 4 (resp. 9) sont 2 et 8 (resp. 3 et 7).

Les différentes possibilités pour a + b sont:

- 2+3 ⇒ 5
- 2+7 ⇒ 9
- 8+3 ⇒ 1
- 8+7 ⇒ 5

> réponse: 1, 5 ou 9

## Mercredi 24 Novembre

Chaque sommet peut être relié à 8 sommets, ce qui fait 9 * 8 = 72 segments sur lesquels on peut construire deux triangles équilatéraux, un de chaque côté.

Cependant, le segment A₁A₂ va générer 2 triangles, comme le segment A₂A₁. Il y a donc 72 triangles non trivialement superposés.

En effet, les segments A₁A₄ A₂A₅ A₃A₆ vont générer des triangles dont le troisième sommet sera A₇, A₈, A₉. Il faut retirer ces trois triangles pour deux sommets. Le troisième comptabilisera le triangle. Soit 72 - 3 - 3 = 66.

> réponse: 66

## Jeudi 25 Novembre

Par le théorème de Thalès, on a (en faisant le tour des parallèles dans le sens horaires):

AX / XB = DY / YC = EZ / ZF = BX / XA

AX / XB = BX / XA implique AX = XB

> réponse: 1

## Vendredi 26 Novembre

Notons que (a + 1)(b + 1) = ab + a + b + 1

Donc les trois équations peuvent s'écrire:

- ab + a + b = (a + 1)(b + 1) - 1 = 524
- bc + b + c = (b + 1)(c + 1) - 1 = 146
- cd + c + d = (c + 1)(d + 1) - 1 = 104

Ce qui donne:

- (a + 1)(b + 1) = 525 = 3 × 5 × 5 × 7
- (b + 1)(c + 1) = 147 = 3 × 7 × 7
- (c + 1)(d + 1) = 105 = 3 × 5 × 7

Ni b + 1 ni c + 1 ne peuvent avoir 7² en facteur puisque les équations 1 et 3 n'ont pas pas 7². Donc on a b + 1 = 21 ou 7 et c + 1 = 7 ou 21.

Ainsi d + 1 = 5 ou 3 × 5 : il ne peut pas y avoir de facteur premier 5 dans c + 1, ni de 7 dans d + 1 puisqu'il est dans c + 1.

De la même façon 5 × 5 est "dans" a, qui vaut 25 ou 75.

| a + 1 | b + 1 | c + 1 | d + 1 | abcd = 8! ? |
| ----- | ----- | ----- | ----- | ----------- |
|   25  |   21  |    7  |   15  | 24×20×6×14 = 40320 ✅ |
|   75  |   7   |   21  |    5  | 74×6×20×4 = 35520 ❌ |

Donc a = 24 et d = 14, d'où: a - d = 10.

> réponse: 10

## Lundi 29 Novembre

Le nombre de diviseurs d'un entier se calcule à partir de la décomposition en facteurs premiers et est égal à: ∏ (kⱼ + 1) où kⱼ est la puissance du j-ième facteur premier.

Pour que d(n) = 3, il faut qu'il n'y ait qu'un seul facteur, et qu'il soit au carré. Les chiffres qui conviennent sont alors:

- 1, 1, p, p   avec p ∈ { 2, 3, 5, 7 }
- 1, 1, 1, p²   avec p ∈ { 2, 3 }

Le dénombrement donne 32.

> réponse: 32

Vérification en [Python](29.py).

```python
#!/usr/bin/env python3

from sympy.ntheory import factorint

nb = 0
for i in range(1000, 10000):
    p = 1
    n = i
    for _ in range(4):
        n, r = divmod(n, 10)
        p *= r

    nf = 1
    for k in factorint(p).values():
        nf *= k + 1
    if nf != 3:
        continue

    # print(i)
    nb += 1

print("réponse:", nb)
```

## Mardi 30 Novembre

La personne qui marche rapidement monte 75 marches. Celle qui marche lentement 50.

Soit a la vitesse de l'ascenseur et v celle de la personne lente, 3v est celle au pas rapide. Soit n le nombre de marches de l'ascenseur.

Exprimons le fait que l'ascenseur "monte" les marches restantes de la même vitesse que les personnes montent leurs marches:

- (n - 75) / a = 75 / 3v
- (n - 50) / a = 50 / v

⇒ (n - 50) / (n - 75) =  50 / 25 = 2

⇒ n - 50 = 2 (n - 75)

⇒ - 50 + 150 = n

> réponse: n = 100
