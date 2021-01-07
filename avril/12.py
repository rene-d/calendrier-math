#!/usr/bin/env python3

def is_zero(f : float):
    return abs(f) < 1e-10

def xy(x, y):

    print(x, y, "->", is_zero(1 + y - x ** 2), is_zero(1 + x - y ** 2))


x = (1 + 5 ** 0.5) / 2
xy(x, x)

x = (1 - 5 ** 0.5) / 2
xy(x, x)

xy(-1, 0)
xy(0, -1)