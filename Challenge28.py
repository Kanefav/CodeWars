def reverse_number(n):
    verf = False
    if n < 0:
        verf = True 
    output = ''
    n = str(n)
    for num in range(len(n), 0, -1):
        if n[num-1] == '-':
            continue
        output += n[num-1]
    if verf == True: return -int(output)
    else:
        return int(output)
        
        
print(reverse_number(-123))