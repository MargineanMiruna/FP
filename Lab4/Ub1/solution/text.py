import turtle


def add_to_switcher(text, switcher1, switcher2):
    lines = text.strip().split()
    ct = 0
    for line in lines:
        ct += 1
        comm = []
        for char in line:
            comm.append(switcher2[char])
        switcher1[str(ct)] = comm


def text_to_screen(t, switcher1, word):
    for ch in word:
        if ch.islower() is False:
            comm = switcher1[ch]
            for c in comm:
                c(t)
        else:
            switcher1[ch](t)
        t.up()
        t.goto(t.xcor() + 15, 0)
        t.setheading(0)
        t.down()
    turtle.done()


def new_char(t, switcher2):
    key = input()
    des = ''
    while key != '':
        des += key
        turtle.onkey(switcher2[key](t), key)
        turtle.listen()
        key = input()
    turtle.done()
    return des
