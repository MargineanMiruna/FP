def sort_list(l1, l2):
    i, j = 0, 0
    l3 = []

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1

    l3 += l1[i:] + l2[j:]
    return l3


print(sort_list([1, 2, 3, 5], [2, 4, 5, 7]))
