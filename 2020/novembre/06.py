#!/usr/bin/env python3

for a in (83, 89):
    for b in (61, 67):
        for c in (41, 43, 47):
            s = f"{a}{b}{c}"
            if len(s) > len(set(s)):
                continue
            reste = set("123456789").difference(set(s))
            somme = a + b + c + sum(map(int, reste))
            print(a, b, c, " ".join(reste), somme)
