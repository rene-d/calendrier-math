#!/usr/bin/env python3

# Lundi 8 Février

# il faut les nombres premiers jusqu'à environ 2010^(1/3), soit environ 13. au-delà c'est trop grand (11*13*17 = 2431)
primes = [2, 3, 5, 7, 11, 13]

# calcule le produit de 3 premiers consécutifs
prod3 = []
for a, b, c in zip(primes, primes[1:], primes[2:]):
    if a * b * c > 2010:
        break
    prod3.append(a * b * c)

year = 2009
while year > 0:
    for i in prod3:
        if year % i == 0:
            print("réponse:", year)
            break
    else:
        year -= 1
        continue
    break
