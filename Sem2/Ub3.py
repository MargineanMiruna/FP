def palindrom(word):
    #word[0], word[-1], word[-2]...
    for idx in range(len(word)//2):
        if word[idx] != word[-(idx+1)]:
            return False

    return True


print(palindrom('anna'))
print(palindrom('aba'))
print(palindrom('sjbv'))

word='anna'
print(word[::-1] == word)