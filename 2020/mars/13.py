#!/usr/bin/env python3

from itertools import permutations

primes = [11, 13, 17, 19, 23, 29, 31, 37, 41]

puiss2 = [2,4,8,16,32]

for line in permutations(primes):

    for i in range(len(line)-1):
        if abs(line[i+1]-line[i]) not in puiss2:
            break
    else:
        print(line)
