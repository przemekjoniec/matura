from fileinput import close

plik = open('dane_obrazki.txt', 'r')
wiersze = plik.readlines()


#Zadanie 64.1
ile_rewersow = 0
max_czarnych_pikseli = 0

for i in range(0, len(wiersze), 22):
    liczba_bialych_pikseli = 0
    liczba_czarnych_pikseli = 0
    for j in range(0, 20):
        wiersz = wiersze[i + j][:len(wiersze[i + j]) - 2]
        for piksel in wiersz:
            if piksel == '0':
                liczba_bialych_pikseli += 1
            else:
                liczba_czarnych_pikseli += 1

    if liczba_czarnych_pikseli > liczba_bialych_pikseli:
        ile_rewersow += 1
    if liczba_czarnych_pikseli > max_czarnych_pikseli:
        max_czarnych_pikseli = liczba_czarnych_pikseli

print(f'max czarnych: {max_czarnych_pikseli}, l. rewersów: {ile_rewersow}')

#Zadanie 64.2
ile_rekurencyjnych = 0
czy_pierwszy = True
do_wydruku_gora = []
do_wydruku_dol = []
for i in range(0, len(wiersze), 22):
    czy_rekurencyjny = True
    for j in range(0,10):
        wiersz = wiersze[i+j][:len(wiersze[i+j]) - 2]
        wiersz_odpowiadajacy = wiersze[i+j+10][:len(wiersze[i+j+10]) - 2]
        if czy_pierwszy:
            do_wydruku_gora.append(wiersz)
            do_wydruku_dol.append(wiersz_odpowiadajacy)
        for k in range(0, 10):
            if wiersz[k] != wiersz[len(wiersz)//2+k] \
                    or wiersz[k] != wiersz_odpowiadajacy[k] \
                    or wiersz[k] != wiersz_odpowiadajacy[len(wiersz)//2+k]:
                        czy_rekurencyjny = False
                        break
        if czy_pierwszy is True and czy_rekurencyjny is False:
            do_wydruku_gora.clear()
            do_wydruku_dol.clear()
        if czy_rekurencyjny is False:
            break
    if czy_rekurencyjny:
        ile_rekurencyjnych += 1
        czy_pierwszy = False

print(f'l rekurencyjnych: {ile_rekurencyjnych}')
print()
for wiersz in do_wydruku_gora:
    print(wiersz)
for wiersz in do_wydruku_dol:
    print(wiersz)

#Zadanie 64.3
#za trudne te zadania nie ma co
