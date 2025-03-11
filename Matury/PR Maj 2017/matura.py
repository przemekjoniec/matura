
plik = open('dane.txt','r')
wiersze = plik.readlines()

# #6.1
najjasniejszy = -1
najciemniejszy = 256

for wiersz in wiersze:
    wiersz = wiersz.strip().split(' ')
    for i in range(0, len(wiersz)):
        if int(wiersz[i]) > najjasniejszy:
            najjasniejszy = int(wiersz[i])
        if int(wiersz[i]) < najciemniejszy:
            najciemniejszy = int(wiersz[i])

print(najjasniejszy)
print(najciemniejszy)
#
# #6.2
ilosc = 0
for wiersz in wiersze:
    wiersz = wiersz.strip().split(' ')
    palindrom = wiersz[::-1]
    if wiersz != palindrom:
        ilosc += 1
print(ilosc)


plik.close()
