# Calendrier Mathématique Septembre 2021

[Solutions 2021](../README.md) - [Homepage](../../README.md)

## Mercredi 1 Septembre

Le critère de divisibilité par 3 est que la somme des chiffres soit multiple de 3.

> réponse: 1 4 7

## Jeudi 2 Septembre

Cela revient à compter le nombre de rectangles ci-dessous:

```text
X
XX
XXX
XXXX
XXXXX
```

Il y a 15 rectangles. Chaque rectangle est le coin inférieur gauche d'un autre rectangle.

Sur ligne du bas, de gauche à droite: on peut faire:

- 5+4+3+2+1 = 15 rectangles (5 de hauteur 1, 4 de hauteur 2, 3 de hauteur 3, etc.)
- 4+3+2+1 = 10 (4x1, 3 de h2, 2 h3, 1 de h4)
- 3+2+1 = 6
- 2+1 = 3
- 1 = 1

Soit 35 pour la dernière ligne.

Pour l'avant-dernière ligne:

- 4+3+2+1 = 10
- 3+2+1
- 2+1
- 1

Soit 20.

De même, 10 en partant la ligne du milieu, puis 4, puis 1.

Au total: 35+20+10+4+1 = 70

Nota: la formule générale est n(n+1)(n+2)(n+3)/24 - cf. [A000332](https://oeis.org/A000332).

> réponse: 70

## Vendredi 3 Septembre

x⁴ - 51x² + 50 = (x² - 1)(x² - 50)

Donc pour x² strictement compris entre 1 et 50, le polynome sera strictement négatif. Dans 2 ≤ ∣x∣ ≤ 7

> réponse: -7 à -2 et 2 à 7

## Lundi 6 Septembre

La quadrilatère est le carré inscrit dans le cercle.

> réponse: 2 cm²

## Mardi 7 Septembre

La condition peut s'écrire: 10 a + b = a + b + c ⇒ 9 a = c

La seule possibilité est a = 1 et c = 9

> réponse: c = 9

## Mercredi 8 Septembre

Les chiffres utilisables sont 1 et 2.

Voici les possibilités: 20000 10001 10010 10100 11000

> réponse: 5

## Jeudi 9 Septembre

ADC et ABC sont des triangles rectangles. On a donc:

AC² = AD² + AC² = 10 + 11 = 21

AB² + BC² = AC² = 21 ⇒ AB = √(21 - 12) = 3

> réponse: 3 cm

## Vendredi 10 Septembre

Le coefficient ![latex](https://render.githubusercontent.com/render/math?math=r&mode=inline) entre deux termes vaut:

![latexml](https://render.githubusercontent.com/render/math?math=r%20%3D%20%5Cfrac%7B%5Csqrt%5B3%5D%7B3%7D%7D%7B%5Csqrt%7B3%7D%7D%20%3D%20%5Cfrac%7B3%5E%7B%5Cfrac%7B1%7D%7B3%7D%7D%7D%7B3%5E%7B%5Cfrac%7B1%7D%7B2%7D%7D%7D%20%3D%20%7B3%7D%5E%7B%5Cfrac%7B1%7D%7B3%7D-%5Cfrac%7B1%7D%7B2%7D%7D%20%3D%20%7B3%7D%5E%7B-%5Cfrac%7B1%7D%7B6%7D%7D)

Le terme suivant est donc:

![latexml](https://render.githubusercontent.com/render/math?math=%5Csqrt%5B6%5D%7B3%7D%5Ctimes%7B3%7D%5E%7B-%5Cfrac%7B1%7D%7B6%7D%7D%20%3D%20%7B3%7D%5E%7B%5Cfrac%7B1%7D%7B6%7D-%5Cfrac%7B1%7D%7B6%7D%7D%20%3D%203%5E0%20%3D%201)

> réponse: 1

## Lundi 13 Septembre

Il s'agit du plus petit nombre premier qui suit 23, à savoir 29.

> réponse: 29

## Mardi 14 Septembre

En dessous de la diagonale:

- trois 1x1
- deux 2x2
- un 3x3

Idem au dessus de la diagonale.

> réponse: 12

## Mercredi 15 Septembre

![schéma](15.png)

Soit C' le symétrique de C par rapport à AB et B' le symétrique de B par rapport à AC.

On a donc EB = EB' et DC = DC'. Donc BE+ED+DC = B'E+ED+DC'.

La plus court chemin de B' à C' étant la ligne droite, il faut calculer cette distance qui sera la longueur minimale recherchée.

Par construction des points B' et C', l'angle ∠C'AB' est le triple de ∠BAC, soit 120°.

La [loi des cosinus](https://fr.wikipedia.org/wiki/Loi_des_cosinus) permet de calculer B'C':

![latexml](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Baligned%7D%0A%28B%27C%27%29%5E2%26%3D%28AC%27%29%5E2%2B%28AB%27%29%5E2-2%28AC%27%29%28AB%27%29cos%28120%5E%7B%5Ccirc%7D%29%20%5C%5C%0A%26%3D6%5E2%2B10%5E2-2%5Ctimes%2010%5Ctimes%206%5Ctimes%20%5Cleft%28-%5Cdfrac%7B1%7D%7B2%7D%5Cright%29%20%5C%5C%0A%26%3D136%2B60%3D196%20%5C%5C%0A%26%3D%7B14%7D%5E2%0A%5Cend%7Baligned%7D)

> réponse: 14 cm

## Jeudi 16 Septembre

Trois équations à trois inconnues:

Soit sg la somme des notes des garçons, sf celles des filles, ng le nombre de garçons.

- (sf + sg) / 40 = 66
- sg / ng = 60
- sf / (40 - ng) = 70

- sf = 2640 - sg
- ng = sg / 60
- sf = 70 × (40 - sg / 60)

2640 - sg = 70 × (40 - sg / 60) ⇒ sg = 960

Le nombre de garçons est: 960 / 60 = 16

> réponse: 16

## Vendredi 17 Septembre

1225 = 5² × 7²

Les nombres qui conviennent sont les permutations différentes de 5577.

5577 5757 5775 7557 7575 7755

> réponse: 6

## Lundi 20 Septembre

Soit (![latex](https://render.githubusercontent.com/render/math?math=a_i&mode=inline)) la série des 1000 nombres. ![latex](https://render.githubusercontent.com/render/math?math=%28a_i%29%3D0&mode=inline) est une solution triviale. Et dès qu'il y a un nombre égal à 0, son voisin est aussi égal à 0, etc. Donc tous les nombres sont nuls ou aucun ne l'est.

```text
N B N B N B
    n*0*n
  b+0+b
```

- Si un blanc = 0, un noir doit être = 0 pour n × n = 0.
- Si un noir = 0, alors le blanc = 0 parce que = 0 × l'autre voisin

Supposons donc ici que ![latex](https://render.githubusercontent.com/render/math?math=a_i%20%5Cne%200&mode=inline). Dès la deuxième égalité, on va voir que ![latex](https://render.githubusercontent.com/render/math?math=a_1%5Cne1&mode=inline) (sinon ![latex](https://render.githubusercontent.com/render/math?math=a_0&mode=inline) serait forcément égal à 0 et tous les nombres seraient aussi égaux à 0 comme vu ci-avant, ce qui provoque une contradiction).

![latexml](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Baligned%7D%0Aa_0%2Ba_2%3Da_1%20%5Cimplies%20%26a_2%3Da_1%20-%20a_0%20%5C%5C%0Aa_1%5Ctimes%20a_3%3Da_2%20%5Cimplies%20%26a_3%3D%28a_1%20-%20a_0%29%20/%20a_1%3D1-a_0/a_1%20%5C%5C%0Aa_2%2Ba_4%3Da_3%20%5Cimplies%20%26a_4%3D%28a_1%20-%20a_0%29%20/%20a_1%20-%20%28a_1%20-%20a_0%29%20%5C%5C%0Aa_3%5Ctimes%20a_5%3Da_4%20%5Cimplies%20%26a_5%3D%5Cfrac%7B%28a_1%20-%20a_0%29%20/%20a_1%20-%20%28a_1%20-%20a_0%29%7D%20%7B%28a_1%20-%20a_0%29%20/%20a_1%7D%20%3D%201%20-%20a_1%20%5C%5C%0Aa_4%2Ba_6%3Da_5%20%5Cimplies%20%26a_6%3D%281%20-%20a_1%29%20-%20%5Cleft%5B%20%28a_1%20-%20a_0%29%20/%20a_1%20-%20%28a_1%20-%20a_0%29%20%5Cright%5D%20%3D%20a_0%20%281%20-%20a_1%29/a_1%20%5C%5C%0Aa_5%5Ctimes%20a_7%3Da_6%20%5Cimplies%20%26a_7%3D%5Cfrac%7Ba_0%281%20-%20a_1%29/a_1%7D%7B1%20-%20a_1%7D%20%3D%20a_0%20/%20a_1%20%5C%5C%0Aa_6%2Ba_8%3Da_7%20%5Cimplies%20%26a_8%3D%20%28a_0%20/%20a_1%29%20-%20%5Cleft%5Ba_0%20%281%20-%20a_1%29/a_1%5Cright%5D%20%3D%20a_0%20%5C%5C%0Aa_7%5Ctimes%20a_9%3Da_8%20%5Cimplies%20%26a_9%3D%5Cfrac%7Ba_0%7D%7Ba_0%20/%20a_1%7D%20%3D%20a_1%0A%5Cend%7Baligned%7D)

On constate donc que ![latex](https://render.githubusercontent.com/render/math?math=a_%7B0%7D%3Da_%7B8%7D&mode=inline) et ![latex](https://render.githubusercontent.com/render/math?math=a_%7B1%7D%3Da_%7B9%7D&mode=inline). Par conséquent il y a un cycle de longueur 8 et  ![latex](https://render.githubusercontent.com/render/math?math=a_%7Bi%7D%3Da_%7Bi%2B8%7D&mode=inline). Faisons la somme des ![latex](https://render.githubusercontent.com/render/math?math=a_0&mode=inline) à ![latex](https://render.githubusercontent.com/render/math?math=a_7&mode=inline) :

![latexml](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Baligned%7D%0AS%26%3Da_0%0A%2Ba_1%0A%2B%28a_1-a_0%29%0A%2B%281-a_0/a_1%29%0A%2B%5Cleft%5B%28a_1-a_0%29/a_1-%28a_1-a_0%29%5Cright%5D%0A%2B%281-a_1%29%0A%2B%28a_0%20%281-a_1%29/a_1%29%0A%2B%28a_0/a_1%29%20%5C%5C%0A%26%3D3%0A%5Cend%7Baligned%7D)

Ainsi, tous les huit nombres, la somme est 3. Comme 1000 est un multiple de 8 et 1000 / 8 = 125, la somme totale est 3 × 125 = 375.

(🙏 Merci à [WolframAlpha](https://www.wolframalpha.com) pour les calculs symboliques et à [Visual Studio Code](https://code.visualstudio.com) et son ⌘2 afin d'écrire l'expression en [![latex](https://render.githubusercontent.com/render/math?math=%5CLaTeX&mode=inline)](https://www.latex-project.org)).

> réponse: 0 ou 375

## Mardi 21 Septembre

La hauteur issue de D de ADB vaut h = 24 / AB × 2

La hauteur issue de C de ACB vaut h = 16 / AB × 2

Comme M est le milieu de DC, la hauteur issue de M de AMB vaut la moyenne des deux hauteurs précédentes, à avoir: 20 / AB × 2

L'aire de AMB est donc:  20 / AB × 2 × AB / 2 = 20 cm²

> réponse: 20 cm²

## Mercredi 22 Septembre

ab = c²

a = 2b - c

D'où: (2b - c) b = c²

2b² - cb - c² = 0 ⇔ (b - c) (2b + c) = 0

Comme a < b < c, b = c n'est pas possible et c = -2b.

En remplaçant c par -2b: a = 4b

Ce qui entraine nécessairement a < b < 0 (si 0 < a < b, a=4b n'est pas possible) et c > 0.

La solution qui minimise c est donc: a = -4 b = -1 c = 2

> réponse: 2

## Jeudi 23 Septembre

n = 11111 en base b vaut b⁴ + b³ + b² + b¹ + b⁰ = (b⁵ - 1) / (b - 1)

- Pour b = 2, n = 31 ❌
- Pour b = 3, n = 121 = 11² ✅

> réponse: base 3

## Vendredi 24 Septembre

![tracé](24.gif)

Les choix 1 et 3 ne sont pas possibles parce qu'il faut un nombre impair d'arêtes au point B (passages puis arrivée).

[programme](24.py) Python qui trace le chemin.

```python
#!/usr/bin/env python3

import turtle


turtle.speed(1)
turtle.penup()

turtle.goto(115, 0)
turtle.write("A", font=("Menlo", 20, "normal"))

turtle.goto(100, 0)
turtle.pendown()
turtle.goto(-100, 00)
turtle.goto(-80, 150)
turtle.goto(120, 120)
turtle.goto(100, 0)
turtle.goto(-80, 150)
turtle.goto(100, 200)
turtle.goto(120, 120)
turtle.penup()

turtle.goto(135, 120)
turtle.write("B", font=("Menlo", 20, "normal"))


turtle.mainloop()

# conversion de la capture pour la création du GIF animé:
# ffmpeg -i capture.mov -vf "fps=10,scale=-1:200:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 24.gif
```

> réponse: 2

## Lundi 27 Septembre

Le triangle ABD est isocèle en B puisque l'angle ∠ADB fait 180 - 80 - 50 = 50° = angle ∠DAB.

Donc AD = BD = CD. Par conséquence, BCD est aussi isocèle en D et x = 180 - 30 × 2 = 120°

> réponse: 120°

## Mardi 28 Septembre

S = 2021 a + 2020 × 2021 / 2 = 2021 × (a + 1010) = 43 × 47 × (a + 1010).

Il faut que a + 1010 = 2021, soit a = 1011. En-deça, il n'y aura pas 43 et 47 en facteur de a + 1010.

> réponse: a = 1011

## Mercredi 29 Septembre

1 / 9² = 0,0̅1̅2̅3̅4̅5̅6̅7̅9̅

> réponse: 37

## Jeudi 30 Septembre

Taille à atteindre: 8 pièces par pile. Il y a au moins 1 + 2 mouvements, puisque le mouvement de départ ne peut laisser 8 pièces et il faut au moins 2 mouvements pour équilibrer 3 colonnes (1 mouvement peut équilibrer 0, 1 ou 2 colonnes au max).

| étape             | pile ① | pile ② | pile ③ |
 ------------------ |---------|---------|---------|
| état initial      |      11 |       7 |       6 |
| 7 de ① vers ②    |       4 |      14 |       6 |
| 6 de ② vers ③    |       4 |       8 |      12 |
| 4 de ③ vers ①    |       8 |       8 |       8 |

> réponse: 3 mouvements
