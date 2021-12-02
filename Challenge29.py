def solution(number):
    soma = 0
    for num in range(0, number):
        if num % 3 == 0 or num % 5 == 0: soma += num
    return soma


print(solution(1000))