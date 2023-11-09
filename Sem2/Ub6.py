def count_to_dict_2(word):
    d={}

    for ch in word:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    return d


print(count_to_dict_2('maria'))
print(count_to_dict_2('arima'))


def anagramme(word1, word2):
    c1 = count_to_dict_2(word1)
    c2 = count_to_dict_2(word2)
    if c1 == c2:
        return True
    else:
        return False


# def anagrame_2(word1, word2):
#     aux = {}
#     for ch in word1:
#         aux[ch] += 1
#     for ch in word2:
#         aux[ch] += 1
#
#     for idx in aux:
#         if aux[idx] % 2 != 0:
#             return False
#     return True


print(anagramme('maria','arima'))
#print(anagrame_2('maria','arima'))

