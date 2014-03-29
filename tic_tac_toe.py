__author__ = 'changyunglin'

# 3 X 3 tic-tac-toe


def checkWin(board):
    # check row
    N = len(board)
    for row in range(N):
        result = 0
        for column in range(1, N):
            if board[row][column] != board[row][column-1]:
                result = 0
                break
            result = 1
        if result == 1:
            print "One row line"
            return 'row %d', row

    # check column
    for column in range(N):
        result = 0
        for row in range(1, N):
            if board[row][column] != board[row-1][column]:
                result = 0
                break
            result = 1
        if result == 1:
            # print "One column line"
            return 'column %d', column

    # check diagonal left-up to right-down
    result = 0
    for row in range(1, N):
        if board[row][row] != board[row-1][row-1]:
            result = 0
            break
        else:
            result = 1
    if result == 1:
        print 'Diagonal check'
        return board

    # check reverse diagonal right-up to left-down
    result = 0
    for row in range(1, N):
        if board[N-row-1][row] != board[N-row][row-1]:
            result = 0
            break
        else:
            result = 1
    if result == 1:
        print 'Inverse Diagonal check'
        return board


column_check = [['x', 'o', 'o'],
                ['x', 'o', 'x'],
                ['o', 'o', 'x']]

row_check =    [['o', 'x', 'o'],
                ['x', 'x', 'x'],
                ['x', 'x', 'o']]

inverse_diag_check =   [['x', 'o', 'o'],
                        ['x', 'o', 'x'],
                        ['o', 'x', 'o']]

diag_check =   [['o', 'x', 'o'],
                ['x', 'o', 'x'],
                ['x', 'x', 'o']]


print (checkWin(row_check))
print (checkWin(column_check))
print (checkWin(inverse_diag_check))
print (checkWin(diag_check))