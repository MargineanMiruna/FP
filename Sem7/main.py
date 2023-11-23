from die import Die
from frac import Frac
from tests import test_count_color, test_auszahlen
from statistics import Statistics
from auto import Auto
from konto import Konto


def main():
    # d = Die(6)
    # r = d.roll()
    # while r != 6:
    #     print(f'rolled: {r}')
    #     r = d.roll()
    # print(f'rolled: {r}')

    # f1 = Frac(4, 12)
    # f1.reduce()
    # print(f'{f1.n}/{f1.m}')

    # s = Statistics()
    # autos = [Auto('m1', 'm2', 1800, 'red'),
    #          Auto('m1', 'm2', 1500, 'blue'),
    #          Auto('m1', 'm2', 1000, 'red')]
    # color = 'red'
    # print(f'#red autos = {s.count_color(autos, color)}')
    # print(f'avg year = {s.avg_year(autos, "m1")}')

    k1 = Konto('101A', 'Peter', 100)
    print(k1.betrag)
    k2 = Konto('101A', 'Peter')
    print(k2.betrag)


test_count_color()
test_auszahlen()
main()