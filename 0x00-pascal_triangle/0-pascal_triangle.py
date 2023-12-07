#!/usr/bin/python3
'''
Module contains a function that returns a list of lists of integers\
        representing the pascal's triangle of n:\
* Returns an empty list if n <= 0;
* Assume n will be always an integer
'''


def pascal_triangle(n):
    '''
    returns a list of lists of integers representing the pascal's triangle\
            of n
    '''
    if (n <= 0):
        return []

    triangle = [[1] * (i + 1) for i in range(n)]

    # start at i = 2, first two lists are [1] and [1, 1]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle
