#!/usr/bin/env python3

import math


def divisors(n):
    divs = [1, n]
    for i in range(2, int(math.sqrt(n)) + 1):
        q, r = divmod(n, i)
        if r == 0:
            divs.extend([i, q])
    return list(sorted(set(divs)))


for n in range(1, 101):
    if n == len(divisors(n)) ** 2:
        print(n)
