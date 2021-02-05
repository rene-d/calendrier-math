#!/usr/bin/env python3

from datetime import datetime

annee = 2020
ref = datetime(2020, 8, 20).weekday()
while True:
    annee += 1
    d = datetime(annee, 8, 20)
    print(f"{d.year} : {d.strftime('%A')}")
    if d.weekday() == ref:
        break
