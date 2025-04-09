plik = open('slowa.txt','r')
wiersze = plik.readlines()


#3.1
licznik = 0
for wiersz in wiersze:
    wiersz = wiersz.strip('\n')
    for i in range(0, len(wiersz)-2):
        if wiersz[i] == 'k' and wiersz[i+2] == 't':
            licznik = licznik + 1
            break

print(licznik)
print('=============================')

#3.2
def rot13(slowo):
    zamiana = ""
    for i in range(len(slowo)):
        literka = ord(slowo[i])+13
        if literka > 122:
            literka -= 26
        zamiana += chr(literka)
    return zamiana

ile = 0
max_slowo = ''

for wiersz in wiersze:
    wiersz = wiersz.strip()
    nowe = rot13(wiersz)
    if wiersz == nowe[::-1]:
        ile += 1
        if len(wiersz) > len(max_slowo):
            max_slowo = wiersz

print(max_slowo)
print(ile)
print('=============================')

#3.3
licznik_2 = 0
for wiersz in wiersze:
    wiersz = wiersz.strip('\n')
    zliczenia = {}
    polowa = len(wiersz)/2
    for znak in wiersz:
        if znak in zliczenia:
            zliczenia[znak] += 1
        else:
            zliczenia[znak] = 1
    if any(liczba >= polowa for liczba in zliczenia.values()):
            licznik_2 += 1
            print(wiersz)

print(licznik_2)
