#Zadanie 4 Hasła

plik = open('hasla.txt','r')
wiersze = plik.readlines()

#a
parzyste = 0
nieparzyste = 0

for wiersz in wiersze:
    wiersz = wiersz.strip('\n')

    if len(wiersz) % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

print(f'Parzyste: {parzyste}, Nieparzyste: {nieparzyste}')

#b
palindromy = []

for wiersz in wiersze:
    wiersz = wiersz.strip('\n')

    wiersz_palindrom = wiersz[::-1]

    if wiersz == wiersz_palindrom:
        palindromy.append(wiersz)

print(palindromy)

#c
hasla = []

for wiersz in wiersze:
    wiersz = wiersz.strip('\n')
    for i in range(0, len(wiersz)-1):
        obecna = ord(wiersz[i])
        kolejna = ord(wiersz[i+1])

        if obecna + kolejna == 220:
            hasla.append(wiersz)
            break

print(hasla)
