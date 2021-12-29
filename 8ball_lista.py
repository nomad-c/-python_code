# 8 Ball 29.12.2021 Czarny
# chciałem potrenować funkcje
# a ta wersja jest z tablicą (jednowymiarową zwaną przez po angielsku listą)
import random

tmp = None
tresci = [
    "Z mojego punktu widzenia - Tak",
    "Zapytaj ponownie .. później..",
    "Lepiej będzie jak Ci teraz nie odpowiem",
    "Nie mogę teraz tego przewidzieć",
    "Skoncentruj się i zapytaj ponownie",
    "Nie licz na to...",
    "To pewne",
    "zdecydowanie TAK",
    "Najprawdopodobniej..",
    "Moja odpowiedź brzmi nie",
    "Według moich źródeł niestety nie",
    "Całkiem dobrze to wygląda",
    "Nie tak dobrze to wygląda jak by mogło",
    "Odpowiedź niknie we mgle - spróbuj ponownie zapytać",
    "Wszystkie znaki na niebie i ziemi wskazują na tak",
    "Bardzo wątpię",
    "No bez wątpienia",
    "Tak, definitywnie TAK",
    "Tak",
    "Możesz na tym polegać",
]

# Funkcja kula - wysyłam do niej wartość aaa
# aby nie zwracała czegoś szczególnego jak user
# wciśnie q, żeby opuścić zabawę
def kula(aaa):
    if aaa != "q":
        rnd = random.randint(0, 19)  # tablice są od ZERA
        # losuje liczbę od zera do 20-tu
        # w zależności od losowania daje wartość odpowiedzi
    else:
        return "Koniec"
    return tresci[rnd]


##################################################################
# Tu się dopiero zaczyna program
##################################################################

while tmp != "q":
    print("Magiczna 8 kula odpowiedź Ci pokaże..chyba, że q wybierzesz")
    tmp = input("Twoje pytanie to:")
    # wali mnie o co pytasz, a jak napiszesz q będzie koniec
    print("*************************************")
    print(kula(tmp))
    print("*************************************")
# Write your code here :-)
