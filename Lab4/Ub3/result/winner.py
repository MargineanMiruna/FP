def win(user, comp):
    if user == comp:
        return 'n'
    elif user == 'r':
        if comp == 'p':
            return 'c'
        else:
            return 'u'
    elif user == 'p':
        if comp == 's':
            return 'c'
        else:
            return 'u'
    else:
        if comp == 'r':
            return 'c'
        else:
            return 'u'
