def solution(number):
    numbers = []
    MaiorQzero = False
    while number > 0:
        MaiorQzero = True
        number -= 1
        if number % 5 == 0 or number % 3 == 0:
            numbers.append(number)
    if MaiorQzero == True:
        return sum(numbers)
    else:
        return 0


print(solution(20))