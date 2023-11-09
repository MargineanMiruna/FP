def reverse(word):
    new_word = ''
    i = 0
    j = len(word) - 1
    while i < len(word)  and j >= 0:
        if word[i] not in 'aeiou':
            new_word += word[i]
            if i < len(word) - 2:
               i += 1
        if word[j] not in 'aeiou':
            j -= 1
        if word[i] in 'aeiou' and word[j] in 'aeiou':
            new_word += word[j]
            i += 1
            j -= 1
    return new_word


print(reverse('Terminator'))


def swap(word):
    vok = 'aeiou'
    voks = []
    for ch in word:
        if ch in vok:
            voks.append(ch)
    s = ''
    i = 1
    for ch in word:
        if ch not in vok:
            s += ch
        else:
            s += voks[-i]
            i += 1
    return s


def test_swap():
    assert swap('terminator') == 'tormaniter'


test_swap()
print(swap('terminator'))