#!/usr/bin/env python3

from math import degrees, atan2


def angle(a, b, c):
    """ Calcule l'angle ABC non signé non orienté. """

    ang = degrees(atan2(c[1] - b[1], c[0] - b[0]) - atan2(a[1] - b[1], a[0] - b[0]))

    ang = round(abs(ang))
    if ang > 180:
        ang = 360 - ang

    return ang


# calcule les coordonnées des 9 points
points = []
for x in range(-1, 2):
    for y in range(-1, 2):
        points.append((x, y))

triangles = set()

for a in points:

    for b in points:
        if a == b:
            # deux points confondus: à ignorer
            continue

        for c in points:
            if a == c or b == c:
                # deux points confondus: à ignorer
                continue

            # calcule les 3 angles du triangles
            angles = angle(b, a, c), angle(c, b, a), angle(a, c, b)
            if min(angles) == 0 or max(angles) >= 90:
                continue

            # on a un triangle, dont tous les angles sont aigus
            # on mémorise l'identification unique du triangle
            triangles.add(str(sorted((a, b, c))))

print("réponse:", len(triangles))
