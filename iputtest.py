# Czarny 29.12.2021 testowanie inputu
# chodzi o to, żeby po wpisaniu tekstu nie wywalił błędu i nie przerwał programu

calkowita = 0  # żeby zrobić pętlę muszę zainicjować zmienną
while calkowita != 69:  # kiedyś tę pętlę muszę zakończyć (mogę)
    try:
        calkowita = int(input("(69 kończy) Wpisz liczbę :"))
        print(calkowita)
    except ValueError:  # wiem, że to valueerror bo wpisałem inny typ
        # i się wywaliło z valueError - to poprawiłem
        print("Wpisałeś tekst a nie liczbę")
