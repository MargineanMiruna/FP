def wiederh(l):
    for idx in range(0, len(l) - 2):
        idxx = idx + 1
        while idxx <= len(l) - 1:
            if l[idxx] == l[idx]:
                l.pop(idxx)
            else:
                idxx += 1
    return l


print(wiederh([12, 32, 12, 87, 12, 43]))