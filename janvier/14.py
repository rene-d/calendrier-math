#!/usr/bin/env python3

# 14 Janvier 2021


for a in range(1, 20):
    for b in range(1, 20):
        # condition 1: le triangle doit exister
        if b < 2 * a:
            # condition 2: périmètre = 20
            if 2 * a + b == 20:
                print(f"triangle {a} {a} {b}")
