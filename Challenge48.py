def dbl_linear(n):
    linear = [1]
    x = 0
    for num in range(0, n):
        x = linear[num]
        for time in range(2, 4):
            num = x*time +1
            if linear.count(num) >= 1:      # need to optimize the .sort() (doing one by yourself)
                pass
            else:
                linear.append(num)
        linear.sort()
    return linear[n]
    

print(dbl_linear(10))