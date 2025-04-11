plik = open('przyklad.txt','r')
wiersze = plik.readlines()

#3.1

zrownowazone = 0
prawie_zrownowazone = 0
for wiersz in wiersze:
    wiersz = wiersz.strip('')
    ilosc_zer = 0
    ilosc_jedynek = 0
    for cyfra in wiersz:
        if cyfra == '0':
            ilosc_zer += 1
        if cyfra == '1':
            ilosc_jedynek += 1

    if ilosc_jedynek == ilosc_zer:
        zrownowazone += 1
    elif ilosc_jedynek-1 == ilosc_zer or ilosc_jedynek+1 == ilosc_zer:
        prawie_zrownowazone += 1

print(zrownowazone, prawie_zrownowazone)

#3.3

def z_binarki(liczba):
    x = 0
    pom = len(liczba)
    for i in range(len(liczba)):
        if liczba[i] == '1':
            x = x + 2 ** (pom-1)
        pom -= 1
    return x

def z_dziesietnego(liczba):
    s = ''
    while liczba > 0:
        if liczba % 2 == 1:
            s += '1'
        else:
            s += '0'
        liczba //= 2

    s = s[::-1]
    return s

max_roznica = 0
for i in range(len(wiersze)-1):
    x1 = z_binarki(wiersze[i].strip())
    x2 = z_binarki(wiersze[i+1].strip())
    roznica = abs(x1-x2)
    roznica = z_dziesietnego(roznica)
    if int(roznica) > max_roznica:
        max_roznica = int(roznica)

print(max_roznica)

#3.4

def cyfry(liczba):
    zbior = set()
    while liczba > 0:
        cyfra = liczba % 10
        zbior.add(cyfra)
        liczba //= 10
    return zbior

ilosc = 0
max_liczba = 0
wynik = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    dziesietna = z_binarki(wiersz)
    rozne = cyfry(dziesietna)
    czy = 0 not in rozne
    if czy == 1:
        ilosc += 1
    if sum(rozne)>max_liczba:
        max_liczba = sum(rozne)
        wyniki = dziesietna

print(ilosc)
print(wyniki)



