def generate_multiple(num, length):
    l = []
    for i in range(1, length + 1):
        l.append(num*i)
    return l


print(generate_multiple(3, 4))