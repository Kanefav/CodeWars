def spiral_sum(size):
    rsize = size
    outsize = size*size
    soma = 0
    for notwhite in range(1, size-1):
        if notwhite == 1:
            size -= notwhite
            soma += size
        elif notwhite % 2 == 0:
            size -= 2
            soma += size
        else:
            soma += size
    if rsize < 10:
        return outsize - soma
    else:
        return outsize - soma-1




print(spiral_sum(123456))