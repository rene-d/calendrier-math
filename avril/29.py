#!/usr/bin/env python3

# 29 Avril

import itertools

r = max(
    a * (b + c) - b * (a + c) for a, b, c in itertools.permutations(range(1, 11), 3)
)

print("réponse:", r)
