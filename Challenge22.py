def get_score(n, first=True, add = 100, time=1):
    if first == True:
        if n > 995:
            output = 0
            for num in range(0, n+1):
                output += (50*num)
            return output
        else:
            time = n
            n = 50
            add = 100
    if first == False:
        add += 50
    while time != 1:
        time -= 1
        return get_score(n+add, False, add, time)
    return n
        

print(get_score(10))