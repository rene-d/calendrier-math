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

![latexml](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Balign%7D%0AM%20-%20N%20%26%3D%20%20%5Cfrac%20%7B%20%5Csum%20%7B%28a_i%20%2B%20a%7D%29%7D%20n%20-%20%5Cfrac%20%7B%20%5Csum%20%7B%20a_i%20%7D%7D%20%7Bn-1%7D%0A%5C%5C%0A%26%3D%20%5Cfrac%20%7B%20%5Csum%20%7B%28a_i%20%2B%20a%7D%29%7D%20n%20-%20%5Cfrac%20n%20%7Bn-1%7D%20%5Cleft%28%5Cfrac%20%7B%5Csum%20%7B%20a_i%20%7D%7D%20%20n%20%2B%20%5Cfrac%20a%20n%20-%20%5Cfrac%20a%20n%20%5Cright%29%0A%5C%5C%0A%26%3D%20M%20-%20%5Cfrac%20n%20%7Bn-1%7D%20%5Cleft%28M%20-%20%5Cfrac%20a%20n%20%5Cright%29%0A%5C%5C%0A%26%3D%20M%20%5Cleft%28%201%20-%20%5Cfrac%20n%20%7Bn-1%7D%20%5Cright%29%20%2B%20%5Cfrac%20%7Ba%7D%20%7Bn-1%7D%0A%5C%5C%0A%26%3D%20-%20%5Cfrac%20M%20%7Bn%20-%201%7D%20%2B%20%5Cfrac%20%7Ba%7D%20%7Bn-1%7D%0A%5C%5C%0A%26%3D%20%5Cfrac%20%7Ba-M%7D%20%7Bn%20-%201%7D%0A%5Cend%7Balign%7D)

> réponse: (a - M) / (n - 1)

## Vendredi 4 Février

Programme [Python](04.py)

C'est le nombre de permutations des éléments ABC A B C, dans lequel il ne faut compter qu'une fois le doublon constitué par "ABC A B C" et "A B C ABC".

> réponse: 23

## Lundi 7 Février

Si Adèle écrit 15, la seule solution est 1 + 2 + 3 + 4 + 5.

Si Adèle écrit 16, la seule solution est 1 + 2 + 3 + 4 + 6. En effet si on remplace un autre nombre par 6 qui est le premier nombre libre, la somme sera supérieure à 16.

Si Adèle écrit 17, on peut remplacer dans la somme initiale le 4 par 6 ou le 5 par 7.

Si Adèle écrit 18, on peut remplacer le 5 par 8 ou le 4 par 7.

Et ainsi de suite: on pourra toujours trouver au moins deux séries de nombres dont la somme vaut le nombre noté.

> réponse: 15 et 16

## Mardi 8 Février

On équilibre le contenu des boîtes en déplaçant la moitié de la différence (qui est paire, puisque p et q sont impairs): (p - q) / 2. En déplaçant un chocolat de plus, la boîte B en aura plus que la boîte A.

> réponse: (p - q) / 2 + 1

## Mercredi 9 Février

- A : "B est vraie"
- B : "E n'est pas vraie"
- C : "les affirmations de A à E sont vraies"
- D : "les affirmations de A à E sont fausses"
- E : "A n'est pas vraie"

C et D ne peuvent pas être vraies car elles se contredisent.

Si A est vraie et E fausse, alors B serait vraie. Ce qui est impossible.

Si A est vraie et E vrai, il y a contradiction.

Si B est vraie, E doit être fausse dans A serait vraie ce qui est impossible.

Il reste E qui est vraie. Et qui entraine B et C fausses.

> réponse: E

## Jeudi 10 Février

![10](./10.png)

Le triangle FDI est isocèle, dans l'angle ∠FDI = 180° - 2 x.

On a aussi ∠FDI + 90° + 90° + ∠EDF = 360°.

∠EDG = 2 𝜃 et ∠DPC = 180 - 2 𝜃. ∠DPC = 360 / 5 = 72°.

D'où:

