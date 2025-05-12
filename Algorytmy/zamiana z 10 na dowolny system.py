def zamianaz10z2(n):
    wynik = ""
    while n > 0:
        wynik = str(n % 2) + wynik
        n = n // 2
    return wynik

def zamianaz10z7(n):
    wynik = ""
    while n > 0:
        wynik = str(n % 7) + wynik
        n = n // 7
    return wynik

def zamianaz10z3(n):
    wynik = ""
    while n > 0:
        wynik = str(n % 3) + wynik
        n = n // 3
    return wynik

print(zamianaz10z2(45))
print(zamianaz10z7(45))
print(zamianaz10z3(345))