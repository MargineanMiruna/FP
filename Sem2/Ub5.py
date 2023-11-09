def count_to_dict_2(word):
    d={}

    for ch in word:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    return d


def count_unique(word):
    counts = count_to_dict_2(word)
    cnt = 0

    for key in counts:
        if counts[key] == 1:
            cnt += 1
    return cnt


print(count_unique('school'))