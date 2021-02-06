#!/usr/bin/env python3

from fractions import Fraction

des = [[0, 0, 4, 4, 4, 4], [3, 3, 3, 3, 3, 3], [2, 2, 2, 2, 6, 6], [1, 1, 1, 5, 5, 5]]

nb = 0
lea_gagne = 0

for de_jean in range(4):
    for tirage_jean in des[de_jean]:
        for de_lea in range(4):
            if de_lea != de_jean:
                for tirage_lea in des[de_lea]:
                    nb += 1
                    if tirage_lea > tirage_jean:
                        lea_gagne += 1

print(lea_gagne, nb, Fraction(lea_gagne, nb))
