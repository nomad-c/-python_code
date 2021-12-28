# 8 Ball 28.12.2021 Czarny
# chciałem potrenować funkcję
import random

tmp = None


def kula(aaa):
    if aaa != "q":
        rnd = random.randint(1, 20)
        # losuje liczbę od zera do 20-tu
        # w zależności od losowania daje wartość odpowiedzi
    else:
        rnd = 404
        # bo właściwie dlaczego nie
        return " "
        # bo ma nie pokazać odpowiedzi
    if rnd == 1:
        return "Z mojego punktu widzenia - Tak"
    if rnd == 2:
        return "Zapytaj ponownie .. później.."
    if rnd == 3:
        return "Lepiej będzie jak Ci teraz nie odpowiem"
    if rnd == 4:
        return "Nie mogę teraz tego przewidzieć"
    if rnd == 5:
        return "Skoncentruj się i zapytaj ponownie"
    if rnd == 6:
        return "Nie licz na to..."
    if rnd == 7:
        return "To pewne"
    if rnd == 8:
        return "zdecydowanie TAK"
    if rnd == 9:
        return "Najprawdopodobniej.."
    if rnd == 10:
        return "Moja odpowiedź brzmi nie"
    if rnd == 11:
        return "Według moich źródeł niestety nie"
    if rnd == 12:
        return "Całkiem dobrze to wygląda"
    if rnd == 13:
        return "Nie tak dobrze to wygląda jak by mogło"
    if rnd == 14:
        return "Odpowiedź niknie we mgle - spróbuj ponownie zapytać"
    if rnd == 15:
        return "Wszystkie znaki na niebie i ziemi wskazują na tak"
    if rnd == 16:
        return "Bardzo wątpię"
    if rnd == 17:
        return "No bez wątpienia"
    if rnd == 18:
        return "Tak, definitywnie TAK"
    if rnd == 19:
        return "Tak"
    if rnd == 20:
        return "Możesz na tym polegać"


while tmp != "q":
    print("Magiczna 8 kula odpowiedź Ci pokaże..chyba, że q wybierzesz")
    tmp = input("Twoje pytanie to:")
    # wali mnie o co pytasz, a jak napiszesz q będzie spacja
    print(kula(tmp))
