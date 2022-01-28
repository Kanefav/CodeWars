from math import sqrt


def prime(n):
    list = []
    for eachnum in range(1, n+1):
        if isprime(eachnum) == True:
            list.append(eachnum)
    return list
               
        
def isprime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for divisor in range(2, int(sqrt(n)+1)):
        if n % divisor == 0: return False
    return True

                

print(prime(11))
