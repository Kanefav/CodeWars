def divisors(num):
    NumD = []
    for divisores in range(2, 100001):
        if num % divisores == 0:
            NumD.append(divisores)
    if num in NumD:
        NumD.remove(num)
    if len(NumD) == 0:
        return f'{num} is prime'
    return NumD


print(divisors(253))