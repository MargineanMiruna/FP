from interactions.choices import Rock
from interactions.choices import Paper
from interactions.choices import Scissors


def user_input(choice):
    if choice == 's':
        Scissors()
    elif choice == 'r':
        Rock()
    else:
        Paper()