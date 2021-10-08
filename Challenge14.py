def max_sequence(arr):
    list = [0]
    for x in range(len(arr)):
        for num in range(x, len(arr)):
            list.append(sum(arr[x:num+1]))
    return max(list)
        

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

