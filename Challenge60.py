from math import sqrt


def is_twinprime(n):
    if is_prime(n) == False: return False
    if is_prime(n-2) == True or is_prime(n+2) == True: return True
    return False


def is_prime(n):
    if n == 2: return True 
    if n % 2 == 0: return False
    for num in range(2, int(sqrt(n)+1)):
        if n % num == 0: return False
    return True


print(is_twinprime(768199))