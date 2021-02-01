#!/usr/bin/env python3


def dessine(pile1, pile2):
    print(f"  {'▉'* pile1}{' '*(3-pile1)}      {'▉'* pile2}{' '*(3-pile2)}")
    print("------   ------")
    print("pile 1   pile 2")


def gagne(pile1, pile2):
    if pile1 == 0:
        return pile2, 2
    if pile2 == 0:
        return pile1, 1

    if pile1 == 3:
        return 3 - pile2, 1

    if pile2 == 3:
        return 3 - pile1, 2

    if pile1 == 2:
        return 1, 1

    if pile2 == 2:
        return 1, 2

    print("AI pwned :(")
    exit(2)


pile = [None, 3, 3]

tour = "joueur"
prompt = True

print("\033[H\033[2J")

while True:

    try:
        if prompt:
            print()
            dessine(pile[1], pile[2])
            print()
            prompt = False

        if tour == "joueur":
            s = input("joueur: nombre,pile ? ")
            if s[0] == "q" or s[0] == "a":
                print("abandon")
                break
            n, p = map(int, s.split(","))
            if p != 1 and p != 2:
                raise Warning(f"numéro de pile invalide ({p})")
            if n <= 0:
                raise Warning(f"vous devez enlever au moins 1 jeton")
            if pile[p] < n:
                raise Warning(f"pas assez de jeton dans la pile {p}")

        else:
            n, p = gagne(pile[1], pile[2])
            print(f"j'enlève {n} jeton{'' if n == 1 else 's'} de la pile {p}")

        pile[p] -= n

        if pile[1] == 0 and pile[2] == 0:
            print()
            dessine(pile[1], pile[2])
            print()
            print("il ne reste rien !")
            print()
            print(f"{tour} a gagné")
            break

        if tour == "ia":
            tour = "joueur"
        else:
            tour = "ia"

        prompt = True

    except KeyboardInterrupt:
        break

    except ValueError as e:
        pass

    except Warning as e:
        print(e)
        pass
