def sym(l):
    ct = 0
    for idx in range(0, len(l) - 1):
        for idxx in range(idx + 1, len(l) - 1):
            if l[idx] == l[idxx] % 10 * 10 + l[idxx] // 10:
                ct += 1
    return ct


print(sym([12, 32, 21, 87, 23, 12]))