plik = open('galerie.txt','r')
wiersze = plik.readlines()

#4.1
galerie = {}

for wiersz in wiersze:
    wiersz = wiersz.strip('').split()
    kraj = wiersz[0]
    if kraj not in galerie:
        galerie[kraj] = 0

for wiersz in wiersze:
    wiersz = wiersz.strip('').split()
    kraj = wiersz[0]
    if kraj in galerie:
        galerie[kraj] += 1

# print(galerie)

#4.2

# for wiersz in wiersze:
#     wiersz = wiersz.strip().split()
#     miasto = wiersz[1]
#     powierzchnia = 0
#     liczba_lokali = 0
#     for i in range(2,len(wiersz),2):
#         if wiersz[i] == '0':
#             break
#         liczba_lokali += 1
#         powierzchnia_lokalu = int(wiersz[i])*int(wiersz[i+1])
#         powierzchnia += powierzchnia_lokalu
#     print(f'{miasto}: {powierzchnia}, {liczba_lokali}')


#4.3
max_lokali = 0
min_lokali = 100
miasto_max = ''
miasto_min = ''
for wiersz in wiersze:
    wiersz = wiersz.strip().split()
    miasto = wiersz[1]
    lokale = {}
    for i in range(2,len(wiersz),2):
        if wiersz[i] == '0':
            break
        powierzchnia_lokalu = int(wiersz[i])*int(wiersz[i+1])
        if powierzchnia_lokalu not in lokale:
            lokale[powierzchnia_lokalu] = 0
        else:
            lokale[powierzchnia_lokalu] += 1

    if len(lokale) > max_lokali:
        max_lokali = len(lokale)
        miasto_max = miasto
    if len(lokale) < min_lokali:
        min_lokali = len(lokale)
        miasto_min = miasto

print(miasto_max,max_lokali)
print(miasto_min,min_lokali)










