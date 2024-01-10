import math


def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])


print(palindrom('123321'))


n = 5793
nc = int(math.log10(n)) + 1
print(n // (10 ** (nc - 1)))


def palindrom2(nr):
    if nr < 10:
        return True
    if nr // 10 ** int((math.log10(nr))) != nr % 10:
        return False
    return palindrom2(nr % 10 ** int(math.log10(nr)) // 10)


print(palindrom2(123321))