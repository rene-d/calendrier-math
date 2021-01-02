#!/usr/bin/env python3

# 25 Juin

import itertools

# pour toutes les permutations des nombres de 1 à 5 (i.e. dispositions sur le cercle)
for nb in itertools.permutations(range(1,6)):
    m = set()

    # commence par chacun des nombres
    for i in range(5):
        # fait la somme de 1 à 5 nombres consécutifs
        for k in range(5):
            s = sum(nb[(j + i) % 5] for j in range(k + 1))

            # ajoute dans la somme dans la liste de vérification
            m.add(s)

    if len(m)==15 and m == set(range(1, 16)):
        print("ok", nb, m)
        break
    else:
        print("ko", nb, m)

print("réponse:", nb)

# il y a en fait 100 réponses ok sur les 5!=120 dispositions possibles