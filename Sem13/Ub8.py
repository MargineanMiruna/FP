def get_column(i, N, m):
    if len(m) != N*N:
        raise ValueError('Nicht quadratisch')
    col = []
    for pos, el in enumerate(m):
        if pos % N == i:
            col.append(el)
    return col


def test():
    assert get_column(0, 3, '012345678') == ['0', '3', '6']
    assert get_column(1, 3, '012345678') == ['1', '4', '7']
    assert get_column(2, 3, '012345678') == ['0', '5', '8']


test()
print(get_column(0, 4, '7842091363327845'))
