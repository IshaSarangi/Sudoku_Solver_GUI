import pprint

def solve(board):
    # solves sudoku board using backtracking
    # board: 2d list of integers
    # return: solution

    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1, 10):
        if valid (board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    else:
        return False

def valid (board, pos, num):
    # returns if the attempted move is valid
    # board: 2d list on integers
    # pos : (row, col)
    # num : integer
    # return: boolean

    # row check
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # column check
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[1] != i:
            return False

    # box check
    xbox = pos[1]//3
    ybox = pos[0]//3

    for i in range(ybox*3, ybox*3 + 3):
        for j in range(xbox*3, xbox*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    else:
        return True

def find_empty(board):
    # finds empty space in board
    # board: partially complete board
    # return: (int row, int col)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)

    else:
         return None

def print_board(board):
    # prints the board
    # board: 2d list of integers
    # return: none

    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j%3 == 0:
                print(" | ", end = "")

            if j == 8:
                print(board[i][j], end = "\n")
            else:
                print(str(board[i][j]) + " ", end = "")

board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

p = pprint.PrettyPrinter(width = 41, compact = True)
solve(board)
p.pprint(board)
