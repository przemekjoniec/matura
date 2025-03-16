plik = open('ciagi.txt','r')
wiersze = plik.readlines()

ciagi_dwycykliczne= []

for wiersz in wiersze:
    wiersz = wiersz.strip()
    dlugosc_slowa = len(wiersz)
    if dlugosc_slowa % 2 == 0:
        w1 = wiersz[:dlugosc_slowa//2]
        w2 = wiersz[dlugosc_slowa//2:]
        # print(f' Wiersz: {wiersz}, jego połowki: {w1}, {w2}')
        if w1 == w2:
            ciagi_dwycykliczne.append(wiersz)

print(f'Ciagi dwucykliczne: {ciagi_dwycykliczne}')

#2

ile_ciagow_bez_1_obok_siebie = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    ma_dwie_jedynki = False
    for i in range(len(wiersz)-1):
        if wiersz[i] == '1' and wiersz[i+1] == '1':
            ma_dwie_jedynki = True
            break

    if not ma_dwie_jedynki:
        ile_ciagow_bez_1_obok_siebie += 1

print(ile_ciagow_bez_1_obok_siebie)

#3
#nie chce mi sie


