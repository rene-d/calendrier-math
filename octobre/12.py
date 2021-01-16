#!/usr/bin/env python3

import itertools

for a00, a02, a10, a11, a21 in itertools.permutations([2, 5, 6, 8, 9]):
    if a00 + 1 + a02 == a10 + a11 + 7 == 4 + a21 + 3 == a00 + a10 + 4 == 1 + a11 + a21 == a02 + 7 + 3:
        break

print("réponse:")
print(f"{a00} 1 {a02}")
print(f"{a10} {a11} 7")
print(f"4 {a21} 3")