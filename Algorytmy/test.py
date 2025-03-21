def czy_pierwsza(a):
    if a == 2:
        return True
    if a%2 == 0:
        return False
    pierwsza = int(a/2)+1
    for dzielniki in range(3, pierwsza, 2):
        if a % dzielniki == 0:
            return False
    return True

print(czy_pierwsza(29))


def nwd(a,b):
    if a % b == 0:
        return b
    else:
        return nwd(b, a%b)


print(nwd(12,16))
a=31
b=3
print(f'nww: {a*b/nwd(a,b)}')

def czynniki(n):
    k = 2
    while n>1:
        while n%k==0:
            print(k)
            n//=k
        k+=1

print(czynniki(1520))