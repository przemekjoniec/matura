plik = open('cyfry.txt','r')
wiersze = plik.readlines()

#a
ilosc = 0
for wiersz in wiersze:
    if int(wiersz) % 2 == 0:
        ilosc += 1

print(ilosc)

#b

min_suma = 0
max_suma = 0

min_liczba = int(wiersze[0])
max_liczba = int(wiersze[0])

for wiersz in wiersze:
    wiersz = wiersz.strip()
    suma = sum(int(i) for i in wiersz)
    if suma > max_suma:
        max_suma = suma
        max_liczba = wiersz

    if suma < min_suma:
        min_suma = suma
        min_liczba = wiersz

print(max_liczba,min_liczba)

#c

cyfry_z_ciagiem_rosnacym = []

def czy_ciag_rosnacy(ciag):
    for i in range(len(ciag)-1):
        if ciag[i] >= ciag[i+1]:
            return False
    return True

for wiersz in wiersze:
    wiersz = wiersz.strip()
    if czy_ciag_rosnacy(wiersz):
        cyfry_z_ciagiem_rosnacym.append(wiersz)

print(cyfry_z_ciagiem_rosnacym)