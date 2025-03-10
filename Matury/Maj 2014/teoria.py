#1a
d = 1
n = 81
while d < n:
    if n % d == 0:
        print(d)
    d = d + 1

#1b

d = 1
n = 81
while d <= n/2:
    if n % d == 0:
        print(d)
    d = d + 1

#1c
#do zrobienia

#2a nie działa ale taki jest pseudokod wiec elo pozdro cke

i = 1
n = 8
a = [ 21, 1, 56, 90, 8, 8, 19, 47 ]
while i < n - 1:
    if a[i] > a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]
    i = i + 2
print(a) #[45, 7, 12, 20, 39, 1]
