#!/usr/bin/env python3

from sympy.ntheory import sieve

sieve.extend(23)
primes = sieve._list

cubes = [n ** 3 for n in sieve._list]

for n in range(55, 121):
    if (n - 55) * (n + 55) in cubes:
        print("réponse:", n)
        break