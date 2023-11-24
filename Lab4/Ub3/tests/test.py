from result.winner import win


def test_win():
    assert win('r', 'p') == 'c'
    assert win('s', 'p') == 'u'
    assert win('p', 'p') == 'n'
    