#!/usr/bin/env python3


def to_base(n: int, base: int) -> str:
    """ Convertit un nombre entier dans son écriture dans la base indiquée qui doit être ≤ 36. """

    if base > 36 or base < 2:
        raise ValueError("to_base() base must be >= 2 and <= 36")

    if n == 0:
        return "0"

    if n < 0:
        n = -n
        sign = "-"
    else:
        sign = ""

    digits = ""
    while n != 0:
        n, r = divmod(n, base)
        digits += "0123456789abcdefghijklmnopqrstuvwxyz"[r]

    return sign + digits[::-1]


for base in range(11, 37):
    if to_base(39, base) == "25" and to_base(3 * 4 * 9, base) == "66":
        print("réponsé:", base)
        break
