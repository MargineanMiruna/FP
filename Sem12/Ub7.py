def sl(l):
    s = 0
    for el in l:
        if type(el) == list:
            s += sl(el)
        else:
            s += el
    return s


print(sl([[1, 3, 6], 5, [[1, 6], [4, 9, 3]]]))
