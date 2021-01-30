#!/usr/bin/env python3

uniq = set()
nb = 0
for n in range(1000, 10000):

    # n multiple de 9
    if n % 9 != 0:
        continue

    s = set(str(n))

    # pas le chiffre 0
    if "0" in s:
        continue

    # quatre chiffres différents
    if len(s) != 4:
        continue

    uniq.add("".join(sorted(s, reverse=True)))
    nb += 1

print(f"uniques ({len(uniq)}):", " ".join(sorted(uniq, reverse=True)))
print("réponse:", nb)
