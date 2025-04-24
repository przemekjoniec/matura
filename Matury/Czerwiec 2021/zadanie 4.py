plik = open('napisy.txt','r')
wiersze = plik.readlines()

#4.1
ile_cyfr = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    for znak in wiersz:
        if znak <= '9' and znak >= '0':
            ile_cyfr += 1

# print(ile_cyfr)

#4.2
j = 0
napis = ''
for i in range(19,len(wiersze),20):
    wiersz = wiersze[i].strip()
    napis += wiersz[j]
    j += 1

# print(napis)

#4.3
napis = ''

for wiersz in wiersze:
    wiersz = wiersz.strip()
    p = wiersz[0]
    o = wiersz[len(wiersz)-1]

    od_tylu = wiersz + p
    od_przodu = o + wiersz

    if od_tylu == od_tylu[::-1]:
        napis += od_tylu[(len(od_tylu)-1)//2]
    if od_przodu == od_przodu[::-1]:
        napis += od_przodu[(len(od_przodu)-1)//2]

print(napis)
