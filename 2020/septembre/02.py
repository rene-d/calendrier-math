#!/usr/bin/env python3

from itertools import permutations

nb = 0
for a, b, c in permutations([0, 1, 2, 3, 5], 3):
    if a == 0:
        continue
    n = a * 100 + b * 10 + c
    if n % 6 == 0:
        print(n)
        nb += 1
print("réponse:", nb)
