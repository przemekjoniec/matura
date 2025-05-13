plik = open('skrot2.txt','r')
wiersze = plik.readlines()
import math

def f(n):
    m = ''
    while n > 0:
        litera = n % 10
        if litera % 2 != 0:
            m += str(litera)
        n //= 10
    return m[::-1]

for wiersz in wiersze:
    wiersz = int(wiersz.strip())
    m = int(f(wiersz))
    if math.gcd(wiersz,m) == 7:
        print(wiersz)


