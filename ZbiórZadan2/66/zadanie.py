plik = open('trojki.txt','r')
wiersze = plik.readlines()

#1
tablica1 = []

for wiersz in wiersze:
    wiersz = wiersz.strip().split(' ')
    liczby = [int(x) for x in wiersz]
    suma1 = 0
    suma2 = 0
    for cyfra in str(liczby[0]):
        suma1 += int(cyfra)
    for cyfra in str(liczby[1]):
        suma2 += int(cyfra)

    if suma1 + suma2 == liczby[2]:
        tablica1.append(liczby)

print(tablica1)

#2
tablica2 = []

import math

def czy_pierwsza(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for wiersz in wiersze:
    wiersz = wiersz.strip().split(' ')
    liczby = [int(x) for x in wiersz]

    if czy_pierwsza(liczby[0]) and czy_pierwsza(liczby[1]) and liczby[0]*liczby[1] == liczby[2]:
        tablica2.append(liczby)

print(tablica2)

#3
tablica3 = []
for wiersz in wiersze:
    wiersz = wiersz.strip().split(' ')
    liczby = [int(x) for x in wiersz]
    a = b = c = 0
    a, b, c = sorted(liczby)

    if (a**2) + (b**2) == c**2:
        tablica3.append(liczby)

print(tablica3)
#brak sprawdzania sasiadujacych wiersz, trzeba sprawdzic recznie, pozdro



