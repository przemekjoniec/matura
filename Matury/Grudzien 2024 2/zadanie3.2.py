plik = open('liczby.txt','r')
wiersze = plik.readlines()

def czy_pierwsza(x):
    if x == 2:
        return True
    if x % 2 == 0 or x <= 1:
        return False
    for i in range(3, int(x//2)+1):
        if x % i == 0:
            return False
    return True

# def dzielniki(x):
#     for i in range(1,int(x / 2) + 1):
#         if x % i == 0:
#             print(str(i) + " "),
#     print(x)
liczby_z_5_czynnikami_pierwszymi = []
for wiersz in wiersze:
    czynniki = []
    wiersz = int(wiersz.strip())
    for i in range(1,int(wiersz / 2) + 1):
        if wiersz % i == 0 and czy_pierwsza(i) and i not in czynniki:
            czynniki.append(i)
    if len(czynniki) >= 5:
        liczby_z_5_czynnikami_pierwszymi.append(wiersz)

print(liczby_z_5_czynnikami_pierwszymi)






