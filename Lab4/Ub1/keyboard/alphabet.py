def a(t):
    t.left(70)
    t.forward(70)
    t.right(140)
    t.forward(70)
    t.up()
    t.right(140)
    t.forward(42)
    t.down()
    t.right(150)
    t.forward(28)
    t.up()
    t.forward(9)
    t.down()


def b(t):
    t.left(90)
    t.forward(68)
    t.right(90)
    for i in range(2):
        t.forward(13)
        t.circle(-17, 180)
        t.forward(13)
        t.right(180)
    t.up()
    t.forward(30)
    t.down()


def c(t):
    t.up()
    t.forward(45)
    t.left(90)
    t.forward(18)
    t.down()
    t.left(180)
    t.circle(-20, 180)
    t.forward(32)
    t.circle(-20, 180)


def d(t):
    t.left(90)
    t.forward(68)
    t.right(90)
    t.forward(5)
    t.circle(-34, 180)
    t.forward(5)
    t.up()
    t.backward(38)
    t.down()


def e(t):
    t.left(90)
    t.forward(68)
    t.right(90)
    for i in range(3):
        t.forward(30)
        if i != 2:
            t.up()
            t.goto(t.xcor() - 30, t.ycor() - 34)
            t.down()


def f(t):
    t.left(90)
    t.forward(68)
    t.right(90)
    for i in range(2):
        t.forward(30)
        if i != 1:
            t.up()
            t.goto(t.xcor() - 30, t.ycor() - 34)
            t.down()


def g(t):
    t.up()
    t.forward(25)
    t.left(90)
    t.forward(28)
    t.down()
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.circle(-20, 180)
    t.forward(32)
    t.circle(-20, 180)


def h(t):
    t.left(90)
    for i in range(2):
        t.forward(68)
        t.up()
        t.goto(t.xcor() + 35, t.ycor() - 68)
        t.down()
    t.up()
    t.goto(t.xcor() - 70, t.ycor() + 34)
    t.down()
    t.right(90)
    t.forward(35)


def i(t):
    t.left(90)
    t.forward(68)


def j(t):
    t.right(60)
    t.circle(10, 150)
    t.forward(63)


def k(t):
    t.left(90)
    t.forward(68)
    t.up()
    t.goto(t.xcor(), t.ycor() - 40)
    t.down()
    t.right(40)
    t.forward(52)
    t.up()
    t.goto(t.xcor() - 25, t.ycor() - 29)
    t.down()
    t.right(103)
    t.forward(47)


def l(t):
    t.left(90)
    t.up()
    t.forward(68)
    t.down()
    t.right(180)
    t.forward(68)
    t.left(90)
    t.forward(40)


def m(t):
    t.left(90)
    t.forward(68)
    t.right(145)
    t.forward(45)
    t.left(110)
    t.forward(45)
    t.right(145)
    t.forward(68)


def n(t):
    t.left(90)
    t.forward(68)
    t.right(145)
    t.forward(80)
    t.left(145)
    t.forward(68)


def o(t):
    t.up()
    t.left(90)
    t.forward(20)
    t.down()
    t.forward(30)
    t.circle(-20, 180)
    t.forward(30)
    t.circle(-20, 180)
    t.up()
    t.right(90)
    t.forward(45)
    t.down()


def p(t):
    t.left(90)
    t.forward(68)
    t.right(90)
    t.forward(13)
    t.circle(-17, 180)
    t.forward(13)
    t.up()
    t.backward(30)
    t.down()


def q(t):
    t.up()
    t.left(90)
    t.forward(20)
    t.down()
    t.forward(30)
    t.circle(-20, 180)
    t.forward(30)
    t.circle(-20, 180)
    t.up()
    t.goto(t.xcor() + 27, t.ycor())
    t.down()
    t.right(135)
    t.forward(25)


def r(t):
    t.left(90)
    t.forward(68)
    t.right(90)
    t.forward(13)
    t.circle(-17, 180)
    t.forward(13)
    t.backward(13)
    t.left(120)
    t.forward(38)


def s(t):
    t.left(90)
    t.up()
    t.forward(7)
    t.down()
    t.right(150)
    t.circle(17, 225)
    t.forward(10)
    t.circle(-17, 225)


def tt(t):
    t.up()
    t.forward(25)
    t.down()
    t.left(90)
    t.forward(68)
    t.left(90)
    t.forward(25)
    t.backward(50)


def u(t):
    t.left(90)
    t.up()
    t.forward(68)
    t.down()
    t.left(180)
    t.forward(48)
    t.circle(20, 180)
    t.forward(50)


def v(t):
    t.left(90)
    t.up()
    t.forward(68)
    t.down()
    t.right(160)
    t.forward(70)
    t.left(140)
    t.forward(70)


def w(t):
    t.left(90)
    t.up()
    t.forward(68)
    t.down()
    t.right(160)
    t.forward(70)
    t.left(140)
    t.forward(40)
    t.right(140)
    t.forward(40)
    t.left(140)
    t.forward(70)


def x(t):
    t.left(60)
    t.forward(77)
    t.left(120)
    t.up()
    t.forward(38)
    t.down()
    t.left(120)
    t.forward(77)


def y(t):
    t.left(90)
    t.up()
    t.forward(68)
    t.down()
    t.right(140)
    t.forward(40)
    t.left(100)
    t.forward(40)
    t.backward(40)
    t.right(140)
    t.forward(37)
    t.left(90)
    t.up()
    t.forward(30)
    t.down()


def z(t):
    t.left(90)
    t.up()
    t.forward(68)
    t.down()
    t.right(90)
    t.forward(45)
    t.right(125)
    t.forward(80)
    t.left(125)
    t.forward(45)


def dot(t):
    t.left(90)
    t.forward(3)


def questionmark(t):
    t.left(90)
    t.up()
    t.forward(60)
    t.down()
    t.right(30)
    t.circle(-17, 240)
    t.left(90)
    t.forward(17)
    t.up()
    t.forward(15)
    t.down()
    t.forward(3)


def exclamation(t):
    t.left(90)
    t.forward(3)
    t.up()
    t.forward(15)
    t.down()
    t.forward(50)