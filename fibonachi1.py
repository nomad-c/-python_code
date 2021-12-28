# fibonacci 27.12.2021 Czarny
# Zmienne
# n1 i n2 - elementy ciągu - poprzedni i następny
n1, n2, iteracje = 0, 1, 1
print("Ciąg Fibbonaciego\n")
print("Ile elementów ciągu chcesz zobaczyć ?")
ile_elementow = int(input(":"))
if (ile_elementow <= 0) or (ile_elementow > 100):
    print("\nChyba cię rozum opuścił..")
else:
    while iteracje <= ile_elementow:
        print(n1)
        tmp = n1 + n2  # tmp zmienna tymczasowa
        n1 = n2
        n2 = tmp
        iteracje += 1
