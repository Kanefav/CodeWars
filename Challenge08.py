def solution(roman):
    num = 0
    verificador = 0
    verificador = 0
    for letra in range(0, len(roman)):
        numteste = num
        proximo = letra + 1
        if roman[letra] == 'I':
            try:
                if roman[proximo] == 'X':
                    verificador = 1
                    num += 9
                elif roman[proximo] == 'V':
                    verificador = 1
                    num += 4
                else:
                    verificador = 0
                    num += 1
            except:
                num += 1
        if verificador == 0:
            if roman[letra] == 'V':
                num += 5
        if verificador == 0:
            if roman[letra] == 'X':
                try:
                    if roman[proximo] == 'L':
                        verificador = 1
                        num += 40
                    elif roman[proximo] == 'C':
                        verificador = 1
                        num += 90
                    else:
                        verificador = 0
                        num += 10
                except:
                    num += 10
        if verificador == 0:
            if roman[letra] == 'L':
                num += 50
        if verificador == 0:
            if roman[letra] == 'C':
                try:
                    if roman[proximo] == 'M':
                        verificador = 1
                        num += 900
                    elif roman[proximo] == 'D':
                        verificador = 1
                        num += 400
                    else:
                        verificador = 0 
                        num += 100
                except:
                    num += 100
        if verificador == 0:
            if roman[letra] == 'D':
                num += 500
        if verificador == 0:
            if roman[letra] == 'M':
                num += 1000
        if num == numteste:
            verificador = 0
    return num


print(solution('MCMLXXXI')) #MCML