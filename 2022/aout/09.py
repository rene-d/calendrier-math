#!/usr/bin/env python3

from itertools import combinations


solutions = set()
nb = 0

for a in combinations(range(16), 10):

    # la grille vide
    grille = [[False for _ in range(4)] for _ in range(4)]

    # les cases sélectionnées
    for i in a:
        grille[i // 4][i % 4] = True

    # diagonale \
    impair = False
    for i in range(4):
        impair = impair ^ grille[i][i]
    if impair:
        continue

    # diagonale /
    impair = False
    for i in range(4):
        impair = impair ^ grille[3 - i][i]
    if impair:
        continue

    # les lignes
    for y in range(4):
        impair = False
        for x in range(4):
            impair = impair ^ grille[y][x]
        if impair:
            break
    if impair:
        continue

    # les colonnes
    for x in range(4):
        impair = False
        for y in range(4):
            impair = impair ^ grille[y][x]
        if impair:
            break
    if impair:
        continue

    nb += 1

    # pour afficher toutes les solutions:
    # for y in range(4):
    #     print("".join(["●" if x else "·" for x in grille[y]]))
    # print()

    s = "".join("".join("1" if grille[x][y] else "0" for x in range(4)) for y in range(4))
    if s in solutions:
        continue
    s = "".join("".join("1" if grille[3 - x][y] else "0" for x in range(4)) for y in range(4))
    if s in solutions:
        continue
    s = "".join("".join("1" if grille[x][3 - y] else "0" for x in range(4)) for y in range(4))
    if s in solutions:
        continue
    s = "".join("".join("1" if grille[3 - x][3 - y] else "0" for x in range(4)) for y in range(4))
    if s in solutions:
        continue

    s = "".join("".join("1" if grille[y][x] else "0" for x in range(4)) for y in range(4))
    if s in solutions:
        continue
    s = "".join("".join("1" if grille[3 - y][x] else "0" for x in range(4)) for y in range(4))
    if s in solutions:
        continue
    s = "".join("".join("1" if grille[y][3 - x] else "0" for x in range(4)) for y in range(4))
    if s in solutions:
        continue
    s = "".join("".join("1" if grille[3 - y][3 - x] else "0" for x in range(4)) for y in range(4))
    if s in solutions:
        continue

    solutions.add(s)


print("solutions:", len(solutions), nb)

solutions = sorted(solutions)
for y in range(4):
    print(" | ".join("".join(["●" if x == "1" else "·" for x in grille[y * 4 : y * 4 + 4]]) for grille in solutions))
