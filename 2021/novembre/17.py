#!/usr/bin/env python3

a, b = 1, 1

unites = set()
while len(unites) < 10:
    # print(f"{a:5}+{b:5}={a+b:6}")
    b, a = a + b, b
    unites.add(b % 10)

print("réponse:", b % 10)
