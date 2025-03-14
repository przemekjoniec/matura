plik = open('liczby1.txt','r')
wiersze = plik.readlines()

#1

max = int(wiersze[0].strip(),8)
min = int(wiersze[0].strip(),8)

for wiersze in wiersze:
    wiersz = int(wiersze.strip())
    if wiersz > max:
        max = wiersz
    if wiersz < min:
        min = wiersz
print(max)
print(min)


#2
plik2 = open('liczby2.txt','r')
wiersze2 = plik2.readlines()

najdluzszy_ciag = []
dlugosc_ciagu = 0

liczby = []
for wiersz in wiersze2:
    wiersz = int(wiersz.strip())
    liczby.append(wiersz)

obecny_ciag = []
obecna_dlugosc = 0

for i in range(0,len(liczby)-1):
    if liczby[i] <= liczby[i+1]:
        obecny_ciag.append(liczby[i])
        obecna_dlugosc += 1
    else:
        if obecna_dlugosc > dlugosc_ciagu:
            dlugosc_ciagu = obecna_dlugosc
            najdluzszy_ciag = obecny_ciag.copy()
            najdluzszy_ciag.append(liczby[i])
        obecny_ciag = []
        obecna_dlugosc = 0

print(najdluzszy_ciag[0])
print(len(najdluzszy_ciag))

#3

plik = open('liczby1.txt','r')
wiersze8 = plik.readlines()
plik = open('liczby2.txt','r')
wiersze10 = plik.readlines()

ile_takich_samych = 0
ile_wiekszych = 0

for i in range(0,len(wiersze8)):
    w_8 = int(wiersze8[i].strip(),8)
    w_10 = int(wiersze10[i].strip())

    if w_8 == w_10:
        ile_takich_samych += 1
    elif w_8 > w_10:
        ile_wiekszych += 1


print(ile_takich_samych)
print(ile_wiekszych)