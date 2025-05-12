import math
def nwd(a, b):
    if a % b == 0:
        return b
    else:
        return nwd(b, a % b)

print(nwd(12,16))
