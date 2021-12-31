#!/usr/bin/env python3

for a in range(1, 141):
    for b in range(1, 141):
        for c in range(1, 141):
            if a * b == 100 and b * c == 140:
                print(a, b, c)
