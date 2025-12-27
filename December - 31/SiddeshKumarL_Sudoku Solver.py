def is_valid(board, r, c, ch):
    for j in range(9):
        if board[r][j] == ch:
            return False
    for i in range(9):
        if board[i][c] == ch:
            return False
    br = (r // 3) * 3
    bc = (c // 3) * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if board[i][j] == ch:
                return False
    return True


def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for ch in map(str, range(1, 10)):
                    if is_valid(board, i, j, ch):
                        board[i][j] = ch
                        if solve_sudoku(board):
                            return True
                        board[i][j] = '.' 
                return False  
    return True 


board = []
for _ in range(9):
    row = input().split()
    board.append(row)

solve_sudoku(board)

for row in board:
    print(" ".join(row))
