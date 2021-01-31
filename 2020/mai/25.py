#!/usr/bin/env python3

from itertools import product

n = sum(1 for a, b, c in product(range(0, 10), repeat=3) if a + b + c == 10)

print("réponse:", n)
