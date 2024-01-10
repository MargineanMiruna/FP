def mx(l):
    if len(l) == 0:
        return None
    if len(l) == 1:
        return l[0]
    return max(l[0], mx(l[1:]))


print(mx([4, 7, 12, 9, 6]))
