# zgadywanka v2. exception handling 29.12.2021 Czarny
import random

traf = 1  # zmienna w której liczę , za którym razem trafiasz - pierwszy raz
secret = random.randint(1, 100)  # losowana liczba od 1 do 100
print("Zgadywanka\nOdgadnij liczbę między 1 a 100 włącznie ")
zgad = 0  # zmienna w której trzymam wybór usera
while zgad != secret:  # dopuki nie zgadniesz
    try:
        # sprawdzam czy wpisał liczbę
        print("Próba numer " + str(traf))
        zgad = int(input("Podaj swój typ:"))
    except ValueError:
        # jak nie wpisał liczby lecimy do początku pętli
        traf += 1
        continue  # to wraca do początku pętli czyli do while
    if zgad > secret:
        print(str(zgad) + " to niestety za dużo ")
        traf += 1
    if zgad < secret:
        print(str(zgad) + " to niestety za mało")
        traf += 1
print("\nTADA!!!!\nZgadłeś za " + str(traf) + " razem")
