def diamond(n):
    if n <= 0:
        return None
    elif n % 2 == 0:
        return None
    else:
        cont = cont2 =  0
        metade = (n/2)-0.5
        metademenor = int(metade)
        string = ''
        diamond = '*'
        for d in range(0, n):
            if len(diamond*(d+1))%2 !=0:
                cont+= 1
                string += ' '*((metademenor+1)-cont) + f'{diamond*(d+1)}\n'
                dima = diamond*(d+1)
        for d2 in range(0, int(metade)):
            string += ' '*(d2+1) + f'{diamond*(len(dima)-(d2+d2+2))}\n'
        return string


print(diamond(31))