- 𝜃 = (180 - ∠DPC) / 2 = 108 / 2 = 54°
- ∠FDI = 180 - 2 𝜃 = 180 - 108 = 72°
- x = (180 - 72) / 2 = 54°

> réponse: 54°

## Vendredi 11 Février

- u₀ = 1
- u₁ = 2
- u₂ = 3 = 1 + 2 = 3 × 2²⁻²
- u₄ = 6 = 3 × 2³⁻²
- uₙ = 3 × 2ⁿ⁻²
- u₁₉ = 3 × 2¹⁷ = 393216

Vérification du calcul en [Rust](./11.rs) :

```rust
fn main() {
    fn u_n(n: u64) -> u64 {
        match n {
            0 => 1,
            1 => 2,
            _ => (0..n).fold(0, |acc, i| acc + u_n(i)),
        }
    }
    println!("{}", u_n(19)); // = 3 × 2ⁿ⁻²
}
```

> réponse: 393216

## Lundi 14 Février

Les cubes laissés en blanc sont ceux non visibles. Les cubes jaunes sont:

- face avant: 12
- face supérieure: 10 (on ne compte pas ceux de la face avant)
- face droite: 8 (idem)

Il y a donc 30 cubes peints, et donc 34 cubes blancs.

> réponse: 34

## Mardi 15 Février

Le deuxième nombre multiple du premier entraine: ∃ k ∈ 𝐍 ⎸ (n + 1011) = k × n

Soit (k - 1) × n = 1011 = 1 × 3 × 337

Donc n peut valoir 1, 3, 337 ou 1011.

Vérification en [Rust](15.rs):

```rust
fn main() {
    (1..=1011)
        .filter(|i| (i + 1011) % i == 0)
        .for_each(|i| println!("{:4} * {:4} = {:4}", i, (i + 1011) / i, i + 1011))
}
```

```rust
fn main() {
    (1..=1011)
        .filter(|i| (i + 1011) % i == 0)
        .for_each(|i| println!("{:4} * {:4} = {:4}", i, (i + 1011) / i, i + 1011))
}
```

> réponse: 4

## Mercredi 16 Février

