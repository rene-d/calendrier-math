#!/usr/bin/env python3

# 1 Mars

import itertools

n = 0
for fruits in itertools.product("AP", repeat=6):
    for i in range(6 - 2):
        if fruits[i] == "A" and fruits[i + 1] == "P" and fruits[i + 2] == "A":
            break
    else:
        n += 1
        # print(" ".join(fruits))
print("réponse:", n)
