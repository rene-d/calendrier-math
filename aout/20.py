#!/usr/bin/env python3

import itertools

n = 0

# rooms[i] = numéro de chambre de l'ami n° i
for rooms in itertools.product(range(5), repeat=5):
    # nb[i] = nombre d'amis dans la chambre i
    nb = [0] * 5
    for room in rooms:
        if nb[room] == 2:
            break
        nb[room] += 1
    else:
        n += 1

print("réponse:", n)
