def points(games):
    output = 0
    for game in games:
        if game[0] > game[2]:
            output += 3
        elif game[0] == game[2]:
            output += 1
    return output
            
 

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))