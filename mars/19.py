#!/usr/bin/env python3

for sign in [-1, 1]:
    for exp in range(0, 7):
        y = sign * 2 ** exp + 4
        x = 4 * y ** 2 // (y - 4)
        print(f"x={x:4}, y={y:4} {x * y == 4 * (y ** 2 + x)}")
