# Calendrier Mathématique Février 2021

## Lundi 1 Février

Cf. [programme](01.py) en Python.

> réponse: 90

## Mardi 2 Février

Mise en équation sous forme d'équations linéaires:
| filles | garçons | cheveux_clairs | cheveux_foncés | filles_cheveux_clairs | filles_cheveux_foncés | garçons_cheveux_clairs | garçons_cheveux_foncés | valeurs |
| ------ | ------- | -------------- | -------------- | --------------------- | --------------------- | ---------------------- | ---------------------- | ------- |
| filles=garçons | 1 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 40% foncés | 0,4 | 0,4 | 0 | -1 | 0 | 0 | 0 | 0 | 0 |
| 60% clairs | 0,6 | 0,6 | -1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 75% foncés=filles | 0 | 0 | 0 | -0,75 | 0 | 1 | 0 | 0 | 0 |
| Σ filles | -1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| Σ garçons | 0 | -1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| Σ foncés | 0 | 0 | 0 | -1 | 0 | 1 | 0 | 1 | 0 |
|  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 50 |

résolution avec numpy avec un [script](02.py) Python.

> réponse: 40%

## Mercredi 3 Février

- aire triangle = c × a / 2
- aire trapèze = c × (b + a / 2)

- rapport 4:1 →
  - 4 × a / 2 = (b + a / 2)
  - 2 a = b + a / 2
  - 3/2 a = b ou a = 2/3 b

> réponse: b/a = 3/2

## Jeudi 4 Février

Calcul avec [script](04.py) Python.

> réponse:
```
              [10]
     [14]  [ 6]  [12]  [ 2]
     [ 3]              [11]
[15]                        [ 1]
     [ 4]              [16]
     [13]  [ 7]  [ 9]  [ 5]
              [ 8]
```

## Vendredi 5 Février

| proposition | interprétation | équation |
| -- | -- | -- |
| Pierre a trois plus de soeurs que de frères      | 3 freres = soeurs |  3 (garçons - 1) = filles |
| Pauline a deux fois plus de soeurs que de frères | 2 freres = soeurs |  2 garçons = filles - 1   |

- 2 garçons + 1 = 3 ( garçons - 1)  ⇒ garçons = 4
- filles = 1 + 2 garçons ⇒ filles = 9

> réponse: 4 garçons, 9 filles

## Lundi 8 Février

Cf. [programme](08.py) en Python.

> réponse: 2002

## Mardi 9 Février

demi-cercle + 2 carrés
- l'angle Θ centre/sommet est 45° (figure symétrique), donc a = √2 / 2
- aire des 2 petits carrés: (√2 / 2)² × 2 = 1

demi-cercle + 1 carré
- il faut que sin Θ = 2 cos Θ
- aire 1 carré: sin Θ × 2 cos Θ = sin² Θ
- or sin² Θ  = 1 - cos² Θ = 4 cos² Θ. donc on a cos² Θ = 1 / 5
- aire grand carré: 1 - 1 / 5 = 4 / 5

> réponse: 4 / 5
