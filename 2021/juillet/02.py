#!/usr/bin/env python3

n = 0
for i in range(11, 100):
    a, b = divmod(i, 10)
    if a != 0 and b != 0:
        if i % a == 0 and i % b == 0:
            print(i)
            n += 1

print("réponse:", n)
