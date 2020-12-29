#!/usr/bin/env python3

# 22 Janvier 2021

# il y a 36 jets possibles, soit 36 nombres:
#   11 12 13 14 15 16 21 22 ... 65 66
# parmi ces nombres il y a 4 carrés: 16 25 36 64
# soit 4/36 ou 1/9

from datetime import datetime, timedelta

un_jour = timedelta(days=1)

visite = datetime(2020, 12, 31)

# vérifie que c'est bien un jeudi
assert visite.weekday() == 3  # 0=lundi 1=mardi 2=mercredi 3=jeudi etc.

# vérifie que les 6 visites suivantes n'ont pas lieu un jeudi
for i in range(1, 7, 13):
    assert (visite + timedelta(days=i)).weekday() != 3

# vérifie que la 7ème visite a lieu un jeudi
assert (visite + timedelta(days=7 * 13)).weekday() == 3

print("réponse:", 7 * 13)
