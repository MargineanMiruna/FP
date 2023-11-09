#Ub1
def is_perfekt(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n


def sum_col(matrix):
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix)):
            sum += matrix[j][i]
        if not is_perfekt(sum):
            return False
    return True


def test_sum_col():
    assert sum_col(
        [[4, 3, 10],
         [1, 2, 10],
         [1, 1, 8]]
    ) == True
    assert sum_col(
        [[4, 3, 10],
         [3, 2, 10],
         [1, 1, 8]]
    ) == False


test_sum_col()