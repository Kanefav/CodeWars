def valid_parentheses(string):
    v = 0
    for index in range(0, len(string)):
        if v < 0: return False
        if string[index] == '(': v += 1
        if string[index] == ')': v -= 1
    if v == 0: return True
        

print(valid_parentheses('())')) 