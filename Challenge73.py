def dig_pow(n, p):
    n2 = []
    for num in str(n):
        n2.append(pow(int(num), p))
        p += 1
    sumn2 = sum(n2)
    if sumn2 == n:
        return 1
    else:
        k = sumn2/n
        strk = str(k)
        v = strk.index('.')
        sliced = strk[v+1:]
        if sliced == '0':
            return int(k)
        else:
            return - 1
        
        
    
print(dig_pow(46288, 3))