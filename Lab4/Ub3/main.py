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
    rounds = 0
    w = 0
    while rounds != 3:
        menu()
        user = input('Rock, Paper, Scissors? ')
        user_input(user)
        print('I chose this: ')
        comp = computer_choice()
        s = win(user, comp)
        if s == 'n':
            print('Tie! Choose again: ')
        else:
            rounds += 1
            if s == 'u':
                w += 1
                print('You won!!!')
            elif s == 'c':
                print('You lost!')

    if w >= 2:
        print('User won the game!')
    else:
        print('Computer won the game:((')


test_win()
main()