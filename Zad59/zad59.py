plik = open('liczby.txt','r')
wiersze = plik.readlines()

# ZADANIE 59.2.
ile_palindromów = 0
for wiersz in wiersze:
    liczba = wiersz.strip()
    odwrócona_liczba = liczba[::-1]

    liczba = int(liczba)
    odwrócona_liczba = int(odwrócona_liczba)

    suma = liczba + odwrócona_liczba
    suma = str(suma)
    suma_odwrócona = suma[::-1]

    if suma == suma_odwrócona:
        ile_palindromów += 1

print('\nZADANIE 59.2.')
print(ile_palindromów)


#ZADANIE 59.3

def znajdz_moc(liczba):
    moc = 0
    ile_cyfr = len(liczba)

    while ile_cyfr > 1:
        moc += 1
        iloczyn = 1
        for cyfra in liczba:
            iloczyn *= int(cyfra)
        liczba = str(iloczyn)
        ile_cyfr = len(liczba)
    return moc

moce = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
min_1 = int(wiersze[0])
max_1 = int(wiersze[0])

for wiersz in wiersze:
    liczba = wiersz.strip()
    moc = znajdz_moc(liczba)
    liczba = int(liczba)
    if moc == 1:
        if liczba < min_1:
            min_1 = liczba
        if liczba > max_1:
            max_1 = liczba
        moce[1] = moce[1] + 1

    elif moc >= 2 and moc <= 8:
        moce[moc] = moce[moc] + 1

print('\nZADANIE 59.3')
print(f'MIN: {min_1}\nMAX: {max_1}')
for i in range(1,9):
    print(f'{i}: {moce[i]}')

