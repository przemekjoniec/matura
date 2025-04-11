def iloczyn(x,y, licznik = 0):
    k = 0
    z = 0
    if y == 1:
        return x
    else:
        k = y // 2
        z = x * k
        if y % 2 == 0:
            wynik = z + z
            return wynik, k, z, licznik
        else:
            wynik =  x + z + z
            return wynik, k, z, licznik

print(iloczyn(9,11))
