#!/usr/bin/env python3

from itertools import permutations

nb = 0
for n in permutations(range(1, 13)):
    if n[0] != 1:
        # pas la peine de refaire toutes les permutations avec 1 à une autre place
        nb *= 12
        break
    for i in range(12):
        a, b, c = n[i], n[(i + 1) % 12], n[(i + 2) % 12]
        if (a + b + c) % 3 == 0:
            break
    else:
        print(" ".join(map(str, n)))
        nb += 1

print(nb)
