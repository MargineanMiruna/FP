def fakultat(n):
    fak = 1
    for idx in range(2, n+1):
        fak *= idx
    return fak


print(fakultat(4))