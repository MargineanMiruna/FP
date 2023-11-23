from result.winner import win


def test_win():
    assert win('r', 'p', debug=True) == 'You lost!'
    assert win('s', 'p', debug=True) == 'You won!!!'
    assert win('p', 'p', debug=True) is None
    