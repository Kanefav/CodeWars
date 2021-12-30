import numpy


def lcm(*args):
    if args == ():
        return 1
    if 0 in args:
        return 0
    args = list(args)
    lista = []
    for num in args:
        for div in range(1, max(args)*2):
            lista.append(num*div)
    for num in lista:
        if lista.count(num) == len(args):
            return num
    #don't work 100% well, idk why 
    #return numpy.lcm.reduce(args)


print(lcm(56, 98))