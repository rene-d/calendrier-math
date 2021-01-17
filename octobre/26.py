#!/usr/bin/env python3

from itertools import product

m = max(
    (a * b * c + a * b + b * c + a * c, a, b, c)
    for a, b, c in product(range(13), repeat=3)
    if a + b + c == 12
)
print(m)
