#!/usr/bin/env python3

# Lundi 1 Février

from itertools import combinations
from math import prod

# les diviseurs de 1260
divisors = (2, 2, 3, 3, 5, 7)

m = 0
for r in range(len(divisors)):
    for d in combinations(divisors, r + 1):
        p = prod(d)
        if p < 100 and m < p:
            m = p

print("réponse:", m)