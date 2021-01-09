#!/usr/bin/env python3

from sympy.ntheory.primetest import isprime

n = 0
for i in range(2, 101):
    if not isprime(i) and (i % 3) != 0 and (i % 7) != 0:
        n += 1
print("réponse:", n)
