#!/usr/bin/env python3

from itertools import permutations

nb = 0
for a, b, c in permutations(range(1, 14), r=3):
    if a < b < c:  # ne tient pas compte de l'ordre
        if (a + b + c) % 3 == 0:  # divisble par 3
            nb += 1
print("réponse:", nb)
