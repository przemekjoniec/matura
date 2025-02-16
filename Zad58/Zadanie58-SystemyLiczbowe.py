import math
plik_1 = open('dane_systemy1.txt','r')
plik_2 = open('dane_systemy2.txt','r')
plik_3 = open('dane_systemy3.txt','r')

wiersze_1 = plik_1.readlines()
wiersze_2 = plik_2.readlines()
wiersze_3 = plik_3.readlines()

# ZADANIE 58.1

min_1 = int(wiersze_1[0].split(' ')[1].strip(), 2)
min_2 = int(wiersze_2[0].split(' ')[1].strip(), 4)
min_3 = int(wiersze_3[0].split(' ')[1].strip(), 8)

for wiersz in wiersze_1:
    temperatura = int(wiersz.split(' ')[1].strip(), 2)
    if temperatura < min_1:
        min_1 = temperatura

for wiersz in wiersze_2:
    temperatura = int(wiersz.split(' ')[1].strip(), 4)
    if temperatura < min_2:
        min_2 = temperatura

for wiersz in wiersze_3:
    temperatura = int(wiersz.split(' ')[1].strip(), 8)
    if temperatura < min_3:
        min_3 = temperatura

print("Zadanie 58.1 WYNIKI:")
print(bin(min_1).replace('0b', ''))
print(bin(min_2).replace('0b', ''))
print(bin(min_3).replace('0b', ''))


# ZADANIE 58.2

ile_blednych_jednoczesnie = 0
start = 12

for i in range(0,len(wiersze_1)):
    poprawna_wartosc = start + 24 * i
    odczyt_1= int(wiersze_1[i].split(' ')[0].strip(), 2)
    odczyt_2= int(wiersze_2[i].split(' ')[0].strip(), 4)
    odczyt_3= int(wiersze_3[i].split(' ')[0].strip(), 8)

    if odczyt_1 != poprawna_wartosc and odczyt_2 != poprawna_wartosc and odczyt_3 != poprawna_wartosc:
        ile_blednych_jednoczesnie += 1

print("\nZadanie 58.2 WYNIKI:")
print(f'Ilość błędnych pomiarów {ile_blednych_jednoczesnie}')

# ZADANIE 58.3

ile_dni_rekordowych = 1
rekord_1 = int(wiersze_1[0].split(' ')[1].strip(), 2)
rekord_2 = int(wiersze_2[0].split(' ')[1].strip(), 4)
rekord_3 = int(wiersze_3[0].split(' ')[1].strip(), 8)

for i in range(1,len(wiersze_1)):
    temperatura_1 = int(wiersze_1[i].split(' ')[1].strip(), 2)
    temperatura_2 = int(wiersze_2[i].split(' ')[1].strip(), 4)
    temperatura_3 = int(wiersze_3[i].split(' ')[1].strip(), 8)

    czy_rekord = False

    if temperatura_1 > rekord_1:
        czy_rekord = True
        rekord_1 = temperatura_1
    if temperatura_2 > rekord_2:
        czy_rekord = True
        rekord_2 = temperatura_2
    if temperatura_3 > rekord_3:
        czy_rekord = True
        rekord_3 = temperatura_3

    if czy_rekord == True:
        ile_dni_rekordowych += 1

print("\nZadanie 58.3 WYNIKI:")
print(ile_dni_rekordowych)

# ZADANIE 58.4

max_skok = 0

for i in range(0,len(wiersze_1)):
    for j in range(0,len(wiersze_1)):
        if i != j:
            t_i = int(wiersze_1[i].split(' ')[1].strip(), 2)
            t_j = int(wiersze_1[j].split(' ')[1].strip(), 2)

            r = (t_i - t_j)**2
            skok = math.ceil(r / abs(i - j))
            if skok > max_skok:
                max_skok = skok

print("\nZadanie 58.4 WYNIKI:")
print(max_skok)