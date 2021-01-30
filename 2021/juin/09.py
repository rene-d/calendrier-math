#!/usr/bin/env python3

import itertools

e = range(1, 6)
n = set()
for s in itertools.product([-1, 1], repeat=5):
    r = sum(a * b for a, b in zip(e, s))
    # print(e, s, r)
    n.add(r)

# print("e:", e)
# print("n:", n)
print("réponse:", len(n))
