plik = open('liczby.txt','r')
wiersze = plik.readlines()


liczbyPierwsze = wiersze[0].strip().split()
LiczbyCalkowite = wiersze[1].strip().split()

#2

# ile = 0
# for i in range(len(liczbyPierwsze)):
#     for j in range(len(LiczbyCalkowite)):
#         if int(LiczbyCalkowite[j]) % int(liczbyPierwsze[i]) == 0:
#             ile += 1
#             break
#
# print(ile)

#3

# liczbyPierwsze = list(map(int, wiersze[0].strip().split()))
# liczbyPierwsze = sorted(liczbyPierwsze, reverse=True)
# print(liczbyPierwsze)
# print(liczbyPierwsze[100])