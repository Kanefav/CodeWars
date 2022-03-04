def modified_sum(a, n):
    output = 0
    for num in a:
        output += num**n
    return output - sum(a)
        


print(modified_sum([1, 2, 3], 3))