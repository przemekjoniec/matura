def f(x):
    if x == 0:
        return 0
    else:
        result =  f(x//2)
        return 2+result
#2.2
print(f(35))

#2.2
for i in range(256,511):
    print(f(i), i)