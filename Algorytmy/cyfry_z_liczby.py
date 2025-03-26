def cyfry_z_liczby(n):
    cyfry = []
    while n > 0:
        cyfra = n % 10
        cyfry.append(cyfra)
        n = n // 10
    return cyfry[::-1]

print(cyfry_z_liczby(1984))