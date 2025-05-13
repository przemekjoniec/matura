plik = open('slowa.txt','r')
wiersze = plik.readlines()

licznik = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    for i in range(0,len(wiersz)-2):
        if wiersz[i] == 'k' and wiersz[i+2] == 't':
            licznik = licznik + 1

print(licznik)