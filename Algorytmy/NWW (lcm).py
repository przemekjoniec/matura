def nwd(a, b):
    if a % b == 0:
        return b
    else:
        return nwd(b, a % b)

a = 31
b = 3
print(f'NWW liczb {a} i {b}: {a * b/nwd(a, b)}')

#NWW(a,b) = a*b/nwd(a,b)