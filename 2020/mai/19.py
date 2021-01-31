#!/usr/bin/env python3

from fractions import Fraction
from math import gcd

n = 0
u = set()
for x in range(1, 11):
    for y in range(1, 11):

        # détermination: x et y premiers entre eux
        if gcd(x, y) == 1:
            n += 1

        # détermination: pente unique
        a = Fraction(y, x)
        u.add(a)

print("réponse:", n, len(u))
