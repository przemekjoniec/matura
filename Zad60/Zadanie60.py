plik = open('liczby.txt', 'r')
wiersze = plik.readlines()


#ZADANIE 60.1
ilosc = []

for wiersz in wiersze:
    liczba = int(wiersz.strip())
    if liczba < 1000:
        ilosc.append(liczba)


print(len(ilosc))
print(ilosc[len(ilosc)-1])
print(ilosc[len(ilosc)-2])

#ZADANIE 60.2
def znajdz_dzielniki(liczba):
    dzielniki=[]
    for i in range(1, liczba // 2 + 1):
        if liczba % i == 0:
            dzielniki.append(i)

    dzielniki.append(liczba)
    return sorted(dzielniki)

for wiersz in wiersze:
    liczba = int(wiersz.strip())
    dzielniki = znajdz_dzielniki(liczba)
    if len(dzielniki) == 18:
        print(f'Liczba: {liczba}, jej dzielniki: {dzielniki}')




