def sum_str(a, b):
    if len(a) <= 0 and len(b) <= 0: return '0'
    if len(a) <= 0 or len(b) <= 0: return a + b 
    return str(int(a) + int(b))


print(sum_str('', '9'))