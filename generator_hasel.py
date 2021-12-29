# generator haseł 29.12.2021 Czarny
# split bez argumentu tworzy liste tych co były oddzielone spacjami
#
import random

# inicjalizacja tablic
cyfry1 = "1 2 3 4 5 6 7 8 9 0"
cyfry = cyfry1.split()
duze1 = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
duze = duze1.split()
znaki1 = "! @ # $ % ^ & * ( ) - + [ ]"
znaki = znaki1.split()
male1 = " a b c d e f g h i j k l m n o p q r s t u v w x y z"
male = male1.split()


def generuj(ile):
    haslo, haslo1, haslo2 = "", "", ""
    if ile < 8:
        ile = 8
    haslo1 = (
        haslo1
        + " "
        + random.choice(cyfry)
        + " "
        + random.choice(duze)
        + " "
        + random.choice(znaki)
        + " "
        + random.choice(male)
    )
    for i in range(ile):
        haslo2 = (
            haslo2
            + " "
            + random.choice(cyfry)
            + " "
            + random.choice(duze)
            + " "
            + random.choice(znaki)
            + " "
            + random.choice(male)
        )
    haslo3 = haslo2.split()  # mam wylosowany zbiór znaków z których zrobię haslo
    haslo4 = haslo1.split()
    for i in range(4):
        haslo = haslo + haslo4[i]
    for i in range(ile - 4):
        haslo = haslo + haslo3[i]
    return haslo


print("enerator hasel")
ile1 = int(input("Ile potrzebujesz znakow ?"))
print(generuj(ile1))
