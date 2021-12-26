#!/usr/bin/env python3

import itertools
from collections import defaultdict

premiers = set()
for i in range(2, 30):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        premiers.add(i)

pairs = list(range(2, 13, 2))
impairs = list(range(1, 13, 2))
reponse = defaultdict(set)
for pair in itertools.permutations(pairs):
    for impair in itertools.permutations(impairs):
        somme = [p + i for p, i in zip(pair, impair)]
        if len(set(somme)) == 6:
            for n in somme:
                if n not in premiers:
                    break
            else:
                liste = " ".join(map(str, sorted(somme)))
                paires = " ".join(sorted(map(lambda a: f"{a[0]}+{a[1]}", zip(impair, pair))))
                reponse[liste].add(paires)

print(reponse)
