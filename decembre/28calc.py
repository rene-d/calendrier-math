#!/usr/bin/env python3

# recherche empirique
aiguille = list()
for t in range(0, 43200):
    h = t / 120
    m = (t / 10) % 360
    if abs(abs(h - m) - 90) < 0.05 or abs(abs(h - m) - 270) < 0.05:
        if len(aiguille) > 0 and (t - aiguille[-1][0]) < 2:
            del aiguille[-1]
        hh, mm = int(h / 30), int(m / 6)
        aiguille.append((t, f"{hh:02d}:{mm:02d}:{t%60:02d}  {h:6.2f} {m:6.2f}"))

# calcul exact
exact = list()
for i in range(22):
    h = (90 + 180 * i) / 11
    m = (12 * h) % 360
    hh, mm, ss = int(h / 30), int(m / 6), int(120 * h) % 60
    fmt = f"{hh:02d}:{mm:02d}:{ss:02d}  {h:6.2f} {m:6.2f}"
    exact.append(fmt)

# affichage
for i, ((_, v), w) in enumerate(zip(aiguille, exact)):
    print(f"{i+1:2}   {v}   {w}")
