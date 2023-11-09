def euclid(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def vielf(l, frm, to):
    v = 1
    for idx in range(frm, to + 1):
        v = v * l[idx] // euclid(v, l[idx])

    return v


print(vielf([12, 24, 48, 7, 3, 12, 9, 5, 11], 0, 2))