def count_to_dict(word):
    d={}

    for ch in word:
        cnt = 0
        for other_ch in word:
            if ch == other_ch:
                cnt += 1

        d[ch] = cnt

    return d


def count_to_dict_2(word):
    d={}

    for ch in word:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    return d


print(count_to_dict('sochool'))
print(count_to_dict_2('sochool'))