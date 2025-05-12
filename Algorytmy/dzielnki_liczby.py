def dzielniki(x):
    for i in range(1,int(x / 2) + 1):
        if x % i == 0:
            print(str(i) + " "),
    print(x)

print(dzielniki(44))