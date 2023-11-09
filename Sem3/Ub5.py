def word_exists(matrix, word):
    count = 0
    l = []
    for ch in word:
        for line in range(len(matrix)):
            for value in range(len(matrix[line])):
                if matrix[line][value] == ch:
                    l.append((line, value))
    for paar in range(len(l)-1):
        if l[paar][0] == l[paar + 1][0]:
            if l[paar][1] == l[paar + 1][1] + 1 or l[paar][1] == l[paar + 1][1] - 1:
                count += 1
        elif l[paar][0] == l[paar + 1][0] + 1 or l[paar][0] == l[paar + 1][0] - 1:
            if l[paar][1] == l[paar + 1][1]:
                count += 1
    if count == len(word) - 1:
        return True
    else:
        return False


print(word_exists([['A', 'B', 'C', 'D'], ['L', 'E', 'G', 'H'], ['Q', 'R', 'T', 'F']], 'ALERQ'))
