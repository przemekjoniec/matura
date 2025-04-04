plik = open('prostokaty.txt','r')
wiersze = plik.readlines()

#1
# pole_min = 907217688
# pole_max = 907217688
#
# for wiersz in wiersze:
#     wiersz = wiersz.strip().split(' ')
#     h = int(wiersz[0])
#     s = int(wiersz[1])
#     pole_obecne = h * s
#     if pole_obecne < pole_min:
#         pole_min = pole_obecne
#     if pole_obecne > pole_max:
#         pole_max = pole_obecne
#
# print(pole_min, pole_max)

#2
maks_dlugosc = 1
obecna_dlugosc = 1
ostatni_prostokat = None
for i in range(1, len(wiersze)-1):

    wiersz_obecny = wiersze[i].strip().split(' ')
    wiersz_poprzedni = wiersze[i-1].strip().split(' ')

    s = int(wiersz_obecny[0])
    h = int(wiersz_obecny[1])
    sp = int(wiersz_poprzedni[0])
    hp = int(wiersz_poprzedni[1])

    if s <= sp and h <= hp:
        obecna_dlugosc += 1
        if obecna_dlugosc > maks_dlugosc:
            maks_dlugosc = obecna_dlugosc
            ostatni_prostokat = (s, h)
    else:
        obecna_dlugosc = 1


print(maks_dlugosc)
print(ostatni_prostokat)
