#!/usr/bin/env python3

# 7 Juin

import itertools

n = set()
for a, b in itertools.product([1, 3, 5, 7, 9], repeat=2):
    n.add(a + b)

print("n:", n)
print("réponse:", len(n))
