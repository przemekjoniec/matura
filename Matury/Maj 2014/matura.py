plik = open('PARY_LICZB.TXT', 'r')
wiersze = plik.readlines()

#A
ilosc_wielokrotnosci = 0

for wiersz in wiersze:
    wiersz = wiersz.strip().split(' ')
    wiersz0 = int(wiersz[0])
    wiersz1 = int(wiersz[1])
    if wiersz0 % wiersz1 == 0 or wiersz1 % wiersz0 == 0:
        ilosc_wielokrotnosci += 1
print(ilosc_wielokrotnosci)

#B
import math

ilosc_liczb_wzglednie_pierwszych = 0
for wiersz in wiersze:
    wiersz = wiersz.strip().split(' ')
    wiersz0 = int(wiersz[0])
    wiersz1 = int(wiersz[1])

    if math.gcd(wiersz0, wiersz1) == 1:
        ilosc_liczb_wzglednie_pierwszych += 1

print(ilosc_liczb_wzglednie_pierwszych)

#C
ilosc = 0
for wiersz in wiersze:
    wiersz = wiersz.strip().split(' ')

    suma0 = sum(int(litery) for litery in wiersz[0])
    suma1 = sum(int(litery) for litery in wiersz[1])

    if suma0 == suma1:
        ilosc += 1

print(ilosc)

