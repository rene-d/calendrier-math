#!/usr/bin/env python3

# il y a 36 jets possibles, soit 36 nombres:
#   11 12 13 14 15 16 21 22 ... 65 66
# parmi ces nombres il y a 4 carrés: 16 25 36 64
# soit 4/36 ou 1/9
# en inversant les chiffres (6 3 sont les chiffres de 36), on doit multiplier par 2, soit 2/9

from fractions import Fraction

# les carrés de 4 à 64
squares = [n * n for n in range(2, 9)]

n = p = 0
for i in range(1, 7):
    for j in range(1, 7):
        n += 1
        if i * 10 + j in squares or i + 10 * j in squares:
            print("chiffres d'un carré:", i, j)
            p += 1

print("réponse:", Fraction(p, n))
