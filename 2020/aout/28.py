#!/usr/bin/env python3

from math import factorial

a0, a1 = 1, 1

for n in range(1, 2021):
    a = n * (a0 + a1)
    n += 1
    a1, a0 = a, a1
    if n <= 6 or n == 2020:
        s = str(a)
        if len(s) > 20:
            s = "[...]" + s[-20:]
        print(f"a({n}) = {s}", factorial(n) == a)
