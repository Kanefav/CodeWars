def valid_solution(board):
    save = []
    firsty = cont = sum = firstx = 0
    secondy = secondx = 3
    for linha in board:
        lin = str(linha)
        if lin.count('0') >= 1:
            return False
    for linha in board:
        if cont == 1:
            firsty = 3
            secondy = 6
        if cont == 2:
            firsty = 6
            secondy = 9
        if cont == 3:
            firsty = 0
            secondy = 3
            firstx = 3
            secondx = 6
        if cont == 4:
            firsty = 3
            secondy = 6
        if cont == 5:
            firsty = 6
            secondy = 9
        if cont == 6:
            firsty = 0
            secondy = 3
            firstx = 6
            secondx = 9
        if cont == 7:
            firsty = 3
            secondy = 6
        if cont == 8:
            firsty = 6
            secondy = 9
        for x in range(firstx, secondx):
            for y in range(firsty, secondy):
                save.append(board[x][y])
                sum += board[x][y]
        if sum != 45:
            return False
        else:
            print(save)
            print(sum)
            cont += 1
            save = []
            sum = 0
    return True


print(valid_solution([ [1, 3, 2, 5, 7, 9, 4, 6, 8],
[4, 9, 8, 2, 6, 1, 3, 7, 5],
[7, 5, 6, 3, 8, 4, 2, 1, 9],
[6, 4, 3, 1, 5, 8, 7, 9, 2],
[5, 2, 1, 7, 9, 3, 8, 4, 6],
[9, 8, 7, 4, 2, 6, 5, 3, 1],
[2, 1, 4, 9, 3, 5, 6, 8, 7],
[3, 6, 5, 8, 1, 7, 9, 2, 4],
[8, 7, 9, 6, 4, 2, 1, 3, 5] ]))