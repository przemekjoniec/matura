def f(n):
    if n > 0:
        print(n)
        f(n-2)
        print(n)

print(f(8))

