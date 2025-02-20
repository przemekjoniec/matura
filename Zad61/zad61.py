plik1 = open('ciagi.txt','r')
plik2 = open('bledne.txt','r')

wiersze1 = plik1.readlines()
wiersze2 = plik2.readlines()

#ZADANIE 61.1

ile_ciagow_aryt = 0
maksymalna_roznica = 0

for i in range(1,len(wiersze1), 2):
    liczby = wiersze1[i].strip().split(' ')
    roznica = int(liczby[1]) - int(liczby[0])

    czy_ciag_arytm = True
    for j in range(0, len(liczby)-1):
        if int(liczby[j + 1]) - int(liczby[j]) != roznica:
            czy_ciag_arytm = False
            break

    if czy_ciag_arytm:
        ile_ciagow_aryt += 1
        if roznica > maksymalna_roznica:
            maksymalna_roznica = roznica

print("Zad 61.1")
print(f'ile ciągów: {ile_ciagow_aryt}, najwieksza roznica: {maksymalna_roznica}')

#ZADANIE 61.2
max_szesciany = []

for i in range(1,len(wiersze1), 2):
    max_lokalny = -1
    liczby = wiersze1[i].strip().split(' ')
    for liczba in liczby:
        if round(pow(int(liczba), 1/3), 5).is_integer():
            liczba = int(liczba)
            if liczba > max_lokalny:
                max_lokalny = liczba
    if max_lokalny != -1:
        max_szesciany.append(max_lokalny)
print("\nZad 61.1")
for max_szescian in max_szesciany:
    print(max_szescian)

#ZADANIE 61.3

#nie chce mi sie pozdro



