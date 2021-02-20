#!/usr/bin/env python3

for x in range(1, 20):
    for y in range(1, 20):
        for z in range(1, 20):
            if x * y * z + x * y + 2 * y * z + x * z + x + 2 * y + 2 * z == 28:
                print(x, y, z, "réponse:", x + y + z)
