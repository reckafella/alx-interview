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


def is_safe(board, row, column, n):
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
    for i, j in zip(range(row, n, 1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_board_helper(board, column, n):
    ''' return solutions after all queens are placed '''
    solutions = []

    if column >= n:
        current_solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    current_solution.append([i, j])
        solutions.append(current_solution)
        return solutions

    for i in range(n):
        if is_safe(board, i, column, n):
            board[i][column] = 1

            solutions += solve_board_helper(board, column + 1, n)

            # backtrack
            board[i][column] = 0
    return solutions


def solve_nqueens(n):
    ''' return all possible solutions '''
    board = [[0] * n for _ in range(n)]

    for solution in sorted(solve_board_helper(board, 0, n)):
        print(solution)


if __name__ == '__main__':
    solve_nqueens(handle_input())
