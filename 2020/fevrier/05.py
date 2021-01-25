#!/usr/bin/env python3


def rev(n):
    """ Retourne le nombre n écrit à l'envers dans sa représentaiton décimale. """
    u = 0
    while n != 0:
        n, r = divmod(n, 10)
        u = u * 10 + r
    return u


print("réponse:", sum(1 for n in range(100, 1000) if rev(n) > n))
