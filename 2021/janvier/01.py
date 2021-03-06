#!/usr/bin/env python3

from sympy.ntheory.primetest import isprime


def rev(n):
    """ Retourne le nombre n écrit à l'envers dans sa représentaiton décimale. """
    u = 0
    while n != 0:
        n, r = divmod(n, 10)
        u = u * 10 + r
    return u


pp = set()
for n in range(11, 101):
    if isprime(n) and isprime(rev(n)):
        pp.add(n)
print("premiers réversibles:", sorted(pp))
print("réponse:", len(pp))
