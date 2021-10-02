def fibonacci(n, m=dict()):
    if n <= 2:
        return 1
    try:
        return m[n]
    except:
        pass
    output = 0
    n1 = 0
    n2 = 1
    for c in range(0, n-1):
        output = n1 + n2
        n1 = n2 
        n2 = output
    m[n] = output
    return output
        

print(fibonacci(100))
print(fibonacci(100))
print(fibonacci(100))
print(fibonacci(100))


