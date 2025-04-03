
tab = [5, 3, 8, 2, 1, 7]

n = len(tab)
for i in range(n - 1):
    for j in range(n - i - 1):
        if tab[j] > tab[j + 1]:
            zmienna = tab[j]
            tab[j] = tab[j + 1]
            tab[j + 1] = zmienna

for element in tab:
    print(element, end=" ")