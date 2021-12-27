#!/usr/bin/env python3


def pgcd(a, b):
    """Retourne le plus grand commun diviseur de deux entiers donnés (algorithme d'Euclide)."""
    while b != 0:
        a, b = b, a % b
    return a


def ppcm(nombres):
    """Retourne le plus petit commun multipe d'une liste de nombre."""
    p = nombres[0]
    for n in nombres[1:]:
        p = p * n // pgcd(p, n)
    return p


for a in range(1, 25):
    for b in range(a + 1, 25):
        if pgcd(a, b) == 4 and ppcm((a, b)) == 24:
            print(f"{a} + {b} = {a + b}")
