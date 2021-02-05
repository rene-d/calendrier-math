#!/usr/bin/env python3

carres = list(n * n for n in range(5))
nb = 0
for n in range(10, 100):
    d, u = divmod(n, 10)
    if d + u in carres:
        print(n)
        nb += 1
print("réponse:", nb)
