
licznik = 0
def f(x,p):
    global licznik
    licznik += 1
    if x == 0:
        return 0
    else:
        c = x % p
        if c % 2 == 1:
            return f(x//p,p) + c
        else:
            return f(x//p,p) - c

for i in range(1,100):
    print(f'funkcja: {f(i,4)}, i: {i}')
