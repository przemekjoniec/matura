from imaplib import Flags

plik = open('hasla.txt', 'r')
wiersze = plik.readlines()

#Zadanie 74.1

tylko_alfanumeryczne = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    if wiersz.isdigit():
        tylko_alfanumeryczne += 1

print(tylko_alfanumeryczne)

#Zadanie 74.2

hasla = []
powtorzenia = set()

for wiersz in wiersze:
    wiersz = wiersz.strip()
    if wiersz not in hasla:
        hasla.append(wiersz)
    else:
        powtorzenia.add(wiersz)

for powtorzenie in sorted(powtorzenia):
    print(powtorzenie)

#Zadanie 74.3

ile_hasel = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()

    for i in range(0, len(wiersz)-3):
        litery = set()
        litery.add(wiersz[i])
        litery.add(wiersz[i+1])
        litery.add(wiersz[i+2])
        litery.add(wiersz[i+3])

        litery = sorted(litery)
        if len(litery) != 4:
            continue
        if ord(litery[3]) - ord(litery[0]) <= 3:
            ile_hasel += 1
            break

print(ile_hasel)

# Zadanie 74.4

ile_haselek = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()

    jest_liczba = False
    jest_mala_litera = False
    jest_wielka_litera = False

    for litera in wiersz:
        if litera >= '0' and litera <= '9':
            jest_liczba = True
        elif litera >= 'a' and litera <= 'z':
            jest_mala_litera = True
        elif litera >= 'A' and litera <= 'Z':
            jest_wielka_litera = True


    if jest_liczba and jest_mala_litera and jest_wielka_litera:
        ile_haselek += 1

print(ile_haselek)



