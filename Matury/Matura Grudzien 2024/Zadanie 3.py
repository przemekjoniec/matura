plik = open('liczby.txt', 'r')
wiersze = plik.readlines()

#1
# kwadraty_liczb_całkowitych = []
# for i in range(31,100):
#     kwadrat = i * i
#     kwadrat = str(kwadrat)
#     kwadraty_liczb_całkowitych.append(kwadrat)
#
# # print(kwadraty_liczb_całkowitych)
#
# kwadraty = []
# licznik_kwadratów = 0
# for wiersz in wiersze:
#     wiersz = wiersz.strip()
#     for i in range(0, len(kwadraty_liczb_całkowitych)):
#         if wiersz == kwadraty_liczb_całkowitych[i]:
#             kwadraty.append(wiersz)
#             licznik_kwadratów += 1
#
# print(kwadraty)
# print(licznik_kwadratów)



# liczby = ['1','7','3','9']
# liczby_min = sorted(liczby)
# liczby_max = sorted(liczby, reverse=True)
#
# liczba_min = liczby[0] + liczby[1] + liczby[2] + liczby[3]
# liczba_max = liczby[3] + liczby[2] + liczby[1] + liczby[0]
#
# print(liczba_min, liczba_max)

#3
wieksza = 0
mniejsza = 0
rowna = 0
rowne = []
for wiersz in wiersze:
    liczby = []
    wiersz = wiersz.strip()
    wiersz = str(wiersz)
    for znak in wiersz:
        liczby.append(znak)
    liczby_min = sorted(liczby)
    liczby_max = sorted(liczby, reverse=True)
    liczba_min = int(liczby_min[0] + liczby_min[1] + liczby_min[2] + liczby_min[3])
    liczba_max = int(liczby_max[0] + liczby_max[1] + liczby_max[2] + liczby_max[3])

    roznica = liczba_max - liczba_min
    wiersz = int(wiersz)
    if roznica > wiersz:
        wieksza += 1
    if roznica < wiersz:
        mniejsza += 1
    if roznica == wiersz:
        rowna += 1
        rowne.append(wiersz)

print(wieksza, mniejsza, rowna)
print(rowne)


