#!/usr/bin/env python3

from itertools import product

r = 6 ** 12
nb = 0
for a, b in product(range(7), repeat=2):
    x = 2 ** a * 3 ** b
    for c, d in product(range(5), repeat=2):
        y = 2 ** c * 3 ** d
        if x ** 2 * y ** 3 == r:
            nb += 1
            print(f"{nb:2} x=2^{a}*3^{b}={x:5} y=2^{c}*3^{d}={y:5}")
print("réponse:", nb)
