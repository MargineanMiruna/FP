def check(l, x):
    for el in l:
        if type(el) == list:
            if check(el, x):
                return True
        else:
            if el == x:
                return True
    return False


print(check([1, [2, 4, 5], [[1,8], [4, 9]], 8], 9))