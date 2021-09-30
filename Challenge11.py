def score(dice):
    contone = contfive = output = 0
    dicestr = []
    for side in dice:
        if side == 1: 
            if contone == 2:
                contone -= 2
                output += 800
            else:
                contone += 1
                output += 100
        elif side == 5:
            if contfive == 2:
                contfive -= 2
                output += 400
            else:
                contfive += 1
                output += 50
        else:
            dicestr.append(str(side))
    if len(dicestr) >= 3:
        if dicestr.count('2') >= 3:
            output += 100 * 2
        if dicestr.count('3') >= 3:
            output += 100 * 3
        if dicestr.count('4') >= 3:
            output += 100 * 4 
        if dicestr.count('6') >= 3:
            output += 100 * 6
        return output
    else:
        return output
            


print(score([4, 4, 4, 3, 3]))