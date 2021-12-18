def prime_factors (n):
    if n == 1: return []
    numprime = 2
    factors = []
    while True:
        if n % numprime == 0:
            factors.append(numprime)
            n = n / numprime
            if n == 1.0:
                return factors
        else:
            numprime += 1


print(prime_factors(12))
print(prime_factors(3))