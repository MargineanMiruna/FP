def find(l, s, e):
    if s > e:
        return e + 1
    if l[s] != s:
        return s
    mid = (s + e) // 2
    if mid == l[mid]:
        return find(l, mid + 1, e)
    else:
        return find(l, s, mid)


l = [0, 1, 2, 3]
print(find(l, 0, len(l) - 1))