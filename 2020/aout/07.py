#!/usr/bin/env python3

nb = 0
for a in range(80, 100):
    for b in range(a, 100):
        n1 = a + (b // 10) + (b % 10)
        n2 = b + (a // 10) + (a % 10)
        if n1 == n2 == 100:
            print(a, b)
            nb += 1
print("réponse:", nb)
