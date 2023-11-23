from choices.user import user_input
from choices.computer import computer_choice
from result.winner import win
from tests.test import test_win


def menu():
    print("""
    Rock - r
    Paper - p
    Scissors - s
    """)


def main():
    menu()
    user = input('Rock, Paper, Scissors? ')
    user_input(user)
    print('I chose this: ')
    comp = computer_choice()
    if win(user, comp) is None:
        main()
    else:
        print(win(user, comp))


test_win()
main()