def changer(s):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    output = ''
    for palavra in s:
        for letra in palavra:
            letra = str(letra).lower()
            if letra == ' ':
                pass
            elif letra in '1234567890':
                pass
            else:
                index = alfabeto.index(letra) + 1
                if index == 26:
                    index = 0
                letra = letra.replace(letra, alfabeto[index])    
            if letra in 'aeiou':
                letra = str(letra).upper()
            output += f'{letra}'
    return output


print(changer('Hello World'))