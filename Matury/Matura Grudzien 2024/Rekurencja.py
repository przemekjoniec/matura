
def F(x,p, licznik = 0):
    licznik += 1
    if x == 0:
        return 0, licznik
    else:
        c = x % p
        if c % 2 == 1:
            wynik, licznik = F(x//p,p, licznik)
            return wynik + c, licznik
        else:
            wynik, licznik = F(x//p,p, licznik)
            return wynik - c, licznik

for i in range(1,99):
    wynik, licznik = F(i,4)
    print(f'Wynik {wynik}, licznik {licznik}, dla i : {i}')


