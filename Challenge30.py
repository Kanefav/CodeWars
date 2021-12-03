from math import sqrt


def solve(n):
    if prime(n) == True: return n
    primeless = primeMore = n
    while True:
        primeless -= 1
        primeMore += 1
        if prime(primeless) == True: return primeless
        if prime(primeMore) == True: return primeMore
        

def prime(n):
    if n == 2: return True
    if n % 2 == 0: return False
    for num in range(2, int(sqrt(n))):
        if n % num == 0: return False
    return True


print(solve(10000000000))
