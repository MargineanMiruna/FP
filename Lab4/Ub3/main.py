import random

def Rock():
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)


def Paper():
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)


def Scissors():
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)


def random_choice():
    l = [Rock(), Paper(), Scissors()]
    return random_choice(l)


def main():
    wahl = input('Schere, Stein oder Papier? ')
    if wahl == 'Schere':
        Scissors()
    elif wahl == 'Stein':
        Rock()
    else:
        Paper()

    print('Ich habe das gewahlt: ')
    random_choice()


main()