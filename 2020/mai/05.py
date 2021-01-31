#!/usr/bin/env python3

import math


def divisors(n):
    divs = [1, n]
    for i in range(2, int(math.sqrt(n)) + 1):
        q, r = divmod(n, i)
        if r == 0:
            divs.extend([i, q])
    return list(sorted(set(divs)))


n = 2
while True:
    u = [0] * 10
    nu = 0
    for d in divisors(n):

        if u[d % 10] == 0:
            u[d % 10] = 1
            nu += 1

        if nu == 10:
            print(n, divisors(n))
            exit()

    n += 1
