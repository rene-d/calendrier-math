#!/usr/bin/env python3

# max(1/(1+i) + 1/(2021-i))

from fractions import Fraction

print(
    max(
        (Fraction(1, 1 + i) + Fraction(1, 2021 - i), f"1/{1+i} + 1/{2021-i}")
        for i in range(0, 1011)
    )[1]
)
