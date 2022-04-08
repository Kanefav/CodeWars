def pattern(n):
    output = '1\n'
    for time in range(2, n+1):
        ast = '*' * (time-1)
        output += f'1{ast}{time}\n'
    return output[:-1]


print(pattern(4))