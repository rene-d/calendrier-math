#!/usr/bin/env python3

from itertools import product

# x+d = 12 ⇒1 ≤ a,b,c,d ≤ 11
for a, b, c, d in product(range(1, 12), repeat=4):
    s = (a + d, b + d, c + d)
    if s == (7, 10, 12):
        # uniquement les solutions a < b < c
        print(a, b, c, d, "Σ=", a + b + c)
