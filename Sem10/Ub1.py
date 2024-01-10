def prim(nr):
    for i in range(2, nr//2):
        if nr % i == 0:
            return False
        return True


def gen_matrix(wert, n):
    matrix = [[wert for _ in range(n)] for _ in range(n)]
    s = 0
    l_prime = [i for i in range(n * 6) if prim(i)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j > i:
                matrix[i][j] = s
                s += 2
            if i > j:
                matrix[i][j] = l_prime[-1]
                l_prime.pop()
    return matrix


def main():
    m = gen_matrix(7, 5)
    for line in m:
        print(line)


main()