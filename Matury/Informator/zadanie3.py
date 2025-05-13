plik = open('dane3.txt','r')
wiersze = plik.readlines()

dlugosci = {}
for wiersz in wiersze:
    wiersz = wiersz.strip().split()
    wiersz0 = int(wiersz[0])
    wiersz1 = int(wiersz[1])
    dlugosc = wiersz1 - wiersz0 + 1
    if dlugosc not in dlugosci:
        dlugosci[dlugosc] = 0
    else:
        dlugosci[dlugosc] += 1

print(max(dlugosci, key=dlugosci.get))


