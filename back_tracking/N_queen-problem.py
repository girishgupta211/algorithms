# Python program to solve N Queen Problem using backtracking

global N
N = 4


# A utility function to check if a queen can be placed on board[row][col]. Note that this
# function is called when "col" queens are  already placed in columns from 0 to col -1.
# So we need to check only left side for attacking queens


def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queen(board, col):
    # base case: If all queens are placed  then return true
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for row in range(N):

        if is_safe(board, row, col):
            # Place this queen in board[row][col]
            board[row][col] = 1

            # recur to place rest of the queens
            if solve_n_queen(board, col + 1):
                return True

            # If placing queen in board[row][col] doesn't lead to a solution, then queen from board[i][col]
            board[row][col] = 0

    # if the queen can not be placed in any row in this column col then return false
    return False


def solve_NQ():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]
             ]

    if not solve_n_queen(board, 0):
        print("Solution does not exist")
        return False

    print(board)
    return True


solve_NQ()
