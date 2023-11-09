def domino(l):
    s = 0
    d = 0
    smax = 0
    dmax = 0
    ct = 0
    x = -1
    for nr in l:
        if ct > 0:
            if nr // 10 == x % 10:
                d = ct
            else:
                s = ct
        ct += 1
        x = nr
        if dmax - smax < d - s:
            smax = s
            dmax = d

    return l[smax:dmax+1]


print(domino([89, 95, 54, 43, 66, 61, 12, 90]))