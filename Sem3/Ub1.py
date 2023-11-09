#V1
def check_sum(numbers, sum):
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == sum:
                return True
    return False


print(check_sum([1, 2, 5, 3], 5))


#V2
def check_sum(numbers, sum):
    for number in numbers:
        if sum - number in numbers:
            return number, sum - number #tuple
    return None


print(check_sum([1, 2, 5, 3], 5))