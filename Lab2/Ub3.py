def konk(l):
    l = sorted(l, reverse= True)
    max = 0
    for nr in l:
        max = max * 100 + nr
    return max


print(konk([35, 65, 79, 12]))