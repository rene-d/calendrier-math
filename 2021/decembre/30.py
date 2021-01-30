#!/usr/bin/env python3

from itertools import permutations

n = 0
for perm in permutations(range(1, 8)):
    prev = 0
    for i in perm:
        if i == 1 and prev == 0:
            prev = 1
        elif i == 2 and prev == 1:
            prev = 2
        elif i == 3 and prev == 2:
            n += 1
            break

print("réponse:", n)
