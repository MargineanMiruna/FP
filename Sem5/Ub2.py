#Ub2
def sum_diag(matrix):
    result = []
    for i in range(len(matrix)):
        sum_linie = 0
        for j in range(len(matrix[i])):
            if i != j:
                sum_linie += matrix[i][j]
        result.append(sum_linie == matrix[i][i])
        # if sum_linie == matrix[i][i]:
        #     result.append(True)
        # else:
        #     result.append(False)
    return result


def test_sum_diag():
    assert sum_diag(
        [[4, 3, 1],
         [1, 2, 1],
         [0, 5, 1]]
    ) == [True, True, False]

    assert sum_diag(
        [[1, 2, 3],
         [1, 2, 1],
         [0, 4, 0]]
    ) == [False, True, False]


test_sum_diag()