def find_el(l, el):
    for i in range(1, len(l) - 1):
        if l[0 - i] == el:
            return len(l) - i


print(find_el([1, 7, 3, 2, 9, 3, 4, 3, 9], 3))