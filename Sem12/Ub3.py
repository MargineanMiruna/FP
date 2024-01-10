def voc(s):
    if len(s) == 0:
        return 0
    if s[0] in 'aeiouAEIOU':
        return 1 + voc(s[1:])
    else:
        return voc(s[1:])


print(voc('mamamiaoo'))