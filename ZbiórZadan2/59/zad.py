plik = open('liczby.txt','r')
wiersze = plik.readlines()

#59.2
# suma_palindromow = 0
# for wiersze in wiersze:
#     liczba = wiersze.strip()
#     liczba_odwrocona = liczba[::-1]
#     suma_liczb = int(liczba) + int(liczba_odwrocona)
#     suma_liczb = str(suma_liczb)
#     palindrom_z_sumy = suma_liczb[::-1]
#
#     if suma_liczb == palindrom_z_sumy:
#         suma_palindromow += 1
#
# print(suma_palindromow)

#59.3

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

print(znajdz_moc('678'))

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

print(moce)
print(min_1, max_1)
