#!/usr/bin/env python3

# 25 Juin

import itertools

solution = None
nb_ok = 0
nb_ko = 0

# pour toutes les permutations des nombres de 1 à 5 (i.e. dispositions sur le cercle)
for perm in itertools.permutations(range(1, 6)):

    # ensemble des nombres qu'on peut obtenir
    m = set()

    # commence par chacun des nombres
    for start in range(5):
        # fait la somme de 1 à 5 nombres consécutifs
        for count in range(1, 6):
            # le modulo permet de boucler sur le cercle
            s = sum(perm[i % 5] for i in range(start, start + count))

            # ajoute dans la somme dans la liste de vérification
            m.add(s)

    if len(m) == 15 and m == set(range(1, 16)):
        nb_ok += 1
        # print("ok", perm, m)
        if not solution:
            solution = perm
    else:
        nb_ko += 1
        # print("ko", nb, m)

print("ok/ko:", nb_ok, nb_ko)

print("réponse:", perm)

# il y a en fait 100 réponses ok sur les 5!=120 dispositions possibles
