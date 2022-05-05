def differentiate(poly):
    if poly.count('^') == 1:
        e = poly.split('^') #equation
        x = e[0][:-1] #x
        if x == '': x = 1
        if x  == '-': x = -1
        p = e[-1]  #power
        x = int(x) * int(p)
        if int(p) >= 3 or int(p) <= -1:
            p = int(p) -1
            return f'{x}x^{p}'
        else:
            return f'{x}x'
    else:
        if poly.count('x') < 1:
            return '0'
        else:
            try: 
                int(poly[:-1])
                return poly[:-1]
            except:
                return poly.replace('x', '1')
        


print(differentiate('x^2'))