#!/usr/bin/python3
'''
Module contains:
a method that calculates the fewest number of operations needed to result in\
        exactly n H characters in the file.
'''


def minOperations(n):
    '''
    a method that calculates the fewest number of operations needed to result\
            in exactly n H characters in the file.
    '''
    if n <= 1:
        return 0

    num_hs = 2
    paste_count = 1
    operations = 2

    while (num_hs < n):
        if (n - num_hs) % num_hs != 0:
            num_hs += paste_count
            operations += 1
        else:
            paste_count = num_hs
            num_hs += paste_count
            operations += 2

    return operations
