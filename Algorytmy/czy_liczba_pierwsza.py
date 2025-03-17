def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    pierwsza = int(n//2) + 1
    for dzielniki in range(3, pierwsza, 2):
        if n % dzielniki == 0:
            return False
    return True

print(czy_pierwsza(13))


# liczby_pierwsze = []
#
# for i in range(0,100):
#     if czy_pierwsza(i):
#         liczby_pierwsze.append(i)
#     else:
#         continue
#
# print(liczby_pierwsze)