from math import sqrt


def decomp(n):
    output = ''
    fatorial = factorial(n)
    SaveFatorial = fatorial
    times = 0
    list = []
    for num in range(2, n+1):
        if prime(num) == True: list.append(num)
    for divisor in list:
        while fatorial % divisor == 0:
            print(fatorial, divisor)
            fatorial /= divisor
            times += 1
        if times == 1:
            output += f'{divisor} * '
        else:
            output += f'{divisor}^{times} * '
        fatorial = SaveFatorial
        times = 0
    output = output[0:-2]
    return output.strip()
            


def prime(n):
    if n == 2: return True
    if n % 2 == 0: return False
    for num in range(2, int(sqrt(n)+1)):
        if n % num == 0: return False
    return True


def factorial(n):
    output = n
    for num in range(n-1, 0, -1):
        output *= num
    return output


print(decomp(22))