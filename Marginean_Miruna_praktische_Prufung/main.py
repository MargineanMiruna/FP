def is_palindrom(s):
    return s.lower() == s[::-1].lower()


def count_palindromes(underage, filename):
    f = open(filename, 'r')
    lines = f.read().split('\n')
    people = list(map(lambda x: x.split(','), lines))
    pal = list(filter(lambda x: is_palindrom(x[0]), people))
    if underage is True:
        pal = list(filter(lambda x: int(x[1]) <= 18, pal))
    cnt = len(pal)
    return cnt


def test_count_palindromes():
    assert count_palindromes(True, 'people.txt') == 2
    assert count_palindromes(False, 'people.txt') == 6


test_count_palindromes()
print(count_palindromes(False, 'people.txt'))


class BinaryNumber:
    def __init__(self, zf):
        self.zf = zf
        self.listzif = list(zf)
        self.listzif = list(map(lambda x: int(x), self.listzif))

    def __str__(self):
        return self.zf

    def sum(self, other, return_list):
        sum = ''
        fl = 0
        if len(self.listzif) > len(other.listzif):
            other.listzif = [0] * (len(self.listzif) - len(other.listzif)) + other.listzif
        else:
            self.listzif = [0] * (len(other.listzif) - len(self.listzif)) + self.listzif
        for i, j in zip(self.listzif[::-1], other.listzif[::-1]):
            sum = str((i + j + fl) % 2) + sum
            fl = (i + j + fl) // 2
        if fl == 1:
            sum = str(fl) + sum
        if return_list is True:
            sum = list(sum)
            sum = list(map(lambda x: int(x), sum))
            return sum
        else:
            return sum


class RepoBinaryNumber:
    def __init__(self):
        self.listbin = []

    def add(self, bin: BinaryNumber):
        self.listbin.append(bin)

    def sum_all(self):
        strsum = '0'
        for bin in self.listbin:
            if bin.listzif[-1] == 1:
                sum = BinaryNumber(strsum)
                strsum = sum.sum(bin, return_list=False)
        return strsum


def main():
    binary_number1 = BinaryNumber('101')
    binary_number2 = BinaryNumber('1110')
    res_sum = binary_number1.sum(binary_number2, return_list=True)
    print(res_sum)
    res_sum = binary_number1.sum(binary_number2, return_list=False)
    print(res_sum)

    binary_number3 = BinaryNumber('10001')
    #binary_number4 = BinaryNumber('111')
    #binary_number5 = BinaryNumber('11')
    repo_binary_number = RepoBinaryNumber()
    repo_binary_number.add(binary_number1)
    repo_binary_number.add(binary_number2)
    repo_binary_number.add(binary_number3)
    #repo_binary_number.add(binary_number4)
    #repo_binary_number.add(binary_number5)
    print(repo_binary_number.sum_all())


main()