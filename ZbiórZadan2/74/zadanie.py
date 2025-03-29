from Zad74.zad74 import jest_liczba, jest_mala_litera, jest_wielka_litera

plik = open('hasla.txt','r')
wiersze = plik.readlines()

ile_hasel_tylko_cyfry = 0

#1

# for wiersz in wiersze:
#     wiersz = wiersz.strip()
#     if wiersz.isdigit():
#         ile_hasel_tylko_cyfry += 1

for wiersz in wiersze:
    wiersz = wiersz.strip()
    tylko_cyfry = True
    for znak in wiersz:
        if znak not in ('0123456789'):
            tylko_cyfry = False
            break
    if tylko_cyfry:
        ile_hasel_tylko_cyfry += 1

print(ile_hasel_tylko_cyfry)


#2

hasla = []
powtorzenia = set()

for wiersz in wiersze:
    wiersz = wiersz.strip()
    if wiersz not in hasla:
        hasla.append(wiersz)
    else:
        powtorzenia.add(wiersz)

for element in sorted(powtorzenia):
    print(element)

#4
spelnia_wymogi = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()

    jest_liczba = False
    jest_mala_litera = False
    jest_wielka_litera = False

    for litera in wiersz:
        if litera >= '0' and litera <= '9':
            jest_liczba = True
        if litera >= 'a' and litera <= 'z':
            jest_mala_litera = True
        if litera >= 'A' and litera <= 'Z':
            jest_wielka_litera = True

    if jest_liczba and jest_mala_litera and jest_wielka_litera:
        spelnia_wymogi += 1

print(spelnia_wymogi)