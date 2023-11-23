from logic.solution import ersatz
from tests.test import test_ersatz


def main():
    wort = input('Wort zu ersetzten: ')
    ersatzwort = input('Ersatzwort: ')
    print(ersatz(wort, ersatzwort))


test_ersatz()
main()