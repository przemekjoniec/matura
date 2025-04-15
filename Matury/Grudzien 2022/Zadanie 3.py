plik = open('liczby.txt','r')
wiersze = plik.readlines()

#3.2
def czy_liczba_pierwsza(x):
    if x == 2:
        return True
    if x % 2 == 0 or x <= 1:
        return False
    for i in range(3, int(x/2+1),2):
        if x % i == 0:
            return False
    return True

licznik = 0
for wiersz in wiersze:
    wiersz = int(wiersz.strip())
    liczba = wiersz - 1
    if czy_liczba_pierwsza(liczba):
        licznik += 1

print(licznik)

