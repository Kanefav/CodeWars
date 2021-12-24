from math import sqrt
from numpy import power


def compare_powers(n1,n2):
    if n1[0] == 1: 
        if n2[0] == 1: return 0
        return 1
    if n1 == n2: return 0
    if power(sqrt(n1[0]), n1[1]/10) > power(sqrt(n2[0]), n2[1]/10): return -1
    return 1
        

print(compare_powers([3,9],[5,6]))