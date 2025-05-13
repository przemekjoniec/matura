plik = open('skrot_przyklad.txt','r')
wiersze = plik.readlines()

def f(n):
    m = ''
    while n > 0:
        litera = n % 10
        if litera % 2 != 0:
            m += str(litera)
        n //= 10
    return m[::-1]

licznik = 0
max_liczba = 0
for wiersz in wiersze:
    wiersz = int(wiersz.strip())
    m = f(wiersz)
    if m == '':
        licznik += 1
        if wiersz > max_liczba:
            max_liczba = wiersz

print(licznik)
print(max_liczba)