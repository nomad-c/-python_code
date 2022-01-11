# konwerter tekstu / szyfrowacz 10.01.2022
# jeszcze trochę...

tabela = [
        ['trzy', '3'],
        ['tu', '2'],
        ['ka', 'K'],
        ['o', '0'],
        ['e', '3'],
        ['s', '5'],
        ['5', '$'],
        ['a', '4'],
        ['b', '!6'],
        ['i', '!'],
        ['sto', '100'],
        ['ku', 'Q'],
        ['h', '#'],
        ['t', '7'],
        [' ', '-'],
        ['g', '6'],
        ['c', '<'],
        ['w', 'VV']
        ]
wpis2 = ''
wpis = input('Wpisz swój tekst: ')
wpis = wpis.lower()
for i in range(len(wpis)):
    wpis = wpis.replace(tabela[i][0], tabela[i][1])
print(wpis)

