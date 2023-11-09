def versch(l):
    for idx in range(1, len(l)):
        l[idx] = l[idx] + l[0]

    return l


print(versch([24, 71, 44, 16, 95]))