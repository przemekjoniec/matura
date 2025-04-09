def binarka(n):
    liczba_binarna = []
    while n>0:
        liczba_binarna.insert(0, str(n%2))
        n = n//2
    return liczba_binarna

print(binarka(20))
