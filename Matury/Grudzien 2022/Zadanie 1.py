plik = open('mecz.txt','r')
wiersze = plik.readline()
wiersze = wiersze.strip()

#1.1
licznik = 0
for i in range(len(wiersze)-1):
    if wiersze[i] != wiersze[i+1]:
        licznik += 1

print(licznik)

#1.2
wynik_a = 0
wynik_b = 0
for i in range(len(wiersze)):
    if wiersze[i] == 'A':
        wynik_a += 1
    if wiersze[i] == 'B':
        wynik_b += 1
    if wynik_a >= 1000 and wynik_a - 3 >= wynik_b:
        print(f'A, {wynik_a}:{wynik_b}')
        break
    elif wynik_b >= 1000 and wynik_b - 3 >= wynik_a:
        print(f'B, {wynik_a}:{wynik_b}')
        break

#1.3
max_passa = 0
druzyna_max = ' '
ile_pass = 0

obecna_passa = 1
obecna_druzyna = wiersze[0]
for i in range(len(wiersze)):
    if wiersze[i] == obecna_druzyna:
        obecna_passa += 1
    else:
        if obecna_passa >= 10:
            ile_pass += 1
            if obecna_passa > max_passa:
                max_passa = obecna_passa
                druzyna_max = obecna_druzyna
        obecna_druzyna = wiersze[i]
        obecna_passa = 1

print(max_passa, druzyna_max, ile_pass)


