def halving_sum(n):
    n_start = n
    start = 2
    output = n
    while n > 1:
        n = int(n_start / start)
        output += n 
        start *= 2
    return output
        
    
print(halving_sum(25))