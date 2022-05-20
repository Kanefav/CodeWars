from numpy import sort


def min_permutation(n):
    nlist = list(str(n))
    z = nlist.count('0')
    nlist = sort(nlist)
    
    if len(nlist) >= 2:
        if z >= 1:
            problem = 0 # '-' first char
            if nlist[0] == '-': problem = 1
            for zero in range(problem, z+problem):
                nlist[zero] = nlist[z+problem]
                nlist[z+problem] = 0
    x = ''.join(nlist)
    return int(x)


print(min_permutation(-2300041))
