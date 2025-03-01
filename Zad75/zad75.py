plik = open('tekst.txt', 'r')
wiersz = plik.readline()

#Zadanie 75.1

slowa_spelniajace_warunek = []
slowa = wiersz.strip().split(' ')

for slowo in slowa:
    if slowo[0] == 'd' and slowo[len(slowo) - 1] == 'd':
        slowa_spelniajace_warunek.append(slowo)

for slowo in slowa_spelniajace_warunek:
    print(slowo)


#Zadanie 75.2

litery = {}
for i in range (0,26):
    litery[i] = chr(97 + i)

def zaszyfruj_slowo(slowo, A, B):
    zaszyfrowane_slowo = ''
    for litera in slowo:
        kod = ((ord(litera)-97)*A+B)%26
        zaszyfrowane_slowo += litery[kod]
    return zaszyfrowane_slowo

for slowo in slowa:
    if len(slowo) >= 10:
        print(zaszyfruj_slowo(slowo,5,2))