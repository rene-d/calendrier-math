#!/usr/bin/env python3

import itertools

r = list((0, 2, 4, 4, 6, 8, 9, 11, 13, 15))

for a in itertools.product(range(-15, 16), repeat=5):

    s = set()
    for b, c in itertools.combinations(a, 2):
        s.add(b + c)

    if (
        (0 in s)
        and (2 in s)
        and (4 in s)
        and (6 in s)
        and (8 in s)
        and (9 in s)
        and (11 in s)
        and (13 in s)
        and (15 in s)
    ):
        l = list()
        for b, c in itertools.combinations(a, 2):
            l.append(b + c)

        l = list(sorted(l))
        if l == r:
            print(list(sorted(a)), l)
