#!/usr/bin/python3
'''
Island perimeter module
'''


def island_perimeter(grid):
    '''
    function that returns the perimeter of the island described in grid
    '''
    ones = 0
    if not isinstance(grid, list):
        return 0
    for i in range(0, len(grid)):
        for j in range(len(grid[i])):
            if not grid[i][j] == 0 or not grid[i][j] == 1:
                return 0
            if grid[i][j] == 0:
                continue
            if grid[i][j] == 1:
                if grid[i-1][j] == 1 and grid[i][j+1] == 1:
                    ones += 1
                ones += grid[i][j]
    return (ones * 2)
