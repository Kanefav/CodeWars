def get_larger_numbers(a, b):
    output = []
    for num in range(0, len(a)):
        if a[num] > b[num]: 
            output.append(a[num])
        else:
            output.append(b[num])
    return output


print(get_larger_numbers([13, 64, 15, 17, 88], [23, 14, 53, 17, 80]))