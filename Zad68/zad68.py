plik = open('dane_napisy.txt', 'r')
wiersze = plik.readlines()

#Zadanie 68.1
def czy_jednolity(napis):
    litera = napis[0]
    for i in range(1, len(napis)):
        if litera != napis[i]:
            return False
    return True

ile_par_napisow_jednolitych = 0
for wiersz in wiersze:
    napisy = wiersz.strip().split(' ')
    if czy_jednolity(napisy[0]) and czy_jednolity(napisy[1]) and napisy[0][0] == napisy[1][0] and len(napisy[0]) == len(napisy[1]):
        ile_par_napisow_jednolitych += 1

print(f'Par: {ile_par_napisow_jednolitych}')

#Zadanie 68.2
def czy_anagramy(napis1, napis2):
    if len(napis1) != len(napis2):
        return False

    liczniki = {}
    for i in range(1, 128):
        liczniki[i] = 0

    for i in range(0, len(napis1)):
        liczniki[ord(napis1[i])] += 1

    for i in range(0, len(napis2)):
        liczniki[ord(napis2[i])] -= 1

    for i in range(1, 128):
        if liczniki[i] != 0:
            return False

    return True

ile_anagramow = 0

for wiersz in wiersze:
    napisy = wiersz.strip().split(' ')
    if czy_anagramy(napisy[0], napisy[1]):
        ile_anagramow += 1

print(f'Ilosc anagramow: {ile_anagramow}')


#Zadanie 68.3

max_anagram = 0
for wiersz in wiersze:
    napisy = wiersz.strip().split(' ')
    lokalny_anagram = 0

    for wiersz in wiersze:
        napisy_zaglebione = wiersz.strip().split(' ')
        if czy_anagramy(napisy[0], napisy_zaglebione[0]):
            lokalny_anagram += 1
        if czy_anagramy(napisy[0], napisy_zaglebione[1]):
            lokalny_anagram += 1
    if lokalny_anagram > max_anagram:
        max_anagram = lokalny_anagram

    lokalny_anagram = 0

    for wiersz in wiersze:
        napisy_zaglebione = wiersz.strip().split(' ')
        if czy_anagramy(napisy[1], napisy_zaglebione[0]):
            lokalny_anagram += 1
        if czy_anagramy(napisy[1], napisy_zaglebione[1]):
            lokalny_anagram += 1
    if lokalny_anagram > max_anagram:
            max_anagram = lokalny_anagram

print(f'Max anagramow: {max_anagram}')