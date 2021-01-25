#!/usr/bin/env python3

s = 0
for n in range(10, 100):
    d, u = divmod(n, 10)
    if n + (d + u) ** 2 == u * 10 + d:
        print(n)
        s += n

print("réponse:", s)
