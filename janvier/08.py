#!/usr/bin/env python3

# 8 Janvier 2021
# triangle de côté 15 cm, 20 cm, 25 cm. calculez les hauteurs
# Nota: le triangle est rectangle, deux hauteurs ont pour longueur 15 et 20 cm


from math import sqrt


def hauteur(a, b, c):
    """ Calcule la hauteur d'un triangle à partir des longueurs de ses côtés. """
    # http://villemin.gerard.free.fr/GeomLAV/Triangle/Calcul/RelQuelh.htm
    h = sqrt(c ** 2 - ((a ** 2 - b ** 2 + c ** 2) / (2 * a)) ** 2)
    return h


print(hauteur(15, 20, 25))
print(hauteur(20, 25, 15))
print(hauteur(25, 15, 20))  # <== donne la troisème hauteur
