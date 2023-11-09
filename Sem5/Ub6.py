#Ub6
def is_palindrom(word):
    return word == word[::-1]


def find_count(filename, word):
    f = open(filename, 'r')
    count = 0

    for line in f:
        words = line.split(' ')

        for w in words:
            if word == w.strip():
                count += 1

    f.close()
    return count


def count_pali(filename):
    f = open(filename, 'r')
    result = {}
    for line in f:
        words = line.split(' ')
        for word in words:
            if is_palindrom(word):
                 result[word] = find_count(filename, word.strip())
    f.close()
    return result


def test_count_pali():
    assert count_pali('data2.txt') == {'anna': 2, 'abbcbba': 1, 'abba': 2}


test_count_pali()