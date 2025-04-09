plik = open('odbiorcy_przyklad.txt','r')
wiersze = plik.readlines()

#4.1
komputery = {}
for i in range(1,len(wiersze)+1):
        if i in komputery:
            komputery[i] += 1
        else:
            komputery[i] = 1

for wiersz in wiersze:
    wiersz = int(wiersz.strip())
    if wiersz in komputery:
        komputery[wiersz] += 1
    else:
        komputery[wiersz] = 1

licznik = 0
for liczba in komputery.values():
    if liczba == 1:
        licznik += 1
print(licznik)


