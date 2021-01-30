#!/usr/bin/env python3

import itertools

saisie = [71, 76, 80, 82, 91]

for nb in itertools.permutations(saisie):
    for i in range(2, len(nb) + 1):

        s = sum(nb[:i])
        if s % i != 0:
            break

        if i == len(nb):
            print(nb[:i], [sum(nb[:j]) / j for j in range(2, len(nb) + 1)])
