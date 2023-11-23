def response(ct, wort, ersatzwort):
    if ct == 0:
        return 'Das Wort kommt in dem Text nicht vor und konnte nicht ersetzt werden.'
    else:
        return f'Ersetzt {wort} durch {ersatzwort} an {str(ct)} Stellen.'