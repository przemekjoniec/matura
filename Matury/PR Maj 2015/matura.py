plik = open('liczby.txt','r')
wiersze = plik.readlines()

#1
ilosc_liczb_z_wieksza_iloscia_zer = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    ilosc_jedynek = 0
    ilosc_zer = 0

    for i in range (0, len(wiersz)):
        if int(wiersz[i]) == 0:
            ilosc_zer += 1
        if int(wiersz[i]) == 1:
            ilosc_jedynek += 1

    if ilosc_zer > ilosc_jedynek:
        ilosc_liczb_z_wieksza_iloscia_zer += 1

print(f'Ilośc liczb z wieksza iloscia zer: {ilosc_liczb_z_wieksza_iloscia_zer}')

#2

ilosc_liczb_pod_przez_2 = 0
ilosc_liczb_pod_przez_8 = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    liczba = int(wiersz,2)

    if liczba % 2 == 0:
        ilosc_liczb_pod_przez_2 += 1
    if liczba % 8 == 0:
        ilosc_liczb_pod_przez_8 += 1

print(f'Ilosc liczb pod przez 2: {ilosc_liczb_pod_przez_2}, przez 8: {ilosc_liczb_pod_przez_8}')

#3

nr_wiersz_z_najmniejsza_liczba = None
nr_wiersz_z_najwieksza_liczba = None
max_liczba = None
min_liczba = None

for indeks, wiersz in enumerate(wiersze):
    wiersz = wiersz.strip()
    liczba = int(wiersz,2)

    if max_liczba is None or liczba > max_liczba:
        max_liczba = liczba
        nr_wiersz_z_najwieksza_liczba = indeks + 1
    if min_liczba is None or liczba < min_liczba:
        min_liczba = liczba
        nr_wiersz_z_najmniejsza_liczba = indeks + 1


print(f'Wiersz z najmniejsza liczba: {nr_wiersz_z_najmniejsza_liczba}, z najwieksza: {nr_wiersz_z_najwieksza_liczba}')


