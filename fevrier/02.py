#!/usr/bin/env python3

# 2 Février

import numpy as np

M = np.array(
    (
        [1, -1, 0, 0, 0, 0, 0, 0],
        [0.4, 0.4, 0, -1, 0, 0, 0, 0],
        [0.6, 0.6, -1, 0, 0, 0, 0, 0],
        [0, 0, 0, -0.75, 0, 1, 0, 0],
        [-1, 0, 0, 0, 1, 1, 0, 0],
        [0, -1, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, -1, 0, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0],
    )
)
M_inv = np.linalg.inv(M)
V = np.array((0, 0, 0, 0, 0, 0, 0, 100))
R = np.matmul(M_inv, V)
# print(R)
print("réponse:", R[6])
