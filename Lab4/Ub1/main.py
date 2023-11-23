from solution.text import add_to_switcher
from solution.text import text_to_screen
from solution.text import new_char
from keyboard.alphabet import *
from keyboard.commands import *
import turtle


def menu():
    print(
        """
        1. Textnachricht zeichnen
        2. Neues Zeichen
        """
    )


def main():
    menu()
    t = turtle.Pen()
    t.pensize(7)
    t.pencolor('black')
    t.up()
    t.goto(-330, 0)
    t.down()
    switcher1 = {
        'A': a, 'a': a,
        'B': b, 'b': b,
        'C': c, 'c': c,
        'D': d, 'd': d,
        'E': e, 'e': e,
        'F': f, 'f': f,
        'G': g, 'g': g,
        'H': h, 'h': h,
        'I': i, 'i': i,
        'J': j, 'j': j,
        'K': k, 'k': k,
        'L': l, 'l': l,
        'M': m, 'm': m,
        'N': n, 'n': n,
        'O': o, 'o': o,
        'P': p, 'p': p,
        'Q': q, 'q': q,
        'R': r, 'r': r,
        'S': s, 's': s,
        'T': tt, 't': tt,
        'U': u, 'u': u,
        'V': v, 'v': v,
        'W': w, 'w': w,
        'X': x, 'x': x,
        'Y': y, 'y': y,
        'Z': z, 'z': z,
        '.': dot,
        '?': questionmark,
        '!': exclamation
    }
    switcher2 = {
        'w': W,
        'a': A,
        's': S,
        'd': D,
        'f': F,
        'g': G
    }
    opt = int(input('Option: '))
    if opt == 1:
        word = input('Type in a word: ')
        file = open('characters.txt', 'r')
        text = file.read()
        file.close()
        add_to_switcher(text, switcher1, switcher2)
        text_to_screen(t, switcher1, word)
    elif opt == 2:
        file = open('characters.txt', 'a')
        des = new_char(t, switcher2)
        file.write(des + '\n')
        file.close()


main()