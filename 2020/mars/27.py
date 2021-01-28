#!/usr/bin/env python3

i = 10
while True:
    n = i ** 3
    if n >= 10000:
        break

    a = n // 1000
    b = (n // 100) % 10
    c = (n // 10) % 10
    d = n % 10

    if n == (a + b + c + d) ** 3:
        print(n)

    i += 1
