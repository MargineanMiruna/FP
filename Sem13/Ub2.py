def rec_sort(l):
    if len(l) == 0:
        return []

    if l[0] == 0:
        return [0] + rec_sort(l[1:])
    else:
        return rec_sort(l[1:]) + [1]


print(rec_sort([0, 1, 1, 0, 0, 0, 1, 0, 1, 1]))