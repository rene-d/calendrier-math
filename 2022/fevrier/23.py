#!/usr/bin/env python3

from itertools import permutations

n = 0
for a in permutations(range(1, 10)):
    p = 0
    for c in a:
        if c == 9 or c == 8:
            # on ignore 8 et 9
            continue
        if p > c:
            # si 1 2 3 4 5 6 7 ne sont pas rangés dans cet ordre, on ne compte pas la solution
            break
        p = c
    else:
        n += 1
print(n - 1)  # -1 pour éliminer 123456789
