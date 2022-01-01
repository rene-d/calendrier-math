#!/usr/bin/env python3

from itertools import permutations

for a in set([((a + b + c + d), e) for a, b, c, d, e in permutations([3, 5, 9, 11, 25])]):
    print(a)
