plik = open('dane_geny.txt', 'r')
wiersze = plik.readlines()

# Zadanie 69.1

gatunki = {}
for i in range(1,501):
    gatunki[i] = 0

ile_gatunków = 0
max_osobników = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    gatunki[len(wiersz)] += 1


for i in gatunki:
    if gatunki[i] != 0:
        ile_gatunków += 1
    if gatunki[i] > max_osobników:
        max_osobników = gatunki[i]


print(f'Liczba gatunków: {ile_gatunków}, max osobników: {max_osobników}')

# Zadanie 69.2
def znajdz_geny(genotyp):
    geny = []
    koniec = 0
    for i in range(0, len(genotyp)-1):
        if koniec > i:
            continue
        if genotyp[i] == 'A' and genotyp[i+1] == 'A':
            gen = 'AA'
            for j in range(i+2, len(genotyp)-1):
                if genotyp[j] == 'B' and genotyp[j + 1] == 'B':
                    gen += 'BB'
                    koniec = j+2
                    geny.append(gen)
                    break
                gen+=genotyp[j]

    return geny

ile_z_mutacja = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    geny = znajdz_geny(wiersz)
    for gen in geny:
        if gen.find('BCDDC') != -1:
            ile_z_mutacja += 1


print(f'Tyle osobników z mutacja: {ile_z_mutacja}')

# Zadanie 69.3

max_liczba_genów = 0
max_dlugosc = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    geny = znajdz_geny(wiersz)
    if len(geny) > max_liczba_genów:S
        max_liczba_genów = len(geny)
    for gen in geny:
        if len(gen) > max_dlugosc:
            max_dlugosc = len(gen)

print(f'Max liczba genów: {max_liczba_genów}, max dlugosc: {max_dlugosc}')

# Zadnie 69.4

ile_odpornych = 0
ile_silnie_odpornych = 0

for wiersz_od_lewej_do_prawej in wiersze:
    wiersz_od_lewej_do_prawej = wiersz_od_lewej_do_prawej.strip()
    wiersz_od_prawe_do_lewej = wiersz_od_lewej_do_prawej[::-1]
    gen_od_lewej = znajdz_geny(wiersz_od_lewej_do_prawej)
    geny_od_prawej = znajdz_geny(wiersz_od_prawe_do_lewej)

    if wiersz_od_prawe_do_lewej == wiersz_od_lewej_do_prawej:
        ile_silnie_odpornych += 1
    if gen_od_lewej == geny_od_prawej:
        ile_odpornych += 1

print(f'Genów silnie odpornych: {ile_silnie_odpornych}, genów odpornych: {ile_odpornych}')



