plik = open('dane_ulamki.txt', 'r')
wiersze = plik.readlines()

#Zadanie 65.1

min = 0.5
min_licznik = 1
min_mianownik = 2

for wiersz in wiersze:
    liczby = wiersz.strip().split(' ')
    licznik = int(liczby[0])
    mianownik = int(liczby[1])
    wartosc_ulamka = licznik / mianownik

    if wartosc_ulamka <= min:
        if wartosc_ulamka == min and mianownik > min_mianownik:
            continue
        min = wartosc_ulamka
        min_licznik = licznik
        min_mianownik = mianownik

print(f'Zadanie 65.1, licznik: {min_licznik}, mianownik: {min_mianownik}')

#Zadanie 65.2
import math
ile_nieskracalnych = 0
for wiersz in wiersze:
    liczby = wiersz.strip().split(' ')
    licznik = int(liczby[0])
    mianownik = int(liczby[1])

    nwd = math.gcd(licznik, mianownik)
    if nwd == 1:
        ile_nieskracalnych += 1

print(f'tyle nieskracalnych: {ile_nieskracalnych}')

#Zadanie 65.3
suma = 0
for wiersz in wiersze:
    liczby = wiersz.strip().split(' ')
    licznik = int(liczby[0])
    mianownik = int(liczby[1])

    nwd = math.gcd(licznik, mianownik)

    if nwd == 1:
        suma += licznik
    else:
        licznik = licznik / nwd
        suma += licznik

print(f'Suma liczników: {int(suma)}')

#Zadanie 65.4
suma = 0
b = (2**2)*(3**2)*(5**2)*(7**2)*13
for wiersz in wiersze:
    liczby = wiersz.strip().split(' ')
    licznik = int(liczby[0])
    mianownik = int(liczby[1])

    suma += (licznik * b) / mianownik

print(f'suma wynosi: {int(suma)}')


