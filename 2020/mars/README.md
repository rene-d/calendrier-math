# Calendrier Mathématique Mars 2020

## Lundi 2 Mars

On écrit les équations de l'énoncé:

- pomme + poire = 24
- pomme = poire - 6

Ce qui donne: 2 poire = 24 + 6, poire = 15. Et pomme = 9.

> réponse: 5 / 3

## Mardi 3 Mars

```text
0   1   2   3   4   5   6   6   8   9
C           A   D           B       E
```

> réponse: C A D B E

## Mercredi 4 Mars

cos 45° = √2 / 2

Donc l'aire du segment coloré est l'aire d'un quart de cercle moins l'aire du triangle isocèle rectangle de côté 1.

Soit: π / 4 - 1 / 2

> réponse: π / 4 - 1 / 2 cm²

## Jeudi 5 Mars

a × b × c = 3 × (a + b + c)

Supposons 0 < a ≤ b ≤ c

a × b = 3 × (a / c + b / c + 1) ≤ 3 × (1 + 1 + 1) = 9 ⇔ a × b ≤ 9

car a / c ≤ 1 et b / c ≤ 1.

Exprimons c en fonction de a,b:

abc - 3c = 3(a+b) ⇒ c = 3 (a + b) / (a b - 3)

```python
for a in range(1,10):
    for b in range(1,10):
        if a * b <= 9 and a <= b:
            if a * b != 3:
                c = 3 * (a + b) / (a * b - 3)
                if b <= c and int(c) == c:
                    print(a,b,c)
```

Les solutions sont:

1. 1 4 15
2. 1 5 9
3. 1 6 7
4. 2 2 12
5. 2 3 5
6. 3 3 3

> réponse: 6 triplets

## Vendredi 6 Mars

> réponse: 2 heures et 1 minute

## Lundi 9 Mars

## Mardi 10 Mars

## Mercredi 11 Mars

## Jeudi 12 Mars

## Vendredi 13 Mars

## Lundi 16 Mars

## Mardi 17 Mars

## Mercredi 18 Mars

## Jeudi 19 Mars

## Vendredi 20 Mars

## Lundi 23 Mars

## Mardi 24 Mars

## Mercredi 25 Mars

## Jeudi 26 Mars

## Vendredi 27 Mars

## Lundi 30 Mars

## Mardi 31 Mars
