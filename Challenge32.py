def factorial(n):
    if n == 0: return 1
    output = n
    for num in range(n-1, 0, -1):
        output *= num
    return output
        
    
print(factorial(5))