plik = open('liczby.txt','r')
wiersze = plik.readlines()

#1

# def czy_3_czynniki(liczba):
#     ile_czynników = 0
#     czynnik = 3
#     if liczba % 2 == 0:
#         return False
#
#     while liczba > 1:
#         if liczba % czynnik == 0:
#             ile_czynników += 1
#         while liczba % czynnik == 0:
#             liczba //= czynnik
#         czynnik += 2
#
#         if ile_czynników > 3:
#             return False
#
#     if ile_czynników == 3:
#         return True
#     else:
#         return False
#
# ile_liczb_z_3_czynnikami = 0
# for wiersz in wiersze:
#     liczba = int(wiersz.strip())
#
#     if czy_3_czynniki(liczba):
#         ile_liczb_z_3_czynnikami += 1
#
# print(ile_liczb_z_3_czynnikami)

#2

ile_palindromów = 0
for wiersz in wiersze:
    liczba = wiersz.strip()
    liczba_odwrocona = liczba[::-1]
    liczba = int(liczba)
    liczba_odwrocona = int(liczba_odwrocona)

    suma = liczba_odwrocona + liczba
    suma = str(suma)
    suma_odwrócona = suma[::-1]
    if suma == suma_odwrócona:
        ile_palindromów += 1

print(ile_palindromów)

#3

def znajdz_moc(liczba):
    moc = 0
    ile_cyfr = len(str(liczba))
    while ile_cyfr > 1:
        moc += 1
        iloczyn = 1

        for cyfr in liczba:
            iloczyn *= int(cyfr)

        liczba = str(iloczyn)
        ile_cyfr = len(liczba)

    return moc

moce = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
min_1 = int(wiersze[0].strip())
max_1 = int(wiersze[0].strip())
for wiersz in wiersze:
    liczba = wiersz.strip()
    moce[znajdz_moc(liczba)] += 1
    moc = znajdz_moc(liczba)
    liczba = int(liczba)
    if moc == 1:
        if liczba < min_1:
            min_1 = liczba
        if liczba > max_1:
            max_1 = liczba

print(moce)
print(min_1, max_1)

