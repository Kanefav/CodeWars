def increment_string(strng):
    if len(strng) == 0: return '1'
    numbers = []
    index = -1
    if strng[-1] in '0123456789':
        if strng[-1] == '9':
            while True:
                index -= 1
                if strng[index] in '0123456789':
                    if strng[index] == '0' or strng[index] == '9':
                        if strng[index-1] == '0' or strng[index-1] == '9':
                            index -= 1
                            break
                else:
                    break
            number = int(strng[index+1:]) + 1
            return f'{strng[:index+1]}{number}'
        else:
            number = int(strng[-1]) + 1
            return f'{strng[:-1]}{number}'
    else:
        return f'{strng}1'
    

            


print(increment_string('ola600833009879')) #not working (idk why),  smt about 3009879