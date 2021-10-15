def order_weight(strng):
    strpesos = sorted(strng.split(' '))
    strpesos = sorted(strpesos, key=soma)
    output = ' '.join(strpesos)
    return output
    
    
def soma(x):
    total = 0
    for item in x:
        total = total + int(item)
    return total


print(order_weight("103 123 4444 99 2000"))
