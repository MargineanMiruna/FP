#a
def primz (n):
    l = []
    for idx in range(n):
        ok = 1
        if idx <= 1:
            ok = 0
        elif idx % 2 == 0 and idx != 2: #Paarzahltest ohne 2
            ok = 0
        else:
            for idxx in range(3,idx//2,2): #sucht Divisoren
                if idx % idxx == 0:
                    ok = 0
        if ok == 1:
            l.append(idx)

    return l


print(primz(22))


#b
def teilf(l):
    s = 0
    d = 0
    smax = 0
    dmax = 0
    x = 0
    ct = 0
    for nr in l:
        ct += 1
        if nr > x:
            d = ct  # capatul drept creste
        else:
            s = ct - 1  # incepe sir nou
        x = nr
        if (d - s) > (dmax - smax):  # daca sirul nou e mai lung se schimba capetele
            smax = s
            dmax = d
    return l[smax:dmax]  # returneaza elementele dintre cele doua capete


print(teilf([1, 2, 3, 2, 6, 9, 10, 5, 7]))
