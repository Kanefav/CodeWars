from math import sqrt


def prime_factors (n):
    if n == 1: return []
    numprime = 2
    factors = []
    if n % 2 == 0:
        step = 0
    else:
        step = 1
    while True:
        try:
            if n % numprime == 0:
                factors.append(numprime)
                n = n / numprime
                if n == 1.0:
                    break
            else:
                numprime += 1
        except:
            factors.append(n)
            break
    for num in factors:
        if prime == False:
            factors.remove(num)
    return factors
    

def prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for num in range(2, int(sqrt(n)+1)):
        if n % num == 0: return False
    return True
            


print(prime_factors(1))
print(prime_factors(8))