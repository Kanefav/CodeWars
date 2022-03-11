def dont_give_me_five(start, end):
    cont = 0
    for num in range(start, end+1):
        if '5' not in str(num):
            cont += 1
    return cont