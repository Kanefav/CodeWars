def digital_root(n):
    if len(str(n)) <= 1:
        return n
    else:
        strn = str(n)
        output = 0
        for x in range(0, len(strn)):
            output += int(strn[x])
        return digital_root(output)
            
    
    
print(digital_root(192))