#Zadanie 67.1
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    n1 = 1
    n2 = 1
    for i in range (3, n+1):
        pomoc = n1
        n1 = n2
        n2 = n1 + pomoc

    return n2

print(fibonacci(5))

#Zadanie 67.2

def czy_pierwsza(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n//2 + 1, 2):
        if n % i == 0:
            return False
    return True

for i in range (1, 41):
    liczba = fibonacci(i)
    if czy_pierwsza(liczba):
        print(f'f{i}: {liczba}')

#Zadanie 67.3

binarne = []
binarne_uzupełnione = []

for i in range (1, 41):
    liczba = fibonacci(i)
    binarne.append(bin(liczba)[2::])

dł_maks = len(bin(fibonacci(40))[2::])

for liczba in binarne:
    dł_liczby = len(liczba)
    zera = ''
    for i in range(0, dł_maks - dł_liczby):
        zera += '0'
    binarne_uzupełnione.append(zera + liczba)

for liczba in binarne:
    print(liczba)
for liczba in binarne_uzupełnione:
    l_oddzielona = ''
    for cyfra in liczba:
        l_oddzielona += cyfra
        l_oddzielona += ' '
    print(l_oddzielona)

#Zadanie 67.4
dokładnie_6_jedynek = []

for i in range(1, 41):
    liczba = fibonacci(i)
    binarne = bin(liczba)[2::]
    ile_jedynek = 0
    for cyfra in binarne:
        if cyfra == '1':
            ile_jedynek += 1

    if ile_jedynek == 6:
        dokładnie_6_jedynek.append(binarne)

for liczba in dokładnie_6_jedynek:
    print(liczba)