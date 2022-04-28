def transpose(matrix):
    lists = []
    num = len(matrix)
    for index in range(1, num+1):
        for m in matrix:
            for item in range(index-1, index):
                lists.append(m[item])
    
    output = []
    for list in range(1, num+1):
        x = num*list
        output.append(lists[x-num:num*list])
    return output
        
            # not fitting w/ lenght


print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))