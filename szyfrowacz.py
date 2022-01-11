# konwerter tekstu / szyfrowacz do tworzenia haseł 10.01.2022
# nowe rzeczy tabela list i docieranie do jej elementów
# replace

tabela = [
    ["trzy", "3"],
    ["tu", "2"],
    ["ka", "K"],
    ["ku", "Q"],
    ["0", "zero"],  # nie może być później
    ["sto", "100"],
    ["o", "0"],
    ["e", "3"],
    ["5", "$"],
    ["a", "@"],
    ["b", "!6"],
    ["i", "!"],
    ["s", "5"],
    ["h", "#"],
    ["t", "7"],
    [" ", "-"],
    ["g", "6"],
    ["c", "<"],
    ["w", "VV"],
]
wpis2 = ""
wpis = input("Wpisz swój tekst: ")
wpis = wpis.lower()
for i in range(18):  # 18 to długość tabeli
    wpis = wpis.replace(tabela[i][0], tabela[i][1])
print(wpis)
