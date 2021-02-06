#!/usr/bin/env python3

a0 = 1
a1 = 1

for n in range(1, 2021):

    a = n * (a0 + a1)

    n += 1
    a1, a0 = a, a1

    if n <= 6 or n == 2020:
        print(f"a({n}) = {a}")
