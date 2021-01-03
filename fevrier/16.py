#!/usr/bin/env python3

from itertools import permutations

n = 0
for a, b, c, d in permutations("ABCD"):
    if a == "A" or b == "B" or c == "C" or d == "D":
        continue
    print(a, b, c, d)
    n += 1

print("réponse:", n)
