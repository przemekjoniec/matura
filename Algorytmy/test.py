def cyfry_z_liczby(a):
    cyfry = []
    while a > 0:
        cyfra = a % 10
        cyfry.append(cyfra)
        a = a // 10
    return cyfry[::-1]

print(cyfry_z_liczby(1984))

def czy_liczba_pierwsza(a):
    if a == 2:
        return True
    if a%2 == 0 or a<=0:
        return False
    polowa = int((a/2) + 1)
    for dzielnik in range(3, polowa, 2):
        if a%dzielnik == 0:
            return False
    return True

print(czy_liczba_pierwsza(719))

def dzielniki_liczby(a):
    for i in range(1, int(a/2+1)):
        if a%i == 0:
            print(str(i) + " ")
    print(a)

print(dzielniki_liczby(150))

def nwd(a,b):
    if a % b == 0:
        return b
    else:
        return nwd(b, a % b)

print(nwd(4,6))
a=4
b=6
print(f'NWW: {a * b/nwd(a,b)}')

def rozklad_na_czynniki_pierwsze(a):
    k = 2
    while a>1:
        while a%k==0:
            print(k)
            a //= k
        k+=1

print(rozklad_na_czynniki_pierwsze(56))
