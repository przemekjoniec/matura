plik_1 = open('liczby1.txt', 'r')
plik_2 = open('liczby2.txt', 'r')

wiersze_1 = plik_1.readlines()
wiersze_2 = plik_2.readlines()

# Zadanie 62.1

max = int(wiersze_1[0].strip(), 8)
min = int(wiersze_1[0].strip(), 8)

for wiersz in wiersze_1:
    liczba_10 = int(wiersz.strip(), 8)
    if liczba_10 > max:
        max = liczba_10
    elif liczba_10 < min:
        min = liczba_10

print(f'Zad 62.1, Max: {oct(max).replace('0o','')}, Min: {oct(min).replace('0o','')}')

# Zadanie 62.2

max_ciag_dl = 1
max_start = int(wiersze_2[0].strip())
obecna_dlugosc = 0
obecna_start = int(wiersze_2[0].strip())
poprzednia_liczba = int(wiersze_2[0].strip())

for i in range(1, len(wiersze_2)):
    obecna_liczba = int(wiersze_2[i].strip())
    if obecna_liczba >= poprzednia_liczba:
        obecna_dlugosc += 1

    if obecna_dlugosc > max_ciag_dl:
        max_ciag_dl = obecna_dlugosc
        max_start = obecna_start

    if obecna_liczba < poprzednia_liczba:
        obecna_dlugosc = 1
        obecna_start = obecna_liczba

    poprzednia_liczba = obecna_liczba

print(f'\n max dl: {max_ciag_dl}, max start: {max_start}')

# Zadanie 62.3
ile_takich_samych_wartosc = 0
ile_wartosci_wiekszych_w_pierwszym_pliku = 0

for i in range(0, len(wiersze_1)):
    liczba_1 = int(wiersze_1[i].strip(), 8)
    liczba_2 = int(wiersze_2[i].strip())


    if liczba_1 == liczba_2:
        ile_takich_samych_wartosc += 1
    elif liczba_1 > liczba_2:
        ile_wartosci_wiekszych_w_pierwszym_pliku += 1

print(f'\n tyle samo: {ile_takich_samych_wartosc}, ile wiekszych: {ile_wartosci_wiekszych_w_pierwszym_pliku}')

# Zadanie 62.4

ile_6_w_10 = 0
ile_6_w_8 = 0

for wiersz in wiersze_2:
    liczba_10 = wiersz.strip()
    for elem in liczba_10:
        if elem == '6':
            ile_6_w_10 += 1
    liczba_8 = oct(int(liczba_10)).replace('0o','')
    for elem in liczba_8:
        if elem == '6':
            ile_6_w_8 += 1

print(f'\n w 10: {ile_6_w_10}, w 8: {ile_6_w_8}')