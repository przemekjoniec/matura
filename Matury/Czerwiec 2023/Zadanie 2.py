#2.2
plik1 = open('slowa1.txt','r')
plik2 = open('slowa2.txt','r')
plik3 = open('slowa3.txt','r')
wiersze1 = plik1.readlines()
wiersze2 = plik2.readlines()
wiersze3 = plik3.readlines()


def czy_mniejszy(n, s, k1, k2):
    i = k1
    j = k2
    while i <= n and j <= n:
        if s[i] == s[j]:
            i += 1
            j += 1
        else:
            if s[i] < s[j]:
                return "Tak"
            else:
                return "Nie"
    if (j <= n):
        return "Tak"
    else:
        return "Nie"

slowo1 = []
for wiersz in wiersze1:
    wiersz = wiersz.strip().split()
    slowo1.append(wiersz)

print(czy_mniejszy(int(slowo1[0][0])-1, slowo1[1][0], int(slowo1[2][0]), int(slowo1[2][1])))

slowo2 = []
for wiersz in wiersze2:
    wiersz = wiersz.strip().split()
    slowo2.append(wiersz)

print(czy_mniejszy(int(slowo2[0][0]) - 1, slowo2[1][0], int(slowo2[2][0]), int(slowo2[2][1])))

slowo3 = []
for wiersz in wiersze3:
    wiersz = wiersz.strip().split()
    slowo3.append(wiersz)

print(czy_mniejszy(int(slowo3[0][0])-1, slowo3[1][0], int(slowo3[2][0]), int(slowo3[2][1])))




