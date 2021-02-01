#!/usr/bin/env python3

from fractions import Fraction


def A(x):
    x = 1 / x
    return x


def B(x):
    x = x   * 2
    return x


x = Fraction(2)
for _ in range(1010):
    x = A(x)
    x = B(x)
print(x)