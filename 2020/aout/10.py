#!/usr/bin/env python3

from fractions import Fraction

des = [
    [0, 0, 4, 4, 4, 4],
    [3, 3, 3, 3, 3, 3],
    [2, 2, 2, 2, 6, 6],
    [1, 1, 1, 5, 5, 5],
]

total_nb = 0
total_lea_gagne = 0
max_lea_f = 0

# Jean choisit un dé
for de_jean in range(4):

    des_lea = set(range(4))
    des_lea.remove(de_jean)

    # Léa choisit un dé parmi les trois restants
    for de_lea in des_lea:

        nb = 0
        lea_gagne = 0

        # Jean tire son dé
        for tirage_jean in des[de_jean]:

            # Léa tire son dé
            for tirage_lea in des[de_lea]:
                nb += 1

                # Léa gagne si son tirage est supérieur à celui de Jean
                if tirage_lea > tirage_jean:
                    lea_gagne += 1

        f = Fraction(lea_gagne, nb)
        # print(
        #     f"de_jean: {des[de_jean]} de_lea: {des[de_lea]} - "
        #     + f"lea_gagne: {lea_gagne}/{nb} = {f}"
        # )
        if f > max_lea_f:
            max_lea_f = f

        total_lea_gagne += lea_gagne
        total_nb += nb

f = Fraction(total_lea_gagne, total_nb)
print(f"total_lea_gagne: {total_lea_gagne}/{total_nb} = {f}")
print(f"max_lea_f: {max_lea_f}")
