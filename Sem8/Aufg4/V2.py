"""
m = [[{1, 2}, {1}, {2, 5}],
     [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}],
     [{0, 1}, {7, 9}, {3, 4}]]
"""
m1 = [[{1, 2}, {1}, {2, 5}],
     [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}],
     [{0, 1}, {7, 9}, {3, 4}]]

m2 = [[{1, 4}, {1}, {2, 8}],
     [{1, 6, 3}, {3, 4, 5}, {5, 6, 3}],
     [{0, 1}, {7, 2}, {9, 4}]]


def sort_line(idx: int, matrix):
    return sorted(matrix[idx], key=lambda x: list(x)[2])


def sub_matrix(m1, m2):
    m3 = []
    for i in range(len(m1)):
        line = []
        for j in range(len(m1)):
            line.append(m1[i][j] - m2[i][j])
        m3.append(line)
    return m3


#print(sub_matrix(m1, m2))
print(sort_line(1, m1))