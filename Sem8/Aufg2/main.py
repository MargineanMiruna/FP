def gem_elem(liste):
    dict_cnt = {}
    for l in liste:
        dict_loc = {}
        for el in l:
            if el in dict_loc:
                dict_loc[el] += 1
            else:
                dict_loc[el] = 1

        for el in dict_loc:
            if el in dict_cnt:
                dict_cnt[el] += 1
            else:
                dict_cnt[el] = 1

    k = []
    for key, value in dict_cnt.items():
        if value == len(liste):
            k.append(key)

    return k


print(gem_elem([[1, 1, 2, 3, 4], [4, 5, 1], [7, 8, 5, 1, 1, 4]]))
