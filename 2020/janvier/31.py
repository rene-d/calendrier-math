#!/usr/bin/env python3

somme_pair = 0
somme_impair = 0
for n in range(0, 10000):
    pair = True
    impair = True
    i = n
    for _ in range(4):
        i, r = divmod(i, 10)
        pair = pair and ((r % 2) == 0)
        impair = impair and ((r % 2) == 1)
    if pair:
        somme_pair += n
    if impair:
        somme_impair += n

print(somme_pair, somme_impair)

print(somme_impair- somme_pair)
