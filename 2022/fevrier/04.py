#!/usr/bin/env python3

from itertools import permutations

print(len(set(a for a in permutations("AABBCC") if "ABC" in "".join(a))))
