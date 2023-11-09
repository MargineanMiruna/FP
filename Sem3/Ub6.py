def big_sum(a, b):
    suma = ''
    i = min(len(a), len(b)) - 1
    j = max(len(a), len(b)) - 1
    d = str(min(int(a), int(b)))
    c = str(max(int(a), int(b)))
    cf = 0
    while i >= 0:
        s = str((int(c[j]) + int(d[i])) % 10 + cf)
        suma = s + suma
        cf = 0
        if int(c[j]) + int(d[i]) > 9:
            cf = 1
        i -= 1
        j -= 1
    while j >= 0:
        s = str((int(c[j]) + cf) % 10)
        suma = s + suma
        if int(c[j]) + cf > 9:
            cf = 1
        else:
            cf = 0
        j -= 1
    if cf == 1:
        suma = '1' + suma
    return suma


print(big_sum('999999', '23'))
