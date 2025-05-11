plik = open('liczby.txt','r')
wiersze = plik.readlines()

licznik = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    for i in range(1,101):
        kwadrat = str(i*i)
        if kwadrat == wiersz:
            print(kwadrat)
            licznik += 1

print(licznik)



