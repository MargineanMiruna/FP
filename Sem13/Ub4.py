def triplett(l, s):
    i = 0
    while l[i] < s:
        j = i + 1
        while l[j] < s:
            if s - l[i] - l[j] in l:
                return l[i], l[j], s - l[j] - l[i]
            j += 1
        i += 1


print(triplett([1, 5, 6, 8, 10], 12))