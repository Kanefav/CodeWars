def high(x):
    x = str(x).split(' ')
    score = Stemp =  0
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    for word in x:
        for letter in word:
            Stemp += alfabeto.index(letter)+1
        if Stemp > score:
            output = word
            score = Stemp
        Stemp = 0
    return output 
           
    
print(high('take me to semynak'))