#!/usr/bin/env python3


etape = 1
compteur = 0
n = 0

while True:
    print(f"{etape:4d} :  {n:5d}   { -2+(etape)*(etape+2):6d} ; ",  end="")

    for _ in range(3 + etape):
        n += 1
        print(n, end=" ")

        compteur += 1
        if compteur == 500000:
            print(n)
            exit()

    print()

    n += etape
    etape += 1
