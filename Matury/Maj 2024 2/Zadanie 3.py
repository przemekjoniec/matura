def f(n):
    m = ''
    while n > 0:
        litera = n % 10
        if litera % 2 != 0:
            m += str(litera)
        n //= 10
    return m[::-1]

print(f(294762))