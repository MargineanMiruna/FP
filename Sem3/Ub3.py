def big_sum(a, b):
    suma = ''
    i = len(a) - 1
    cf = 0
    while i >= 0:
        s = str((int(a[i]) + int(b[i])) % 10 + cf)
        suma = s + suma
        cf = 0
        if int(a[i]) + int(b[i]) > 9:
            cf = 1
        i -= 1
    if cf == 1:
        suma = '1' + suma
    return suma


print(big_sum('923', '129'))
