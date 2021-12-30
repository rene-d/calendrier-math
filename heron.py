#!/usr/bin/env python3

a = eval(input("a ? "))
b = eval(input("b ? "))
c = eval(input("c ? "))

p = (a + b + c) / 2
A = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(f"p={p} A={A}")
