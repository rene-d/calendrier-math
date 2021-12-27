# Calendrier Mathématique Février 2022

[Solutions 2022](../README.md) - [Homepage](../../README.md)

## Mardi 1 Février

![01](./01.png)

### Construciton géométrique

![latexml](https://render.githubusercontent.com/render/math?math=%5Cfrac%20%7BPB%7D%20%7BPC%7D%20%5Ctimes%20%5Cfrac%20%7BPC%7D%20%7BPA%7D%20%3D%20%5Cfrac%201%202%5Ctimes%5Cfrac%202%203%3D%5Cfrac%201%203)

autrement dit:
![latexml](https://render.githubusercontent.com/render/math?math=%5Cfrac%20%7BBP%7D%20%7BBA%7D%20%3D%20%5Cfrac%201%204)

### Résolution analytique

Considérons le repère orthonormé où les points B, P, A ont pour coordonnées respectives (-2; 0), (-1, 0) et (2; 0).

coordonnées du point C:
![latexml](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Balign%7D%0Ax_C%20%26%3D%20-%20%5Cfrac%201%202%20%20%20%20%20%20%20%5C%5C%0Ay_C%20%26%3D%20%5Csqrt%20%7B2%5E2%20-%20%7B%5Cleft%28%5Cfrac%201%202%20%5Cright%29%7D%5E2%7D%20%3D%20%5Cfrac%20%7B%5Csqrt%20%7B15%7D%7D%202%0A%5Cend%7Balign%7D)

distance BC:
![latexml](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Balign%7D%0ABC%20%26%3D%20%5Csqrt%20%7B%7B%5Cleft%28x_C-x_B%5Cright%29%7D%5E2%20%2B%20%7B%5Cleft%28y_C-y_B%5Cright%29%7D%5E2%7D%20%5C%5C%0A%26%3D%20%5Csqrt%20%7B%20%7B%5Cleft%28%20-%20%5Cfrac%201%202%20-%20%28-2%29%20%5Cright%29%7D%5E2%20%2B%20%7B%5Cleft%28%20%5Cfrac%20%7B%5Csqrt%20%7B15%7D%7D%202%20-%200%20%5Cright%29%7D%5E2%7D%20%5C%5C%0A%26%3D%20%5Csqrt%20%7B%5Cfrac%209%204%20%2B%20%5Cfrac%20%7B15%7D%204%7D%20%5C%5C%0A%26%3D%20%5Csqrt%20%7B6%7D%0A%5Cend%7Balign%7D)

distance CA en utilisant Pythagore:
![latexml](https://render.githubusercontent.com/render/math?math=CA%3D%5Csqrt%7B%7BAB%7D%5E2-%7BBC%7D%5E2%7D%3D%5Csqrt%7B16-6%7D%3D%5Csqrt%7B10%7D)

d'où le rapport ![latex](https://render.githubusercontent.com/render/math?math=%5Cfrac%20%7BCB%7D%20%7BCA%7D&mode=inline):
![latexml](https://render.githubusercontent.com/render/math?math=%5Cfrac%20%7BCB%7D%20%7BCA%7D%20%3D%20%5Cfrac%20%7B%5Csqrt%20%7B6%7D%7D%20%7B%5Csqrt%20%7B10%7D%7D%20%3D%20%5Csqrt%20%5Cfrac%203%205)

> réponse: √(3/5)

## Mercredi 2 Février

Avec les chiffres des unités, on déduit que X + Y = 10 puisque X + Y + Z ≡ Z (mod 10).

Avec la retenue qui en suit, on sait que X = Z + 1.

- X + Y + Z + 1 = 10 * Y + X
- 10 + X = 10 * Y + X
- 10 = 10 * Y
- Y = 1

Et par conséquence : X = 9 et Z = 8

Vérification:

```text
     9 9 9 9
   + 1 1 1 1
   + 8 8 8 8
────────────
   1 9 9 9 8
```

> réponse: Z = 8

## Jeudi 3 Février

![latexml](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Balign%7D%0AM%20%26%3D%20%5Cfrac%20%7B%20%5Csum%20%7B%28a_i%20%2B%20a%7D%29%7D%20n%0A%5C%5C%0AN%20%26%3D%20%5Cfrac%20%7B%20%5Csum%20%7B%20a_i%20%7D%7D%20%7Bn-1%7D%0A%5Cend%7Balign%7D)

![latexml](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Balign%7D%0AM%20-%20N%20%26%3D%20%20%5Cfrac%20%7B%20%5Csum%20%7B%28a_i%20%2B%20a%7D%29%7D%20n%20-%20%5Cfrac%20%7B%20%5Csum%20%7B%20a_i%20%7D%7D%20%7Bn-1%7D%0A%5C%5C%0A%26%3D%20%20%20%5Cfrac%20%7B%20%5Csum%20%7B%28a_i%20%2B%20a%7D%29%7D%20n%20-%20%5Cfrac%20n%20%7Bn-1%7D%20%5Cleft%28%0A%20%20%20%20%20%20%20%20%5Cfrac%20%7B%5Csum%20%7B%20a_i%20%7D%7D%20%20n%20%2B%20%5Cfrac%20a%20n%20-%20%5Cfrac%20a%20n%20%5Cright%29%0A%5C%5C%0A%26%3D%20M%20-%20%5Cfrac%20n%20%7Bn-1%7D%20%5Cleft%28M%20-%20%5Cfrac%20a%20n%20%5Cright%29%0A%5C%5C%0A%26%3D%20M%20%5Cleft%28%201%20-%20%5Cfrac%20n%20%7Bn-1%7D%20%5Cright%29%20%2B%20%5Cfrac%20%7Ba%7D%20%7Bn-1%7D%0A%5C%5C%0A%26%3D%20-%20%5Cfrac%20M%20%7Bn%20-%201%7D%20%2B%20%5Cfrac%20%7Ba%7D%20%7Bn-1%7D%0A%5C%5C%0A%26%3D%20%5Cfrac%20%7Ba-M%7D%20%7Bn%20-%201%7D%0A%5Cend%7Balign%7D)

> réponse: (a - M) / (n - 1)

## Vendredi 4 Février

Programme [Python](04.py)

C'est le nombre de permutations des éléments ABC A B C, dans lequel il ne faut compter qu'une fois le doublon constitué par "ABC A B C" et "A B C ABC".

> réponse: 23

## Lundi 7 Février

## Mardi 8 Février

On équilibre le contenu des boîtes en déplaçant la moitié de la différence (qui est paire, puisque p et q sont impairs): (p - q) / 2. En déplaçant un chocolat de plus, la boîte B en aura plus que la boîte A.

> réponse: (p - q) / 2 + 1

## Mercredi 9 Février

## Jeudi 10 Février

## Vendredi 11 Février

## Lundi 14 Février

## Mardi 15 Février

## Mercredi 16 Février

## Jeudi 17 Février

## Vendredi 18 Février

## Lundi 21 Février

## Mardi 22 Février

## Mercredi 23 Février

## Jeudi 24 Février

## Vendredi 25 Février

## Lundi 28 Février
