from math import sqrt


def solve(a,b):
    FactorList = []
    PrimesList = []
    for num in range(1, b+1):
        if b % num == 0:
            FactorList.append(num)
    
    for num in FactorList:
        if prime(num) == True:
            PrimesList.append(num)

    for div in PrimesList:
        if a % div == 0:
            continue 
        else:
            return False
    return True


def prime(num):
    if num == 2: return True 
    if num % 2 == 0: return False
    for div in range(2, int(sqrt(num)+1)):
        if num % div == 0: return False 
    return True


print(solve(2, 256))