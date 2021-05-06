def xo(s):
    s = s.upper()
    count = count2 = 0
    for i in range(0, len(s)):
        if s[i].find('X'):
            count += 1
        if s[i].find('O'):
            count2 += 1
    if count == count2:
        return True
    else:
        return False


a = str(input('Write many letters: '))
if xo(a) == True:
    print('Yeah hehe')
else:
    print('1-1')