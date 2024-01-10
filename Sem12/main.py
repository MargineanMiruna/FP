def sum_rec(l, i):
    if i < len(l):
        return l[i] + sum_rec(l, i + 1)
    else:
        return 0


print(sum_rec([1, 2, 3, 4, 5], 0))


def sum_rec2(l):
    if len(l) <= 1:
        return l[0]
    return l[0] + sum_rec2(l[1:])


print(sum_rec2([1, 2, 3, 4, 5]))


def sum_rec3(l):
    if len(l) <= 1:
        return l[0]
    return l[-1] + sum_rec3(l[:-1])


print(sum_rec3([1, 2, 3, 4, 5]))