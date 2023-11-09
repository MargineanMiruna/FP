from math import gcd


#Ub1
def add(a, b):
    return simplify((a[0] * b[1] + b[0] * a[1], a[1] * b[1]))


def test_add():
    assert add((1, 2), (2, 3)) == (7, 6)
    assert add((1, 2), (1, 2)) == (1, 1)


def sub(a, b):
    return simplify((a[0] * b[1] - a[1] * b[0], a[1] * b[1]))


def test_sub():
    assert sub((5, 2), (3, 4)) == (7, 4)
    assert sub((4, 3), (1, 4)) == (13, 12)


def mul(a, b):
    return simplify((a[0] * b[0], a[1] * b[1]))


def test_mul():
    assert mul((5, 2), (3, 4)) == (15, 8)
    assert mul((4, 3), (1, 4)) == (1, 3)


def div(a, b):
    return simplify((a[0] * b[1], a[1] * b[0]))


def test_div():
    assert div((5, 2), (3, 4)) == (10, 3)
    assert div((4, 3), (1, 4)) == (16, 3)


#Ub2
def simplify(frac):
    g = gcd(frac[0], frac[1])
    return frac[0]//g, frac[1]//g


def test_simplify():
    assert simplify((20, 12)) == (5, 3)


#Ub3
def add_frac(fracs, frac):
    fracs.append(frac)


def los_frac(fracs, frac):
    fracs.pop(frac)


def sum_fracs(fracs):
    sum = 0, 1
    for frac in fracs:
        sum = add(sum, frac)
    return sum


def test_sum():
    assert sum_fracs([(1, 2), (2, 3), (1, 2)]) == (5, 3)


#Ub4
def menu():
    return """
    1 - add frac
    2 - calculate sum
    3 - delete frac
    4 - exit
    """


def main():
    fracs = []
    while True:
        print(menu())

        opt = int(input('opt = '))
        if opt == 1:
            n = int(input('numarator = '))
            m = int(input('numitor = '))

            add_frac(fracs, (n, m))
        if opt == 2:
            n, m = sum_fracs(fracs)
            print('sum = ', (n, m))
        if opt == 3:
            idx = int(input('index = '))

            los_frac(fracs, idx)
            print(fracs)
        if opt == 4:
            break


test_simplify()
test_add()
test_sub()
test_mul()
test_div()
test_sum()
main()