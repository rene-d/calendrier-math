#!/usr/bin/env python3

import itertools
import re

n = 0
while True:
    n += 1
    for k in range(2, 10):
        if n % k != k - 1:
            # le modulo k n'est pas ok
            break
    else:
        # tous les modulo sont ok
        break

print(n)
