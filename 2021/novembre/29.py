#!/usr/bin/env python3

from sympy.ntheory import factorint

nb = 0
for i in range(1000, 10000):
    p = 1
    n = i
    for _ in range(4):
        n, r = divmod(n, 10)
        p *= r

    nf = 1
    for k in factorint(p).values():
        nf *= k + 1
    if nf != 3:
        continue

    # print(i)
    nb += 1

print("réponse:", nb)
