plik = open('dane_napisy.txt','r')
wiersze = plik.readlines()


#68.1
anagramy = []
jednolite = 0

for wiersz in wiersze:
    wiersz = wiersz.strip(' ').split()
    if len(wiersz[0]) == len(wiersz[1]) and sorted(wiersz[0]) == sorted(wiersz[1]):
        anagramy.append(wiersz)

def czy_jednolity(napis1):
    pierwszy_znak = napis1[0]
    for znak in napis1:
        if znak != pierwszy_znak:
            return False
    return True

for i in range(len(anagramy)):
    if czy_jednolity(anagramy[i][0]):
        jednolite += 1

print(jednolite)

#68.2
licznik_anagramów = 0
for wiersz in wiersze:
    wiersz = wiersz.strip(' ').split()
    if len(wiersz[0]) == len(wiersz[1]) and sorted(wiersz[0]) == sorted(wiersz[1]):
        licznik_anagramów += 1

print(licznik_anagramów)

