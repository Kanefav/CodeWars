def calc(expr):
    if len(expr) == 0: return 0
    x = expr.split(' ')
    index = -1
    num = []
    for item in range(0, len(x)):
        if x[item] not in '+-*/':
            index += 1
            try:
                num.append(int(x[item]))
            except:
                num.append(float(x[item]))
        else:
            num1 = num[index-1]
            num2 = num[index]
            num.pop()
            num.pop()
            index -= 1
            if x[item] == '+':
                num.append(num1+num2)
            if x[item] == '-':
                num.append(num1-num2)
            if x[item] == '*':
                num.append(num1 * num2)
            if x[item] == '/':
                num.append(num1 / num2)
    return num[0]


print(calc('5 1 2 + 4 * + 3 -'))