def parts_sums(ls):
    currentlySum = 0
    output = [0]
    for index in range(len(ls)-1, -1, -1):
        currentlySum += ls[index]
        output.append(currentlySum)
    output.reverse()
    return output
    
    
print(parts_sums([0, 1, 3, 6, 10]))