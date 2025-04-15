def SumaKwCyfr(n):
    wynik = 0
    while n > 0:
        cyfra = n % 10
        wynik += cyfra ** 2
        n = n // 10
    return wynik

print(SumaKwCyfr(123))