#!/usr/bin/env python3

nb = 0
for n in range(10, 91):
    d, u = divmod(n, 10)
    if d * u + d + u == n:
        print(n)
        nb += 1
print("réponse:", nb)
