#!/usr/bin/env python3

# 23 Juin

import itertools
import re

k = 0
while True:
    k += 1

    # construit le facteur 88888...8 (k chiffres)
    nk = 0
    for _ in range(k):
        nk = nk * 10 + 8

    n = 8 * nk

    # calcule la somme des chiffres
    s = 0
    while n != 0:
        n, r = divmod(n, 10)
        s += r

    # n = re.sub(r"(1+)", lambda x: f"<1×{len(x[1])}>" if len(x[1]) > 10 else x[1], str(8 * nk))
    # print(k, n, s)

    if s == 1000:
        break

print("réponse:", k)