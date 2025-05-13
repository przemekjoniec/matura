
licznik = 0
def f(n):
    global licznik

    b = 1
    c = 0
    while n > 0:
        a = n % 10
        n = n // 10
        if a%2 == 0:
            c = c + b * (a//2)
        else:
            c = c + b
            licznik += 1
        b = b * 10
    return c

print(f(333333666666999999))
print(licznik)
