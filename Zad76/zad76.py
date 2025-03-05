#Zadanie 76.1

# ZADANIE 76.1.
def zaszyfruj_słowo(słowo, tablica):
    licznik = 0
    for i in range(0, len(słowo)):
        if licznik == len(tablica):
            licznik = 0
        nowe_słowo = list(słowo)
        litera_do_zamiany = słowo[i]
        nowe_słowo[i] = słowo[tablica[licznik] - 1]
        nowe_słowo[tablica[licznik] - 1] = litera_do_zamiany
        słowo = ''.join(nowe_słowo)
        licznik += 1
    return słowo

print(zaszyfruj_słowo('INFORMATYKA', [3,2,5,4,1]))

plik = open('szyfr1.txt','r')
wiersze = plik.readlines()

klucz = wiersze[6].strip().split(' ')
for i in range(0, len(klucz)):
    klucz[i] = int(klucz[i])

słowa = []
for i in range (0, len(wiersze)-1):
    słowa.append(wiersze[i].strip())

for słowo in słowa:
    print(zaszyfruj_słowo(słowo, klucz))


#Zadanie 76.2

plik = open('szyfr2.txt','r')
wiersze = plik.readlines()

słowo = wiersze[0].strip()
klucz = wiersze[1].strip().split(' ')
for i in range(0, len(klucz)):
    klucz[i] = int(klucz[i])

print('=========')
print(zaszyfruj_słowo(słowo, klucz))