[Pythagore](https://fr.wikipedia.org/wiki/Théorème_de_Pythagore) ![latex](https://render.githubusercontent.com/render/math?math=a%5E2%2Bb%5E2%3Dc%5E2&mode=inline) :

![latexml](https://render.githubusercontent.com/render/math?math=%5Csqrt%20%7B%206%5E2-4%5E2%20%7D%20%3D%20%5Csqrt%20%7B20%7D%20%3D%202%20%5Csqrt%205%20%3D%204.472%20%5Ctext%7B%20m%7D)

> réponse: 2 √5 m

## Jeudi 17 Février

Soit 𝑥 le coût à l'achat d'une boîte de cacao et n le nombre de boîtes de café vendues.

La mise en équation de l'énoncé donne:

n × 140 + (n / 2) × (𝑥 × 1.2) = (n × 100 + (n / 2) × 𝑥) × 1.36

En simplifiant par n (non nul!) on obtient:

140 + 𝑥 × 0.6 = 136 + 0.68 × 𝑥

0.08 × 𝑥 = 4

𝑥 = 50

Le prix d'achat est donc 50€ et celui de vente 50 × 1.2 = 60€

> réponse: 60 €

## Vendredi 18 Février

Margaux peut échanger avec Juliette 2×2=4 parts de gâteau avec ses 2×5 parts de pizza. Elle peut donc récupérer 2×3 verres de jus de fruits.

> réponse: 6

## Lundi 21 Février

Les diviseurs positifs de 8 sont: 1 2 4 8. Ceux de 10 sont 1 2 5 10.

Il y a donc 4×4=16 sommes possibles. Parmi celles-là, seules ces huit sommes 1+10 2+10 4+10 8+10 4+5 8+5 8+2 8+1 sont strictement supérieures à 8.

> réponse: 1 / 2

## Mardi 22 Février

En appliquant la fonction logarithme puis en simplifiant les équations par ![latex](https://render.githubusercontent.com/render/math?math=%5Cln%202&mode=inline) (respectivement ![latex](https://render.githubusercontent.com/render/math?math=%5Cln%203&mode=inline)), on obtient:

![latexml](https://render.githubusercontent.com/render/math?math=x%20%5Cln%208%20-%20%28x%2By%29%20%5Cln%202%20%3D%20%5Cln%2064%20%5Cimplies%20x%2By%20%3D%20%5Cfrac%20%7Bx%20%5Cln%202%5E3%20-%20%5Cln%202%5E6%7D%20%7B%5Cln%202%7D%20%3D%20%7B3x-6%7D)

![latexml](https://render.githubusercontent.com/render/math?math=%28x%2By%29%20%5Cln%209%20-%204y%20%5Cln%203%20%3D%20%5Cln%20243%20%5Cimplies%20x%2By%20%3D%20%5Cfrac%20%7B%5Cln%203%5E5%20%2B%204y%20%5Cln%203%7D%20%7B%5Cln%203%5E2%7D%20%3D%20%5Cfrac%20%7B5%2B4y%7D%7B2%7D)

Soit:

![latexml](https://render.githubusercontent.com/render/math?math=2x-y%3D6%0A%5C%5C%0A2x-2y%3D5)

On résoud ce système linéaire de deux équations à deux inconnues:

![latexml](https://render.githubusercontent.com/render/math?math=-y-%28-2y%29%3D6-5%20%5Cimplies%20y%3D1%20%5Cimplies%20x%3D%5Cfrac%207%202)

D'où:

![latexml](https://render.githubusercontent.com/render/math?math=2xy%20%3D%207)

> réponse: 7

## Mercredi 23 Février

Il faut placer les chiffres 8 et 9 "entre" les chiffres 1 2 3 4 5 6 7.

Il y a 8 "cases vides" autour de chaque chiffre, donc ![latex](https://render.githubusercontent.com/render/math?math=A_%7Bn%7D%5E%7Bk%7D%20%3D%20A_%7B8%7D%5E%7B2%7D%20%3D%208%20%5Ctimes%207%20%3D%2056&mode=inline) possibilités (ou [arrangements](https://fr.wikipedia.org/wiki/Arrangement)) de placer les 8 et 9 entre les autres.

Dans ces 8 cases vides, on peut placer de deux manières différentes les chiffres 8 et 9: 89 ou 98. Ce qui fait 16 possibilités, moins la dernière  car 1 2 3 4 5 6 7 89 est interdit: il en reste 15.

Vérification en [Python](23.py).

```python
#!/usr/bin/env python3

from itertools import permutations

n = 0
for a in permutations(range(1, 10)):
    p = 0
    for c in a:
        if c == 9 or c == 8:
            # on ignore 8 et 9
            continue
        if p > c:
            # si 1 2 3 4 5 6 7 ne sont pas rangés dans cet ordre, on ne compte pas la solution
            break
        p = c
    else:
        n += 1
print(n - 1)  # -1 pour éliminer 123456789
```

> réponse: 71

## Jeudi 24 Février

75 × 0.8 = 60

> réponse: 60

## Vendredi 25 Février

Soit n le nombre de personnes avant et après Sandra. Le nombre total d'élèves est donc 2n+1.

- n + 1 ≤ 19 (Raoul après Sandra) : n ≤ 18
- 28 ≤ 2n+1 (rang de Thomas) : n ≥ 13.5
- il faut que le 2n+1 soit multiple de 3

```text
1 ...                            Th                         Ra
1 ... 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ...
                  ^^ ^^ ^^ ^^ ^^
                      Sandra
```

Seul n=16 (car 16×2+1 = 33 = 11×3) convient, les autres possibilités ne conduisent pas à un effectif total divisible par 3.

Le rang de Sandra est donc n+1 = 17.

> réponse: 17

## Lundi 28 Février

La base de chaque triangle équilatéral vaut exactement la somme des deux autres côtés. Ainsi la somme de tous les côtés autres que les bases vaut exactement le double de la somme des bases. Et ce, quelque soit le nombre de triangles équilatéraux.

> réponse: 40 cm
