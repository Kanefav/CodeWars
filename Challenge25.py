def gap(g, m, n):
    #g (integer >= 2) which indicates the gap we are looking for
    #m (integer > 2) which gives the start of the search (m inclusive)
    #n (integer >= m) which gives the end of the search (n inclusive)
    primes = []
    diference = 0
    for prime in range(m, n+1):
        if is_prime(prime) == True:
            primes.append(prime)
    #print(primes)
    for num in range(len(primes)):
        if diference <= 0:
            diference = primes[num]
        else:
            diference -= primes[num]
            #print(primes[num], diference)
            if diference == -g:
                return [primes[num-1], primes[num]]
            else:
                diference = 0
                diference = primes[num]
        


def is_prime(num):
    if num % 2 == 0: return False
    for Num in range(3, 99, 2):
        if Num == num:
            pass
        elif num % Num == 0:
            return False
    return True
        
        
        


print(gap(2,3,5))