#!/usr/bin/env python3

# 9 Avril

n = 0
for a in range(740, 2022, 5):
    if a % 400 == 0:
        n += 1
    elif a % 100 == 0:
        pass
    elif a % 4 == 0:
        n += 1

print("réponse:", n)
