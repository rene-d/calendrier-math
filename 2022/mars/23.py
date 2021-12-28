#!/usr/bin/env python3

from itertools import permutations

for a, b, c, d, e, f, g in permutations([1, 3, 4, 6, 7, 8, 9]):
    if 5 + a + b + 2 == 5 + c + d + e == e + f + g + 2:
        print(5, a, b, 2, "-", 5, c, d, e, "-", e, f, g, 2, "=", 5 + a + b + 2)
