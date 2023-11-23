def read():
    f = open('./meine_datei.txt', 'r')
    text = f.read()
    f.close()
    return text


def write(text):
    f = open('./meine_datei.txt', 'w')
    f.write(text)
    f.close()


def clear():
    f = open('./meine_datei.txt', 'a')
    f.seek(0)
    f.truncate()
    f.close()