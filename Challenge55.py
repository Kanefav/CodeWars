def calculator(txt):
    sliced = txt.split(' ')
    #plus
    if sliced[1] == '+':
        return f'{sliced[0]}{sliced[2]}'
    #less
    if sliced[1] == '-':
        if sliced[0] > sliced[2]:
            less_limit = len(sliced[0]) - len(sliced[2])
            return sliced[0][:less_limit]
        else:
            less_limit = len(sliced[2]) - len(sliced[0])
            return sliced[2][:less_limit]
    #times
    if sliced[1] == '*':
        times = len(sliced[2])
        return sliced[0]*times
    #divison
    if sliced[1] == '//':
        divide = len(sliced[0]) // len(sliced[2])
        return sliced[0][:divide]


print(calculator('..... // ..'))