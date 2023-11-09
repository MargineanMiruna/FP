#a
def rel_prim(n):
    l = []
    for idx in range(2,n):
        ok = 1
        for idxx in range(2, max(idx,n)):
            if idx % idxx == 0 and n % idxx == 0: #cauta divizori comuni
                ok = 0
        if ok == 1:
            l.append(idx)
    return l


print(rel_prim(16))


#b
def max_sum(l):
    sum = 0
    summax = 0
    smax = 0
    dmax = 0
    s = 0
    d = 0
    ct = 0
    for nr in l:
        ct += 1
        if (sum + nr) > 0:
            sum += nr
            d = ct
        else:
            s = ct
            sum = 0
        if summax < sum:
            summax = sum
            smax = s
            dmax = d
    return l[smax:dmax]


print(max_sum([3, -9, 7, -2, 1, 3, 3]))

