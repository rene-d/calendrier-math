#!/usr/bin/env python3

import itertools

n = 0
for p in itertools.permutations("12345"):
    pp = "".join(p)  # recrée une chaine
    pp = pp + pp  # pour éliminer si le premier et le dernier sont consécutifs
    if "12" in pp or "23" in pp or "34" in pp or "45" in pp:
        continue
    if "21" in pp or "32" in pp or "43" in pp or "54" in pp:
        continue
    print("".join(p))
    n += 1
print("réponse:", n)
