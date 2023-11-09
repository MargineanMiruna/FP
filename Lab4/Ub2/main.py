def ersetzt(wort, ersatz):
    f = open('../meine_datei.txt', 'r+')
    ct = 0
    text = f.read()
    f.seek(0)
    f.truncate()
    new_text = ''
    words = text.split(' ')
    for word in words:
        if word == wort:
            ct += 1
            new_text = new_text + ersatz + ' '
        else:
            new_text = new_text + word + ' '
    f.write(new_text)
    f.close()

    if ct == 0:
        print('Das Wort kommt in dem Text nicht vor und konnte nicht ersetzt werden.')
    else:
        print('Ersetzt ' + wort + ' durch ' + ersatz + ' an ' + str(ct) + ' Stellen.')


def main():
    wort = input('Wort zu ersetzten: ')
    ersatz = input('Ersatzwort: ')
    ersetzt(wort, ersatz)


main()