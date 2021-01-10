# Calendrier Mathématique Mai 2021

## Lundi 3 Mai

Le triangle bleu ABP a la même aire que le triangle équilatéral ABO: même base AB, même hauteur h

Ainsi l'aire de la région bleue est la même l'aire du secteur OAB du disque, soit 1/6e du disque.

> réponse: π r² / 6

## Mardi 4 Mai

(x + 1) + (x + 2) / 2 + ... + (x + 2021) / 2021 = 2021

x × (1 + 1/2 + 1/3 + ... + 1/2021) + 2021 × 1 = 2021

x × 𝑨 = 0

La seule solution est x = 0

> réponse: 0

## Mercredi 5 Mai

1. orange > rouge
2. bleue > jaune
3. bleue et jaune non mitoyennes

Il y a trois possibilités pour les maisons bleues et jaunes:

1. BxJx
2. BxxJ
3. xBxJ

Et une fois celles-ci posées, les maisons orange et rouge ont leur place.

> réponse: 3

## Jeudi 6 Mai

21, 91, 161, ..., 1911, 1981, 2051

1981 = 21 + 70 * 28

Vérification Python:

```python
>>> sum(1 for i in range(1,2022) if i % 10 == 1 and i % 7 == 0)
29
```

> réponse: 29

## Vendredi 7 Mai

Soit a l'arête du cube.

- volume: a³ = 64 cm³ = 2⁶
- arête: a = 2² cm
- aire côté: a² = 2⁴ = 16 cm²
- aire cube: 16 × 6 = 96 cm²

> réponse: 96 cm²

## Lundi 10 Mai

Soit a = ∛(2 + √5) + ∛(2 - √5)

a³ = (2 + √5) + 3 × ∛(2 + √5)² × ∛(2 - √5) + 3 × ∛(2 + √5) × ∛(2 - √5)² + (2 - √5)

a³ = (2 + √5) + 3 × ∛(2 + √5) × ∛(2² - 5) + 3 × ∛(2 - √5) × ∛(2² - 5) + (2 - √5)

a³ = 4 - 3 × (∛(2 + √5) + ∛(2 - √5))

a³ = 4 - 3 × a

a³ + 3a - 4 = 0

(a - 1)(a² + a + 4) = 0

Une seule racine: a = 1

> réponse: 1

## Mercredi 12 Mai

Si (3n + 4) / (2n - 1) est entier, alors (3n + 4) / (2n - 1) - 2 aussi.

(3n + 4) / (2n - 1) - 2 = (6 - n) / (2n - 1)

Il faut que numérateur = 0 ou numérateur >= dénominateur: 6 - n >= 2n - 1 ⇒ 7 >= 3n

Donc trois valeurs pourraient convenir: 1, 2, 6

Si n = 1, (3 + 4) / (2 - 1) = 7 → ok

Si n = 2, (6 + 4) / (4 - 1) = 10 / 3 → ko

Si n = 6, (18 + 4) / (12 - 1) = 22 / 11 → ok

Donc 2 valeurs conviennent: n = 1 et n = 6

> réponse: 2 valeurs


## Jeudi 13 Mai

![schéma](13.png)

BFE = BCE = 90° (par construction)

BCEF est un quadrilatère cyclique: il existe un point G centre du cercle inscrit

théorème des angles aux centres: deux angles qui interceptent le même arc sont égaux. <br>
D'où: BEC = BFC

angle FBC = 90° - FBA = BAF car BAF triangle rectangle <br>
= AED  car AB et DE sont // <br>
= BEC car E milieu de DC <br>
D'où: FBC = BEC

en définitive, on a BEC = FBC = BFC

le triangle BCF est donc isocèle en C et BC = FC

> réponse: 3 cm

## Vendredi 14 Mai

1/2+1/5+1/10 = 7/10+1/10 = 8/10 = 4/5

10 × (4/5)⁻¹ = 10 × 5 / 4 = 25 / 2

> réponse: 25 / 2


## Lundi 17 Mai

il faut faire 16 17 ou 18

soit (selon le premier dé):

- 6-6-6 6-6-5 6-5-5 6-5-6 6-6-4 6-4-6
- 5-6-6 5-5-6 5-6-5
- 4-6-6

soit 10 jets possibles

vérification en Python:

```python
>>> sum(1 for a in range(1,7) for b in range(1,7) for c in range(1,7) if a+b+c>15)
10
```

il y a 6³ = 216 jets possibles. La probabilité de faire plus de quinze est 10 / 216 = 5 / 108

> réponse: 5 / 108

## Mercredi 19 Mai

aire trapèze : (L + l) × h / 2

aire ABFE:  h × (3 + 1) / 2 = 2 h

aire CDEF:  (3 - h) × (3 + 1) / 2 = 2 × (3 - h)

aire bleue:  2 h + 6 - 2 h = 6 cm²

> réponse: 6 cm²

## Jeudi 20 Mai

Chaque jour Kikikou mange 1/3 + 1/4 = 7/12 de boîte par jour, soit 6 / (7/12) = 72 / 7 de cagette

Le chat a à manger pendant un peu plus de 10 jours, il finira le 11ème jour.

> réponse: jeudi de la semaine suivante

## Vendredi 21 Mai

```
X-X-X
-----
X-X-X
-----
X-X-X
```

> réponse: 9

## Mecredi 26 Mai

Edouard effectue 40 km. Pour les faire en 24 min, il doit rouler à:

40 / 24 × 60 = 100 km/h

> réponse: 100 km/h

## Jeudi 27 Mai

Il est possible que les 4 conjoints 1 arrivent en premier. La cinquième personne formera forcément un couple.

> réponse: 5

## Lundi 31 Mai

![schéma](31.png)

AC = √(3² + 4²) = 5

aire ABC = 3 × 4 / 2 = 6 cm²

formule de Héron: aire ACD : √(p(p-a)(p-b)(p-c)) avec p = (a+b+c)/2

p = (5 + 5 + 6) / 2 = 8

aire ACD = √(8 (8 - 5) (8 - 5) (8 - 3)) = √(8 × 3 × 3 × 2) = 3 × 4 = 12 cm²

> réponse: 18 cm²
