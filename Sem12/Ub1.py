def sum_par(n):
    if n == 0:
        return 0

    if n % 2 == 0:
        return n % 10 + sum_par(n//10)
    else:
        return sum_par(n//10)


print(sum_par(123456))
