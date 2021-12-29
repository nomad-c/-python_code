# Czarny 29.12.2021 testowanie inputu
# chodzi o to, żeby po wpisaniu tekstu nie wywalił błędu i nie przerwał programu

calkowita = 0
while calkowita != 69:
    try:
        calkowita = int(input("(69 kończy) Wpisz liczbę :"))
        print(calkowita)
    except ValueError:
        print("Wpisałeś tekst a nie liczbę")
