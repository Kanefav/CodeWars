def valid_solution(board):
    sum = 0
    for linha in board:
        lin = str(linha)
        if lin.count('0') >= 1:
            return False
    for linha in range(0, 9, 3):
        for x in range(linha, linha+3):
            for y in range(linha, linha+3):
                sum += board[x][y]
        if sum != 45:
            return False
        else:
            sum = 0
    return True


print(valid_solution(             [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 4, 5, 2, 8, 6, 1, 7, 9]]))