def solution(s):
    output = []
    segundaLetra = 0
    for corte in range(0, len(s), 2):
        segundaLetra += 1
        try:
            output.append(f'{s[corte]}{s[segundaLetra]}')
            segundaLetra += 1
        except:
            output.append(f'{s[corte]}_')
    return output


print(solution('asdfads'))