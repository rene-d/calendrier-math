#!/usr/bin/env python3

# 11 Juin

# sans programme, il faut éliminer de la liste les carrés et leurs mutiples:
# 4 8 9 12 16 18 20
# il reste 13 nombres

import itertools

squares = set(n * n for n in range(1, 21))

n = 20
while n > 1:

    # toutes les permutations de n nombres entre 1 et 20
    for factors in itertools.combinations(range(1, 21), n):

        # est-ce qu'il y a deux nombres dont le produit forme un carré ? (ex: 1 et 9)
        for a, b in itertools.combinations(factors, 2):
            if a * b in squares:
                break
        else:
            print(f"{n} est ok", factors)
            break
    else:
        n -= 1
        continue
    break

print("réponse:", n)