# Calendrier Mathématique Août 2020

## Lundi 3 Août

## Mardi 4 Août

En développant:

- ab + ac = 152
- bc + ba = 162
- ca + cb = 170

Notons x = ab, y = bc et z = ca. Les équations peuvent s'écrire:

- x + z = 152
- y + x = 162
- z + y = 170

Ce qui se résout en: x = 72, y = 90, z = 80

xyz = ab × bc × ca = (abc)² = 72 × 90 × 80 = 518400 = 720²

Nota: la solution positive au système initial est: a = 8, b = 9, c = 10

> réponse: 720

## Mercredi 5 Août

## Jeudi 6 Août

Soient r₁ et r₂ les rayons des deux cercles en centimètres.

A₁ - A₂ = π (r₁² - r₂²) = 72 π

r₁ + r₂ = 1800

(r₁ + r₂)(r₁ - r₂) = 72 ⇒ (r₁ - r₂) = 72 / 1800 = 1 / 25

2r₁ = 1800 + 1 / 25

On en déduit r₁ - 45001 / 50 et r₂ = 45001 / 50 = 1 / 25 = 44999 / 50

> réponse: 44999 / 50 et 45001 / 50

## Vendredi 7 Août

Comme 100 = 9 + 9 + 82, le plus petit nombre "centenaire" possible est 82. Il faut tester ensuite...

Le [programme](07.py) Python le fait pour nous.

```python
#!/usr/bin/env python3

nb = 0
for a in range(80, 100):
    for b in range(a, 100):
        n1 = a + (b // 10) + (b % 10)
        n2 = b + (a // 10) + (a % 10)
        if n1 == n2 == 100:
            print(a, b)
            nb += 1
print("réponse:", nb)
```

Il y a donc cinq "paires centenaires": (83, 89) (84, 88) (85, 87) (8,6 86) (90, 91)

> réponse: 5

## Lundi 10 Août

Si Jean choisit le dé 4-0:

- 0 est toujours perdant (i.e. Léa gagne)
- 4 est perdant 5 fois sur 18 tirages possibles

2/6 + 4/6 × 5/18 = 14/27

Si Jean choisit le dé 3:

- 3 est perdant 4+2+3 = 9/18 = 1/2

Si Jean choisit le dé 6-2:

- 2 est perdant 4+6+3: 4/6 × 13/18 = 13/27
- 6 est toujours gagnant

Si Jean choisit le dé 5-1:

- 1 est perdant 4+6+6 fois: 3/6 × 16/18
- 5 est perdant 2 fois: 3/6 × 2/18

3/6 × 2/18 + 3/6 × 16/18 = 1/2

Soit au total:

1/4 × (14/27 + 1/2 + 13/27 + 1/2) = 1/4 × 2 = 1/2

> réponse: Léa a une chance sur deux de gagner: p = 1/2

## Mardi 11 Août

Soit d le chiffre des dizaines de n et u celui des unités.

Ils sont solution de l'équation:

d × u + d + u = 10 × d + u

d × u + d = 10 × d

u + 1 = 10  (car d ≠ 0)

Soit, u = 9 et d quelconque.

Autrement dit, tous les nombres qui se terminent par 9 entre 10 et 90.

> réponse: 8

## Mercredi 12 Août

## Jeudi 13 Août

![latex](https://render.githubusercontent.com/render/math?math=k%3D%5Cfrac%7B9n%5E2%2B31%7D%7Bn%5E2%2B7%7D%3D%5Cfrac%7B9n%5E2%2B63-32%7D%7Bn%5E2%2B7%7D%3D9-%5Cfrac%7B32%7D%7Bn%5E2%2B7%7D&mode=inline)

Il faut donc que 𝑛²+7 divise 32.

- 𝑛=1: 𝑛²+7=8 ✅
- 𝑛=2: 𝑛²+7=11 et 11 ne divise pas 32 ❌
- 𝑛=3: 𝑛²+7=16 convient ✅
- 𝑛=4: 𝑛²+7=23 non ❌
- 𝑛=5: 𝑛²+7=32 ok ✅

> réponse: 𝑛 = ±1 ±3 ±5

## Vendredi 14 Août

## Lundi 17 Août

## Mardi 18 Août

## Mercredi 19 Août

## Jeudi 20 Août

## Vendredi 21 Août

## Lundi 24 Août

## Mardi 25 Août

## Mercredi 26 Août

## Jeudi 27 Août

## Vendredi 28 Août

## Lundi 31 Août
