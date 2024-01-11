#!/usr/bin/python3
import sys
'''N Queens Puzzle'''


def handle_input():
    ''' Handle input '''
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            exit(1)
    except ValueError:
        print('N must be a number')
        exit(1)
    return n


def is_safe(board: list, row: int, column: int, n: int) -> bool:
    '''
    check if there is a queen in the same row, column or diagonal
    '''
    # same row
    for i in range(column):
        if board[row][i] == 1:
            return False

    # upper diagonal
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    # lower diagonal
    for i, j in zip(range(row, n, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_board_helper(board: list, column, n) -> bool:
    ''' return True if all queens are placed '''
    if column >= n:
        return True

    for i in range(n):
        if is_safe(board, i, column, n):
            board[i][column] = 1

            if solve_board_helper(board, column + 1, n):
                return True
            # backtrack if placing the queen in the current position does not
            #   lead to a solution
            board[i][column] = 0
    return False


def solve_nqueens(n: int) -> list:
    ''' return all possible solutions '''
    board = [[0] * n for _ in range(n)]
    solution = []

    if solve_board_helper(board, 0, n):
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
    print(solution)


if __name__ == '__main__':
    n = handle_input()
    solve_nqueens(n)
