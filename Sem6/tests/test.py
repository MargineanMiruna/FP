from logik.hangman import guess


def test_guess():
    """
    MASINA

    state la start: (0, 0, [])

    choice = S: (0, 1, [2])
    choice = N: (0, 2, [2, 4])
    choice = X: (1, 2, [2, 4])
    """
    assert guess('Miruna', 'r', (0, 0, [])) == (0, 1, [2])
    assert guess('Miruna', 'u', (0, 1, [5])) == (0, 2, [5, 3])