plik = open('skrot2.txt','r')
wiersze = plik.readlines()

def nieparzysty_skrot(n):
    m = 0
    p = 1
    while n > 0:
        cyfra = n % 10
        if cyfra % 2 != 0:
            m = m + cyfra * p
            p = p * 10
        n = n // 10
    return m

def nwd(n, np):
    if n % np == 0:
        return np
    else:
        return nwd(np, n % np)

for wiersz in wiersze:
    n = wiersz.strip()
    n = int(n)
    np = nieparzysty_skrot(n)
    dzielnik = nwd(n, np)
    if dzielnik == 7:
        print(n)


    #2
# licznik = 0
# max_liczba = 46
#
# for wiersz in wiersze:
#     wiersz = wiersz.strip()
#     wynik = nieparzysty_skrot(int(wiersz))
#     if wynik == 0:
#         licznik += 1
#         if int(wiersz) > int(max_liczba):
#             max_liczba = wiersz
#
# print(licznik, max_liczba)

