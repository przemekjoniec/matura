plik = open('liczby.txt','r')
wiersze = plik.readlines()

#4.1
podzielne_przez_17 = []
for wiersz in wiersze:
    wiersz = wiersz.strip()
    odbicie = wiersz[::-1]
    if int(odbicie) % 17 == 0:
        podzielne_przez_17.append(odbicie)

print(podzielne_przez_17)

#4.2
max_liczba = int(wiersze[0].strip())
max_wb = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    odbicie = wiersz[::-1]
    roznica = int(wiersz) - int(odbicie)
    wb = abs(roznica)
    if wb > max_wb:
        max_wb = wb
        max_liczba = wiersz

print(max_liczba, max_wb)

#4.3
def czy_pierwsza(x):
    if x == 2:
        return True
    if x % 2 == 0 or x <=1:
        return False
    for i in range(3, int(x/2+1), 2):
        if x % i == 0:
            return False
    return True

pierwsze = []
for wiersz in wiersze:
    wiersz = wiersz.strip()
    odbicie = wiersz[::-1]
    if czy_pierwsza(int(odbicie)) and czy_pierwsza(int(wiersz)):
        pierwsze.append(wiersz)

print(pierwsze)

#4.4
unikalne = set()
liczby = {}
for wiersz in wiersze:
    wiersz = wiersz.strip()
    if wiersz in liczby:
        liczby[wiersz] += 1
    else:
        liczby[wiersz] = 1
    if wiersz not in unikalne:
        unikalne.add(wiersz)

ile2 = 0
ile3 = 0
print(len(unikalne))
for liczba, ile_razy in liczby.items():
    if ile_razy == 2:
        ile2 += 1
    if ile_razy == 3:
        ile3 += 1
print(ile2, ile3)
