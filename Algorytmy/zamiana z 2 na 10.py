def na10(n):
    x = len(n) - 1
    sum = 0
    for cyfra in n:
        if cyfra == "1":
            sum += 1 * 2 ** x
        x -= 1
    return sum

print(na10("1001001001"))
