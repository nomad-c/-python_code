# papier, kamień nożyczki z tablicą i funkcją 29.12.2021 Czarny
import random

win, lose, remis, wybor, wybkom = 0, 0, 0, "p", None
# wybor - wybór człowieka
# wybór jest równe 'p' żeby od czegoś zacząć
# ale to nie ma znaczenia bo potem i tak mu ustawiam
# wybkom - wybór komputera
gra = ["p", "k", "n"]

while wybor in gra:  # jak wybierzesz coś innego niż poprawnie to wyjdziemy z pętli
    print("Papier, Kamień, Nożyczki")
    print("Wygrałeś " + str(win) + " przegrałeś " + str(lose) + " remis " + str(remis))
    wybor = input("Wybierz p,k,n albo q czy coś innego, żeby opuścić grę\n:")
    if wybor == "p":
        print("Wybrałeś PAPIER")
    if wybor == "k":
        print("Wybrałeś KAMIEŃ")
    if wybor == "n":
        print("Wybrałeś NOŻYCZKI")
    if (wybor != "p") and (wybor != "k") and (wybor != "n"):
        print("koniec")
        wybor = "q"
        break
    wybkom = random.randint(gra)  # Losowanie wartości od 0 do 2 (0,1,2)
    # tak naprawdę są trzy przypadki
    # jakbym rozkładał każdy z każdym tak jak w książce
    # komputer miałby co najmniej 3 razy więcej roboty
    if wybkom == "p":  # przekładam to na literkę, żeby mi się nie pozajączkowało
        print("Komputer wybrał PAPIER")
        if wybor == "n":
            win += 1
            print("Wygrałeś")
        elif wybor == "k":
            lose += 1
            print("Przegrałeś")
        else:
            remis += 1
            print("Remis")
    if wybkom == "k":
        print("Komputer wybrał KAMIEŃ")
        if wybor == "p":
            win += 1
            print("Wygrałeś")
        elif wybor == "n":
            lose += 1
            print("Przegrałeś")
        else:
            remis += 1
            print("Remis")
    if wybkom == "n":
        print("Komputer wybrał NOŻYCZKI")
        if wybor == "k":
            win += 1
            print("Wygrałeś")
        elif wybor == "p":
            lose += 1
            print("Przegrałeś")
        else:
            remis += 1
            print("Remis")
