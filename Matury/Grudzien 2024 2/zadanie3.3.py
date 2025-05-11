plik = open('liczby.txt','r')
wiersze = plik.readlines()

mniejsza = 0
wieksza = 0
rowna = 0
rowne = []

for wiersz in wiersze:
    liczba = []
    wiersz = wiersz.strip()
    for cyfra in wiersz:
        liczba.append(int(cyfra))
    liczba.sort()
    min_liczba = ''
    for znak in liczba:
        min_liczba += str(znak)
    liczba.sort(reverse=True)
    max_liczba = ''
    for znak in liczba:
        max_liczba += str(znak)
    min_liczba = int(min_liczba)
    max_liczba = int(max_liczba)
    wiersz = int(wiersz)

    if max_liczba - min_liczba == wiersz:
        rowna += 1
        rowne.append(wiersz)
    elif max_liczba - min_liczba > wiersz:
        wieksza += 1
    elif max_liczba - min_liczba < wiersz:
        mniejsza += 1

print(mniejsza)
print(rowna)
print(wieksza)
print(rowne)
