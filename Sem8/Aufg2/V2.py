import math


def read_list(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    l = []
    for line in lines:
        nr = 0
        nrs = line.strip().split(',')
        for i in nrs:
            nr = nr * 10 + int(i)
        l.append(nr)
    return l


def build(num):
    nc = int(math.log10(num)) + 1
    new = 0
    p = 1
    ogl = 0
    while num != 0:
        uc = num % 10
        num //= 10
        if nc % 3 == 0:
            ogl = ogl * 10 + uc
            new = uc * p + new
            p *= 10
        nc -= 1
    return new == ogl and new != 0


def transfer(filename, l):
    with open(filename, 'w') as file:
        for i in l:
            nr = i
            if build(nr) is True:
                file.write(str(i) + '\n')


print(read_list('input.txt'))
transfer('output.txt', read_list('input.txt'))