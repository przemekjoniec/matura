plik = open('anagram.txt','r')
wiersze = plik.readlines()

#A

lista_wierszy = []

for wiersz in wiersze:
    wiersz = wiersz.strip().split(' ')
    if len(wiersz[0]) == len(wiersz[1]) and len(wiersz[0]) == len(wiersz[2]) and len(wiersz[0]) == len(wiersz[3]) and len(wiersz[0]) == len(wiersz[4]):
        lista_wierszy.append(wiersz)

print(lista_wierszy)

#B
from collections import Counter
def czy_anagram(slowo1, slowo2, slowo3, slowo4, slowo5):
    if len(slowo1) != len(slowo2) or len(slowo1) != len(slowo3) or len(slowo1) != len(slowo4) or len(slowo1) != len(slowo5):
        return False

    return Counter(slowo1) == Counter(slowo2) == Counter(slowo3) == Counter(slowo4) == Counter(slowo5)

anagramy = []
for wiersz in wiersze:
    napis = wiersz.strip().split(' ')
    if czy_anagram(napis[0], napis[1], napis[2], napis[3], napis[4]):
        anagramy.append(napis)

print(anagramy)


