# Calendrier Mathématique Déccembre 2021

## Mercredi 1 Décembre

- 9 chiffres de 1 à 9
- 2 × 90 chiffres de 10 à 99
- 3 × 900 chiffres de 100 à 999
- 4 × 1022 chiffres de 1000 à 2021

Soit 9 + 2 × 90 + 3 × 900 + 4 × 1022 = 6977

Vérification en Python:

```python
len("".join(map(str, range(1, 2022))))
```

> réponse: 6977

## Jeudi 2 Décembre

Il n'y a que deux possibilités de suites sans nombres consécutifs à côté.

- 1 3 5 2 4
- 1 4 2 5 3

Elles correspondent d'ailleurs, au sens de rotation près.

Il y a donc 2 × 5 solutions.

Vérification avec [programme](02.py) Python.

```python
#!/usr/bin/env python3

import itertools

n = 0
for p in itertools.permutations("12345"):
    pp = "".join(p)  # recrée une chaine
    pp = pp + pp  # pour éliminer si le premier et le dernier sont consécutifs
    if "12" in pp or "23" in pp or "34" in pp or "45" in pp:
        continue
    if "21" in pp or "32" in pp or "43" in pp or "54" in pp:
        continue
    print("".join(p))
    n += 1
print("réponse:", n)
```

> réponse: 10

## Vendredi 3 Décembre

On a:

37² = AC² + AB²

AD² + AC² = CD² ⇒ AC² = 13² - 5² = 144 ⇒ AC = 12 cm

AB² = 37² - 144 = 1225

D'où AB = 35 cm et l'aire 35 × 12 / 2 = 210 cm²

> réponse: 210 cm²

## Lundi 6 Décembre

![schéma](06.png)

L'aire du triangle ABC est 8 cm². Les aires des petits triangles BED etc. est 2 cm². En effet E est le milieu de BC, G le milieu de CA et D le milieu de AD. Donc l'aire du trapèze est 6 cm².

> réponse: 6 cm²

## Mardi 7 Décembre

3n+2 est toujours impair. Donc les nombres à considérer doivent être impairs. De plus, ça ne peut pas être un multiple de 3 car 3n+2 n'est pas divisible par 3.

En carré impair entre 5 et 302 sans facteur 3, il y a 25 49 169 289.

- 25 - 2 = 22 pas divisible par 3 et pas ok
- 49 - 2 = 47 idem
- 169 - 2 = 167 idem
- 289 - 2 = 287 idem

> réponse: aucun

## Mercredi 8 Décembre

Autant compter avec un [programme](08.py).

```python
#!/usr/bin/env python3

import itertools
from sympy.ntheory import sieve

primes = sieve._list

n = 0
for p in itertools.permutations([2,4,6,8]):
    for a,b in zip([1,3,5,7],p):
        if a+b not in primes:
            break
    else:
        print(p)
```

> réponse: 6

## Jeudi 9 Décembre

![schéma](09.png)

On va essayer de maximiser l'aire du triangle APC.

Aire = AP × h / 2 avec h la hauteur issue de C. La valeur est maximale quand h = AC, qui est la plus grande valeur. Elle a pour valeur 20 × 15 / 2 = 150 cm².

Reste à vérifier si B est sur le cercle de 12 cm lorsque AP et AC sont perpendiculaires.

AC = √(AP² + AC²) = √(225 + 400) = √625 = 25.

La hauteur issue de P doit vérifier h × 25 / 2 = 150 pour que le calcul de l'aire soit correct. On trouve h = 12 cm. Donc AC coupe bien le cercle de 12 cm en un point P. De plus, B est tangent au cercle.

> réponse: 150 cm²

## Vendredi 10 Décembre

Soit a et p les âges de Arlette et Patrick en 2021.

- p - 3 = 3 (a - 3) / 4   ⇒   4p = 3a + 3  ①
- p + 3 = a - p + 20      ⇒   2p = a + 17  ②

① - 2 × ②   ⇒   a + 3 - 34 = 0, soit a = 31

> réponse: 31 ans
