#!/usr/bin/env python3

# 5 Janvier 2021

import itertools

expr = "100 {} 45 {} 67 {} 62 == 50"

for signs in itertools.product("+-", repeat=3):
    e = expr.format(*signs)
    v = eval(e)
    if v == True:
        n = signs.count("-")
        p = signs.count("+")
        print(f"{e} p={p} n={n} p-n={p-n}")
