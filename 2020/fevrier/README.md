# Calendrier Mathématique Février 2020

## Lundi 3 Février

## Mardi 4 Février

L'hexagone est rempli de:

- 7 petits hexagones, eux-mêmes équivalents à 6 petits triangles équivaléraux, soit 42
- 12 petits triangles équilatéraux

L'aire coloriée est constituée de:

- 6 petits triangles
- 1 hexagone, soit 6 petits triangles

La proportion est donc: (6 + 6) / (42 + 12) = 2 / 9

> réponse: 2 / 9

## Mercredi 5 Février

[Programme](05.py) Python.

```python
#!/usr/bin/env python3


def rev(n):
    """ Retourne le nombre n écrit à l'envers dans sa représentaiton décimale. """
    u = 0
    while n != 0:
        n, r = divmod(n, 10)
        u = u * 10 + r
    return u


print("réponse:", sum(1 for n in range(100, 1000) if rev(n) > n))
```

> réponse: 360

## Jeudi 6 Février

- susie < marie
- laurie < lucie
- noémie = rosie
- sophie < susie
- laurie = marie
- lucie < noémie

- sophie < susie < marie = laurie < lucie < noémie = rosie

> réponse: Sophie

## Vendredi 7 Février

[Programme](07.py) Python.

```python
#!/usr/bin/env python3

s = 0
for n in range(10, 100):
    d, u = divmod(n, 10)
    if n + (d + u) ** 2 == u * 10 + d:
        print(n)
        s += n

print("réponse:", s)
```

> réponse: 27

## Lundi 10 Février

La face qui touche les dés 2 et 3 est 1 puisque les 5 autres nombres sont visibles.

Donc la face entre les dés 1 et 2 est 6. Et par conséquant la face cherchée est 1.

> réponse: 1

## Mardi 11 Février

## Mercredi 12 Février

## Jeudi 13 Février

![schéma](13.png)

Le centre du cercle est sur la droite AB et le point F est tel que EF est la hauteur issue de E du triangle ACE.

EF × AC = AE × CE

EF × 1 = ½ × √(1 - ½²) = √3 / 4

> réponse: √3 / 4 cm

## Vendredi 14 Février

√(x - 9) - √(x - 16) = 1

élevons au carré: 2x - 25 - 2 √((x - 9) (x - 16)) = 1

simplifions: x - 13 = √((x - 9) (x - 16))

élevons encore au carré: x² -  26x + 169 = x² - 25x + 144

simplifions: x = 169 - 144

d'où: x = 25

> réponse: x = 25

## Lundi 17 Février

## Mardi 18 Février

## Mercredi 19 Février

## Jeudi 20 Février

## Vendredi 21 Février

## Lundi 24 Février

## Mardi 25 Février

## Mercredi 26 Février

## Jeudi 27 Février

## Vendredi 28 Février
