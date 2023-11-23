from interactions.with_file import read
from interactions.with_file import write
from interactions.with_keyboard import response


def ersatz(wort, ersatzwort, debug=False):
    text = read()
    ct = 0
    lines = text.split('\n')
    new_text = ''

    for line in lines:
        words = line.split(' ')
        for word in words:
            word = word.strip()
            if word == wort:
                ct += 1
                new_text = new_text + ersatzwort + ' '
            else:
                new_text = new_text + word + ' '

        new_text += '\n'

    if debug is False:
        write(new_text)

    return response(ct, wort, ersatzwort)
