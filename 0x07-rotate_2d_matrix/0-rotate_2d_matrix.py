#!/usr/bin/python3
'''
Rotate 2D Matrix Module
'''


def rotate_2d_matrix(matrix):
    '''
    Given an n x n 2D matrix, function rotates it 90 degrees clockwise
    '''
    N = len(matrix)

    for i in range(N):
        for j in range(i+1, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(N):
        for j in range(int(N/2)):
            matrix[i][j], matrix[i][N-j-1] = matrix[i][N-j-1], matrix[i][j]
