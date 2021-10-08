def square_digits(num):
    output = ''
    num = str(num)
    for valor in range(0, len(num)):
        elevado = int(num[valor])*int(num[valor])
        output += str(elevado)
    return int(output)


print(square_digits(9119))