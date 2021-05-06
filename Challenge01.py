# return masked string
def maskify(cc):
    if len(cc) <= 4:
        return cc
    censura = ''
    for i in range(0, len(cc)):
        if i >= len(cc)-4:
            censura += cc[i]
        else:
            censura += '#'
        
    return censura


print(maskify('dadadadadasdwadsas'))