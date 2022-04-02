from math import sqrt


def is_prime(num):
    if num <= 1:
        return False
    if num == 2: return True 
    for x in range(2, int(sqrt(num)+1)):
        if num % x == 0: return False
    return True


print(is_prime(6))