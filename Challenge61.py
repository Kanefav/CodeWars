def dont_give_me_five(start, end):
    r = start + end
    fives = 0
    if end > 100:
        rstr = str(r)
        zeros = len(rstr[1:])
        cent = '1' + '0' * zeros
        times_fives = 1
        if cent >= '1000':
            times_fives = cent[:-2]
        print(zeros, cent, times_fives)
        while r > 0:
            if r - int(cent) > 0:
                r -= int(cent)
                fives += 18 * int(times_fives)
            else:
                break
    for num in range(0, r):
        if '5' in str(num):
            fives += 1
    num = end-start
    return num - fives +1
    
    
print(dont_give_me_five(0, 100))