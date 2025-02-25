plik = open('ciagi.txt', 'r')
wiersze = plik.readlines()

#Zadanie 63.1

def czy_dwucykliczny(ciag):
    if len(ciag) % 2 != 0:
        return False
    for i in range(0, len(ciag)//2):
        if ciag[i] != ciag[len(ciag)//2+i]:
            return False
    return True

ile_dwucyklicznych = 0
ciagi = []
for wiersz in wiersze:
    wiersz = wiersz.strip()
    if czy_dwucykliczny(wiersz):
        ile_dwucyklicznych += 1
        ciagi.append(wiersz)

print(f'Ilosc: {ile_dwucyklicznych}')
print(f'Ciagi: {ciagi}')

#Zadanie 63.2
def czy_jedynki_obok_siebie(ciag):
    for i in range (1, len(ciag)):
        if ciag[i] == ciag[i-1] and ciag [i] == '1':
            return False
    return True

ile_bez_jedynek_obok = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    if czy_jedynki_obok_siebie(wiersz):
        ile_bez_jedynek_obok += 1

print(f'Ile : {ile_bez_jedynek_obok}')

#Zadanie 63.3
#do zrobienia