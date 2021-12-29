# papier, kamień nożyczki z tablicą i funkcją 29.12.2021 Czarny
# nowości to random.choice(listy)
# wykorzystanie zmiennej gra do możliwych wyników
# do trzech razy sztuka z wykorzystaniem for i range

import random

wybor, wybkom = None, None
# wybor - wybór człowieka
# wybkom - wybór komputera
# inicjalizuje mimo, że nie muszę ale chodzi o opisanie
status = [0, 0, 0]  # tu ukryłem wygrane, przegrane i remisy
gra = ["p", "k", "n"]


def podsumowanie():  # zrobiłem taką funkcję bo to dwa razy robię
    print(
        "Wygrałeś "
        + str(status[0])
        + " przegrałeś "
        + str(status[1])
        + " remis "
        + str(status[2])
    )  # podsumowanie
    if status[0] > status[1]:
        print("Tak generalnie to wygrałeś")
        print("Gratulacje !!!")
    elif status[0] < status[1]:
        print("Tak generalnie to przegrałeś")
        print("Dupa")
    else:
        print("No remis jest")


###############################################################
# koniec funkcji podsumowanie
####################################################


def calagra(iteracje):
    for i in range(iteracje):  # do iteracji razy sztuka
        print(
            "Wygrałeś "
            + str(status[0])
            + " przegrałeś "
            + str(status[1])
            + " remis "
            + str(status[2])
        )
        wybor = input("Wybierz p,k,n albo cokolwiek innego, żeby opuścić grę\n:")
        if wybor == "p":
            print("Ty wybrałeś PAPIER", end=" ")
        # end=' ' żeby nie przeskakiwał do następnej linii
        if wybor == "k":
            print("Ty wybrałeś KAMIEŃ", end=" ")
        if wybor == "n":
            print("Ty wybrałeś NOŻYCZKI", end=" ")
        if (wybor != "p") and (wybor != "k") and (wybor != "n"):
            print("Trzeba było coś wybrać")
            print("Przegrałeś walkowerem")
            status[1] += 1
            continue
        wybkom = random.choice(gra)  # Losowanie wartości ze zbioru gra
        # tak naprawdę są trzy przypadki
        # jakbym rozkładał każdy z każdym tak jak w książce
        # komputer miałby co najmniej 3 razy więcej roboty
        if wybkom == "p":
            print("a komputer wybrał PAPIER")
            if wybor == "n":
                status[0] += 1
                print("Wygrałeś")
            elif wybor == "k":
                status[1] += 1
                print("Przegrałeś")
        if wybkom == "k":
            print("a komputer wybrał KAMIEŃ")
            if wybor == "p":
                status[0] += 1
                print("Wygrałeś")
            elif wybor == "n":
                status[1] += 1
                print("Przegrałeś")
        if wybkom == "n":
            print("a komputer wybrał NOŻYCZKI")
            if wybor == "k":
                status[0] += 1
                print("Wygrałeś")
            elif wybor == "p":
                status[1] += 1
                print("Przegrałeś")
        if wybkom == wybor:
            status[2] += 1
            print("Remis")  # bo remis jest wszędzie taki sam
            # i nie trzeba tego trzy razy sprawdzać
            # ale warunek musi być na końcu bo inaczej komunikaty są w złej kolejności


###############################################################
# koniec funkcji calagra
####################################################

# tu się zaczyna program
pytanko = "cokolwiek"
# zmienna po to, żeby się zapytać czy gra dalej
# nie mogłem wykorzystać ponownie wybor
# bo wartość n oznacza nożyczki

while pytanko != "n":
    print("Do trzech razy sztuka")
    print("Papier, Kamień, Nożyczki")
    calagra(3)
    podsumowanie()
    pytanko = input("Grasz ponownie ?(t/n):")
podsumowanie()
# koniec
