#!/usr/bin/env python3

from fractions import Fraction

n = 2
tn = 1  # valeur de t2
while n < 2020:
    n += 2
    tn = Fraction(n - 3, n - 1) * tn
print(f"n={n:5} tn={tn}")
