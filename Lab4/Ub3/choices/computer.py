from interactions.choices import Rock
from interactions.choices import Paper
from interactions.choices import Scissors
import random


def computer_choice():
    l = ['r', 'p', 's']
    choice = random.choice(l)
    if choice == 'r':
        Rock()
    elif choice == 'p':
        Paper()
    else:
        Scissors()
    return choice