#!/usr/bin/env python3

import itertools
from sympy.ntheory import sieve

primes = sieve._list

n = 0
for p in itertools.permutations([2, 4, 6, 8]):
    for a, b in zip([1, 3, 5, 7], p):
        if a + b not in primes:
            break
    else:
        print(p)
