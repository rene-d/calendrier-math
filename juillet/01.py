#!/usr/bin/env python3

# 1er Juillet 2021

for i in range(11, 100):
    a, b = divmod(i, 10)
    if (a + b) * 5 == i - (a + b * 10):
        print(i)