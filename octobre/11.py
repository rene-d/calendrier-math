#!/usr/bin/env python3

import itertools

results = set()
for ops in itertools.product("0-+", repeat=4):
    result = 0
    for op, nb in zip(ops, [1, 3, 9, 27]):
        if op == "+":
            result += nb
        elif op == "-":
            result -= nb
    if result > 0:
        results.add(result)

print(len(results))