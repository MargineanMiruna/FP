#Ub4
def max_line_file(filename):
    f = open(filename, 'r')
    result = []
    for line in f:
        max_length = 0
        max_word = ''
        words = line.split(' ')

        for word in words:
            word = word.strip()
            if len(word) > max_length:
                max_word, max_length = word, len(word)

        result.append(max_length)
    f.close()
    return result


def test_max_line_file():
    assert max_line_file('data.txt') == [4, 4]


test_max_line_file()