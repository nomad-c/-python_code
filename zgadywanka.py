# zgadywanka 27.12.2021 Czarny
import random

traf = 0 #zmienna w której liczę , za którym razem trafiasz
secret = random.randint(1, 100) #losowana liczba od 1 do 100
print("Zgadywanka\nOdgadnij liczbę między 1 a 100 włącznie ")
zgad = 0  # zmienna w której trzymam wybór usera
while zgad != secret:   #dopuki nie zgadniesz
    zgad = int(input("Podaj swój typ:"))
    if zgad > secret:
        print("Niestety za dużo")
        traf += 1
    if zgad < secret:
        print("Niestety za mało")
        traf += 1
print("\nTADA!!!!\nZgadłeś za " + str(traf) + " razem")
