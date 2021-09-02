def namelist(names):
    string = ''
    if len(names) == 0:
        return string
    if len(names) == 1:
        string = names[0]['name']
        return string
    if len(names) == 2:
        for nome in range(0, len(names)):
            nometemp = names[nome]['name']
            if nome == 0:
                string += f'{nometemp} & '
            else:
                string += nometemp
        return string
    if len(names) >=3:
        verificar = 0
        for nome in range(0, len(names)):
            if verificar == 0:
                nometemp = names[nome]['name']
                if nometemp == names[-2]['name']:
                    string += f'{nometemp} & '
                    verificar = 1
                if verificar == 0:
                    string += f'{nometemp}, '
            else:
                nometemp = names[nome]['name']
                string += nometemp
        return string


lista = [ {'name': 'Bart'}]
print(namelist(lista))
