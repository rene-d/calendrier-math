#!/usr/bin/env python3

# résolution du système d'équations linéaires

import numpy as np

# import random

# la matrice du système à 4 équations
M = np.array([[1, 4, 9, 16], [4, 9, 16, 25], [9, 16, 25, 36], [1, 1, 1, 1]])
print(M)
print(np.linalg.det(M))

# la matrice du système à 3 équations
M = np.array([[1, 4, 9], [4, 9, 16], [9, 16, 25]])
print(M)

# son inverse
Minv = np.linalg.inv(M)
print(Minv)

# vecteur résultat
v = np.array([1, 8, 23])

# colonne des x4, aléatoire
x4 = 0  # random.uniform(-100, 100)
vx4 = np.array([16 * x4, 25 * x4, 36 * x4])

r = np.matmul(Minv, v - vx4)

print(r)
print(np.sum(r) + x4)
