def array_diff(a, b):
    output = a
    for times in range(len(b)):
        for nums in a:
            if nums == b[times]:
                for num in range(len(a)):
                    try:
                        output.remove(nums)
                    except:
                        pass
    return output
            
    
    
print(array_diff([1,2,2], [1]))