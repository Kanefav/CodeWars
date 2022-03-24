def two_sum(numbers, target):
    for num in numbers:
        for num2 in range(0, len(numbers)):
            if num + numbers[num2] == target and numbers.index(num) != num2:
                return [numbers.index(num), num2]


print(two_sum([2, 2, 3], 4))