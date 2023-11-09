#Ub3
def schlange(matrix):
    for i in range(len(matrix)):
        if i % 2 == 0:
            for j in range(len(matrix) - 1):
                if matrix[i][j] <= matrix[i][j + 1]:
                    return False
        else:
            for j in range(-1, -len(matrix) + 1, -1):
                if matrix[i][j] >= matrix[i][j - 1]:
                    return False
    return True


def test_schlange():
    assert schlange(
        [[1, 2, 3],
        [6, 5, 4],
        [7, 8, 9]]
    ) == True


test_schlange()