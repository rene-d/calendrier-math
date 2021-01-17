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
