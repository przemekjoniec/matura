from time import perf_counter

licznik = 0
def Algo(n):
    global licznik
    if n<= 2:
        return "1"
    else:
        p = 1
        k = n
        while k - p > 1:
            s = (p+k) // 2
            licznik += 1
            if s * s <= n:
                p = s
            else:
                k = s
        return p

print(Algo(1024))
print(licznik)
