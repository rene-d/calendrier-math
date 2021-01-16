#!/usr/bin/env python3

# les palindromes à 3 chiffres sont forcément du genre 'aba' avec a ∈ [1,9] et b quelconque.
# il y a donc 9 * 10 palindromes entre 100 et 1000


def rev(n):
    """ Retourne le nombre n écrit à l'envers dans sa représentaiton décimale. """
    u = 0
    while n != 0:
        n, r = divmod(n, 10)
        u = u * 10 + r
    return u


palindromes = [n for n in range(100, 1001) if rev(n) == n]

print("palindromes:", palindromes)
print("réponse:", len(palindromes))
