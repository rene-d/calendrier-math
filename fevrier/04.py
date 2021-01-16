#!/usr/bin/env python3

CONF = (
    "x1 + x10 + 13 + 2",
    "x1 + x2 + x3 + 2",
    "x8 + x9 + x10 + 13",
    "x1 + x4 + x6 + 13",
    "x5 + x7 + x10 + 2",
    "x6 + x8 + 8 + 15",
    "x7 + x9 + 8 + 1",
    "x3 + x5 + 10 + 1",
    # "x2 + x4 + 10 + 15",
)

X = [3, 4, 5, 6, 7, 9, 11, 12, 14, 16]


import numpy as np
import re


M = np.zeros((10, 10))
V = np.zeros((10))

for i, e in enumerate(CONF):
    for x in re.findall(r"x(\d+)", e):
        M[i, int(x) - 1] = 1
    v = 34
    for x in re.findall(r" (\d+)", e):
        v -= int(x)
    V[i] = v


M[9, 0] = 1  # pour fixer x1
M[8, 1] = 1  # pour fixer x2

for x1 in X:
    V[9] = x1

    for x2 in X:
        V[8] = x2

        if np.linalg.det(M) == 0:
            continue

        M_inv = np.linalg.inv(M)
        R = np.matmul(M_inv, V)
        if set(R) == set(X):
            print(R)
