def cyfrazliczby(n):
    cyfry=[]
    while n > 0:
        cyfra = n%10
        cyfry.append(cyfra)
        n //= 10
    return cyfry[::-1]

print(cyfrazliczby(10564))

def czyliczbapierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(n//2)+1,2):
        if n % i == 0:
            return False
    return True

print(czyliczbapierwsza(5))

def dzielnikiliczby(n):
    dzielniki=[]
    m = n
    for i in range(1,int(n//2)+1):
        if n % i == 0:
            dzielniki.append(i)
    dzielniki.append(m)
    return dzielniki

print(dzielnikiliczby(32))

def nwd(a,b):
    if a % b == 0:
        return b
    else:
        return nwd(b, a % b)
print(nwd(6,14))

#NWW

a = 6
b = 14
print(f'{int(a*b/nwd(a,b))}')

def rozkladnaczynnikipierwsze(n):
    k = 2
    czynniki = []
    while n > 1:
        while n % k == 0:
            czynniki.append(k)
            n //= k
        k += 1
    return czynniki
print(rozkladnaczynnikipierwsze(345))

def z10na3(n):
    wynik = ""
    while n > 0:
        wynik = str(n%3) + wynik
        n = n // 3
    return wynik

print(z10na3(345))
