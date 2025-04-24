licznik = 0

def modyfikuj(s, k, n):
    global licznik
    licznik += 1
    if s + k < n:
        modyfikuj(s + k, k, n)
    i = s + 1

n = 2021
modyfikuj(20, 35, n)
print(licznik)