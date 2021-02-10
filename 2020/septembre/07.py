#!/usr/bin/env python3

import itertools

nb = 0
for a, b, c in itertools.combinations(range(1, 14), r=3):
    if (a + b + c) % 3 == 0:
        print(a, b, c)
        nb += 1
print("réponse:", nb)
