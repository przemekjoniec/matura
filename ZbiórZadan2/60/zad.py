plik = open('liczby.txt','r')
wiersze = plik.readlines()

#1
liczby_mniejsze_niz_1000 = []

for wiersz in wiersze:
    wiersz = wiersz.strip()
    wiersz = int(wiersz)
    if wiersz < 1000:
        liczby_mniejsze_niz_1000.append(wiersz)

print(len(liczby_mniejsze_niz_1000))
print(liczby_mniejsze_niz_1000[len(liczby_mniejsze_niz_1000)-1])
print(liczby_mniejsze_niz_1000[len(liczby_mniejsze_niz_1000)-2])

#2
def znajdz_dzielniki(liczba):
    dzielniki = []

    for i in range(1, liczba):
        if liczba % i == 0:
            dzielniki.append(i)
    dzielniki.append(liczba)
    return sorted(dzielniki)


for wiersz in wiersze:
    wiersz = wiersz.strip()
    wiersz = int(wiersz)
    dzielnik = znajdz_dzielniki(wiersz)
    if len(dzielnik) == 18:
        print(f'Liczba: {wiersz}, dzielniki: {dzielnik}')











plik.close()
