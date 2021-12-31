def solution(n):
    nString = str(n)
    nString = nString.split('.')
    num = '1'
    for zero in range(0, len(nString[1])):
        num += '0'

    floats = int(nString[1]) / int(num)
            
    if floats <= 0.25-0.00000000001:
        return n - floats
    if floats >= 0.25 and floats <= 0.50:
        return n + (0.50 - floats)
    if floats >= 0.50 and floats <= 0.75-0.00000000001:
        return n + (0.50 - floats)
    if floats >= 0.75:
        return n + (1.0 - floats)
    
print(solution(4.74999999991))