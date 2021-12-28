# papier, kamień nożyczki 27.12.2021 Czarny
import random

win, lose, remis, wybor, wybkom = 0, 0, 0, None, None
# wybor - wybór człowieka
# wybkom - wybór komputera
while wybor != "q":  # jak wybierzesz "q" to wyjdziemy z pętli
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

    if wybor != "q":  # bo jak równy q to po co..
        tmp = random.randint(0, 2)  # Losowanie wartości od 0 do 2 (0,1,2)
        # tak naprawdę są trzy przypadki
        # jakbym rozkładał każdy z każdym tak jak w książce
        # komputer miałby co najmniej 3 razy więcej roboty
        if tmp == 0:
            wybkom = "p"  # przekładam to na literkę, żeby mi się nie pozajączkowało
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

        if tmp == 1:
            wybkom = "k"
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
        if tmp == 2:
            wybkom = "n"
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
