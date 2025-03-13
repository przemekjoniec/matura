plik = open('ciagi.txt','r')
wiersze = plik.readlines()

#1
ilosc_ciagow = 0
maksymalna_roznica = 0
for i in range(1, len(wiersze), 2):
    liczby = wiersze[i].strip().split(' ')
    roznica = int(liczby[1]) - int(liczby[0])

    czy_ciag_arytm = True
    for j in range(0, len(liczby)-1):
        # if int(liczby[j+1]) - int(liczby[j]) != roznica:
        #     czy_ciag_arytm = False
        #     break
        if int(liczby[j]) + roznica != int(liczby[j+1]):
            czy_ciag_arytm = False
            break
    if czy_ciag_arytm:
        ilosc_ciagow += 1
        if roznica > maksymalna_roznica:
            maksymalna_roznica = roznica
print(ilosc_ciagow)
print(maksymalna_roznica)

#2
max_szesciany = []
for i in range(1, len(wiersze), 2):
    max_lokalny = -1
    liczby = wiersze[i].strip().split(' ')

    for liczba in liczby:
        if round(pow(int((liczba)),1/3),5).is_integer():
            if int(liczba) > max_lokalny:
                max_lokalny = int(liczba)
    if max_lokalny != -1:
        max_szesciany.append(max_lokalny)
print(max_szesciany)

#3
plik1 = open('bledne.txt','r')
wiersze1 = plik1.readlines()

bledne_liczby = []
for i in range(1, len(wiersze1), 2):
    liczby = wiersze1[i].strip().split(' ')
    roznica = int(liczby[1]) - int(liczby[0])

    for j in range(0, len(liczby)-1):
        if int(liczby[j+1]) - int(liczby[j]) != roznica:
            bledne_liczby.append(liczby[j+1])
            break
        # if int(liczby[j]) + roznica != int(liczby[j+1]):
        #     bledne_liczby.append(liczby[j+1])
        #     break

print(bledne_liczby)
