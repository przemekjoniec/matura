plik = open('slowa.txt','r')
wiersze = plik.readlines()

licznik = 0
max_dl = 0
slowo_max_dl = ''
for wiersz in wiersze:
    wiersz = wiersz.strip()
    slowo_zakodowane = ''
    slowo_nie_zakodowane = wiersz
    for i in range(len(slowo_nie_zakodowane)):
        litera = ord(wiersz[i]) + 13
        if litera > 122:
            litera -= 26
            slowo_zakodowane += chr(litera)
        else:
            slowo_zakodowane += chr(litera)

    if slowo_zakodowane == slowo_nie_zakodowane[::-1]:
        licznik += 1
        if len(slowo_nie_zakodowane) > max_dl:
            max_dl = len(slowo_nie_zakodowane)
            slowo_max_dl = slowo_nie_zakodowane

print(licznik)
print(slowo_max_dl)