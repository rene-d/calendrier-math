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

## Lundi 8 Février

Cf. [programme](08.py) en Python.

> réponse: 2002
