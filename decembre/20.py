#!/usr/bin/env python3

n = 0
for a in range(1, 7):
    for b1 in range(1, 7):
        for b2 in range(1, 7):
            if a > b1 + b2:
                # print(a,b1,b2)
                n += 1

print("réponse:", n, "/ 216")
