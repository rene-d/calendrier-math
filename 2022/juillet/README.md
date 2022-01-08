# Calendrier Mathématique Juillet 2022

[Solutions 2022](../README.md) - [Homepage](https://rene-d.github.io/calendrier-math/)

## Vendredi 1 Juillet

Soit ![latex](https://render.githubusercontent.com/render/math?math=x%3D10b%2Ba%2Cy%3D10c%2Bb%2Cx%5E2%3Dy%5E3&mode=inline). Que vaut ![latex](https://render.githubusercontent.com/render/math?math=a%2Bb%2Bc&mode=inline) ?

Si on ramène les nombres à leur décomposition en facteurs premiers, on voit que ![latex](https://render.githubusercontent.com/render/math?math=x&mode=inline) doit être un cube et ![latex](https://render.githubusercontent.com/render/math?math=y&mode=inline) un carré. Or, les cubes à deux chiffres sont 27 et 64.

On a donc pour choix ![latex](https://render.githubusercontent.com/render/math?math=b%3D2%2C%20a%3D7&mode=inline) ou ![latex](https://render.githubusercontent.com/render/math?math=b%3D6%2C%20a%3D4&mode=inline), et donc ![latex](https://render.githubusercontent.com/render/math?math=y%3D%5Csqrt%5B3%5D%7B%7B27%7D%5E2%7D%3D%7B%5Cleft%28%5Csqrt%5B3%5D%7B27%7D%5Cright%29%7D%5E2%3D3%5E2%3D9&mode=inline) ou  ![latex](https://render.githubusercontent.com/render/math?math=y%3D%5Csqrt%5B3%5D%7B%7B64%7D%5E2%7D%3D16&mode=inline).

La première solution ne convient pas car ![latex](https://render.githubusercontent.com/render/math?math=b&mode=inline) vaudrait 0 ce qui est contraire à l'énoncé.

La deuxième implique ![latex](https://render.githubusercontent.com/render/math?math=a%3D4&mode=inline) et ![latex](https://render.githubusercontent.com/render/math?math=b%3D6&mode=inline), ce qui est correct. Donc ![latex](https://render.githubusercontent.com/render/math?math=c%3D1&mode=inline).

![latex](https://render.githubusercontent.com/render/math?math=a%2Bb%2Bc%3D4%2B6%2B1%3D11&mode=inline)

> réponse: 11

## Lundi 4 Juillet

```text
    S E R V I
  ×         4
  ───────────
    I V R E S
```

On part de `I`=8 et `S`=2, puis `E`=1 pour éviter la retenue, etc.

```text
    2 1 9 7 8
  ×         4
  ───────────
    8 7 9 1 2
```

> réponse: 21978 × 4 = 87912

## Mardi 5 Juillet

n² + 6n = n (6 + n)

Pour qu'il n'y ait qu'un diviseur premier, il faut que n et n+6 soient une puissance d'un nombre premier. Et que ce nombre premier divise aussi n+6, donc 6.

n=1 convient car 6+1=7 et 7 est premier.

6 est divisible par 2 et par 3: 2×(2+6)=16=2⁴, 3×(3+6)=27=3³

> réponse: 1 2 3

## Mercredi 6 Juillet

Il faut résoudre dans 𝐍 ab = 2(a+b).

- ab - 2a - 2b = 0
- a(b - 2) - 2(b - 2) - 4 = 0
- (a - 2)(b - 2) = 4

On en déduit que a-2 et b-2 sont des diviseurs de 4.

Donc a peut valoir 4+2 ou 2+2 ou 1+2, et b respectivement 1+2, 2+2, 4+2.

Ce qui donne soit un carré 4×4 soit un rectangle 6×3. Ou bien soit n=16 soit n=18.

> réponse: 16 et 18

## Jeudi 7 Juillet

| voyage | reste sur rive 1 | aller | retour | reste sur la rive 2
| ------ | ---------------- | ----- | ------ | -------------------
|    1   |   H1    H2 F3 H3 | F1 F2 | F1     |       F2
|    2   |   H1    H2    H3 | F1 F3 | F1     |       F2    F3
|    3   |         H2    H3 | F1 H1 | F2     | F1 H1       F3
|    4   |               H3 | F2 H2 | F3     | F1 H1 F2 H2
|    5   |                  | F3 H3 |        | F1 H1 F2 H2 F2 H3

> réponse: oui, en 9 trajets

## Vendredi 8 Juillet

On a ![latex](https://render.githubusercontent.com/render/math?math=xy%3D4%28y-x%29&mode=inline).

![latexml](https://render.githubusercontent.com/render/math?math=%5Cfrac%7B2y%2B12%28y-x%29-2x%7D%7By-x-8%28y-x%29%7D%0A%3D%5Cfrac%7B%2812%2B2%29%28y-x%29%7D%7B%281-8%29%28y-x%29%7D%0A%3D-%5Cfrac%7B14%7D7%3D-2)

> réponse: -2

## Lundi 11 Juillet

> réponse: 8.50€

## Mardi 12 Juillet

L'aire du carré jaune est 25 cm² donc son côté 5 cm et sa diagonale 5√2 cm. Cette dernière est le diamètre du petit cercle, qui est aussi le côté du carré médian. La diagonale du carré médian est dans 5√2×√2 = 10 cm, qui est le diamètre du grand cercle, et le côté du carré ABCD.

> réponse: 100 cm²

## Mercredi 13 Juillet

![13](13.png)

> réponse: les deux carrés au milieu

## Jeudi 14 Juillet

La condition ![latex](https://render.githubusercontent.com/render/math?math=15a-13b%3D1&mode=inline) peut s'écrire:

![latexml](https://render.githubusercontent.com/render/math?math=b%3D%5Cfrac%20%7B15a-1%7D%7B13%7D%20%5Cle%20500%0A%5Cimplies%0Aa%20%5Cle%20%5Cfrac%20%7B500%5Ctimes%2013%2B1%7D%7B15%7D%20%3D%20433.4)

C'est ![latex](https://render.githubusercontent.com/render/math?math=a&mode=inline) qui limite, car la condition ci-dessus n'impose pas la limite 500 pour ![latex](https://render.githubusercontent.com/render/math?math=b&mode=inline).

Le plus petit ![latex](https://render.githubusercontent.com/render/math?math=a&mode=inline) qui convienne est ![latex](https://render.githubusercontent.com/render/math?math=a%3D7&mode=inline). Donc ![latex](https://render.githubusercontent.com/render/math?math=a%3D7%2B13k&mode=inline).

![latex](https://render.githubusercontent.com/render/math?math=7%2B13k%20%5Cle%20433%20%5Cimplies%20k%3D32%20%5Cimplies%20a%3D423&mode=inline)

![latex](https://render.githubusercontent.com/render/math?math=a%3D423&mode=inline) est la plus grande valeur possible pour a.
Ceci implique _de facto_ ![latex](https://render.githubusercontent.com/render/math?math=b%3D%5Cfrac%7B15%5Ctimes%20423-1%7D%7B13%7D%3D488&mode=inline).

Finalement: ![latex](https://render.githubusercontent.com/render/math?math=a%2Bb%3D423%2B488%3D911&mode=inline)

Vérification en Python:

```python
print(max((a + b, a, b)
          for a in range(501) for b in range(501)
          if 15 * a - 13 * b == 1))
```

> réponse: 911

## Vendredi 15 Juillet

On doit avoir 3 × a = 𝑥8, donc a = 6. On vérifie aisément que 6 est la solution: 6 + 66 + 666 = 738.

> réponse: 6

## Lundi 18 Juillet

Les triangles sont isocèles et rectangles (pour que les triangles remplissent le coin du rectangle).

Leur diagonale vaut donc 2√2. Et l'aire du rectangle: 3×2√2 × 2×2√2 = 48

> réponse: 48 cm²

## Mardi 19 Juillet

Il y a 9 barres noires et 8 blanches. Donc 8-3=5 barres noires épaisses et par conséquent 4 barres blanches fines.

> réponse: 4

## Mercredi 20 Juillet

Le vol dure 11h. Le repas est donc servi à 19h30.

> réponse: 19h30

## Jeudi 21 Juillet

Sur chaque extrêmité il y a 4 cordes : il faut donc 4×10=40 extrêmités de corde en tout. Et une corde a deux extrémités.

> réponse: 20

## Vendredi 22 Juillet

## Lundi 25 Juillet

Le critère de divisibilité par 4 est que les deux derniers chiffres forment un nombre dvisible par 4. Avec les chiffres donnés, on peut former:

- 24
- 32, 36
- 52, 56
- 64
- 72, 76

Soit 8 terminaisons possibles. Avec les quatre autres chiffres, on peut former 4!=24 nombres par terminaison.

D'où 8×24 = 192 nombres

> réponse: 192

## Mardi 26 Juillet

Conditions:

- Rouge ≥ 1, Bleu ≥ 1, Vert ≥ 1
- Rouge + Vert ≥ 10
- Vert + Bleu ≥ 20
- Bleu + Rouge ≥ 40

Il faut au moins 41 billes: 40 bleues et rouges et 1 verte.

Exemple:

- 20 billes rouges
- 20 billes bleues
- 1 bille verte

> réponse: 41

## Mercredi 27 Juillet

- Il y a 12 triangles de côté 1.
- Il y a 6 triangles de côté 2.
- Il y a 2 triangles de côté 3.

## Jeudi 28 Juillet

![28](28.png)

L'angle ∠ABM vaut 180 - 48 - 84 = 48°, donc le triangle ABM est isocèle en A.

AM = MD par définition et AB = DC parce que ABCD est un parallelogramme. Donc MDC est également isocèle en D.

L'angle ∠MDC vaut 180 - 84 = 96°, parce que ABCD est un parallélogramme. Et donc l'angle ∠DCM vaut (180 - 96) / 2 = 42°

> réponse: 42°

## Vendredi 29 Juillet

Posons: ![latex](https://render.githubusercontent.com/render/math?math=X%3Dx%5E%7B20%7D&mode=inline) et ![latex](https://render.githubusercontent.com/render/math?math=Y%3Dy%5E%7B20%7D&mode=inline)

L'équation devient: ![latex](https://render.githubusercontent.com/render/math?math=X%5E2-XY%2BY%5E2%3D0&mode=inline)

![latex](https://render.githubusercontent.com/render/math?math=X%3D%5Cfrac%201%202%20%5Cleft%28%20Y%20%5Cpm%20%5Csqrt%20%7BY%5E2-4Y%5E2%7D%20%5Cright%29%3D%5Cfrac%201%202%20Y%20%5Cleft%28%201%20%5Cpm%20%20i%20%5Csqrt%20%7B3%7D%20%5Cright%29&mode=inline)

On voit que la seule solution réelle est Y=0 et X=0.

> réponse: un couple: (0, 0)
