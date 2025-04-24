plik = open('liczby.txt','r')
wiersze = plik.readlines()


#4.1

# liczby = []
# for wiersz in wiersze:
#     wiersz = wiersz.strip()
#     if wiersz[0] == wiersz[len(wiersz)-1]:
#         liczby.append(wiersz)
#
# print(len(liczby))
# print(liczby[0])

#4.2

def czynniki_pierwsze(a):
    czynniki_pierwsze = []
    k = 2
    while a>1:
        while a%k==0:
            czynniki_pierwsze.append(k)
            a //= k
        k += 1
    return czynniki_pierwsze

def czynniki_pierwsze_rozne(a):
    czynniki_pierwsze = []
    k = 2
    while a>1:
        while a%k==0:
            if k not in czynniki_pierwsze:
                czynniki_pierwsze.append(k)
            a //= k
        k += 1
    return czynniki_pierwsze

max_czynników = 0
max_liczba = 0
max_roznych_czynników = 0
max_liczba_roznych_czynników = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    czynniki = czynniki_pierwsze(int(wiersz))
    czynniki_rozne = czynniki_pierwsze_rozne(int(wiersz))

    if len(czynniki) > max_czynników:
        max_czynników = len(czynniki)
        max_liczba = wiersz
    if len(czynniki_rozne) > max_roznych_czynników:
        max_roznych_czynników = len(czynniki_rozne)
        max_liczba_roznych_czynników = wiersz

print(max_liczba,max_czynników)
print(max_liczba_roznych_czynników,max_roznych_czynników)


