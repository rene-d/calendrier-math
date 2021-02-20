#!/usr/bin/env python3

for n in range(100, 1000):
    r = (n % 10) * 100 + ((n // 10) % 10) * 10 + (n // 100)
    s = n + r
    if (s % 10) % 2 == 1 and ((s // 10) % 2 == 1) and ((s // 100) % 2 == 1):
        print(n)
        break
