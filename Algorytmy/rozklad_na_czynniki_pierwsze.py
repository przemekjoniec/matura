def czynniki_pierwsze(a):
    k = 2
    while a>1:
        while a%k==0:
            print(k)
            a //= k
        k += 1

print(czynniki_pierwsze(420))


