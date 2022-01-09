#!/usr/bin/env python3

carres = [n * n for n in range(6)]


def cherche(nb, trouves):

    if len(nb) == 0:
        print(trouves)
    else:
        if len(trouves) > 0:
            precedent = trouves[-1]
        else:
            precedent = 0
        for i, a in enumerate(nb):
            if precedent + a not in carres:
                continue
            cherche(nb[0:i] + nb[i + 1 :], trouves + [a])


cherche([n for n in range(1, 17)], [])
