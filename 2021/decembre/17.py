#!/usr/bin/env python3

for i in range(10, 100):

    if i % 4 == 0 and i % 5 != 0:
        a, b = divmod(i, 10)
        j = b * 10 + a
        if j % 4 != 0 and j % 5 == 0:
            print(i)
