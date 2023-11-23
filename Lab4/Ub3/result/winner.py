def win(user, comp, debug=False):
    if user == comp:
        if debug is False:
            print('Tie! Choose again: ')
        return None
    elif user == 'r':
        if comp == 'p':
            return 'You lost!'
        else:
            return 'You won!!!'
    elif user == 'p':
        if comp == 's':
            return 'You lost!'
        else:
            return 'You won!!!'
    else:
        if comp == 'r':
            return 'You lost!'
        else:
            return 'You won!!!'
