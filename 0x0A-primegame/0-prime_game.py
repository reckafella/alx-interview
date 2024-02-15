#!/usr/bin/python3
'''
Prime game module
'''


def isWinner(x, nums):
    ''' Find the winner of the game '''
    if x < 1 or not nums:
        return None
    if x > 10000 or len(nums) > 10000:
        return None

    maximum_number = max(nums)

    primes_filter = [True for _ in range(max(maximum_number + 1, 2))]

    for i in range(2, int(pow(maximum_number, 0.5)) + 1):
        if not primes_filter[i]:
            continue
        for j in range(i * i, maximum_number + 1, i):
            primes_filter[j] = False
    primes_filter[0] = primes_filter[1] = False

    prime_numbers_encountered = 0

    for i in range(len(nums)):
        if primes_filter[i]:
            prime_numbers_encountered += 1
        primes_filter[i] = prime_numbers_encountered

    first_player = 0
    for x in nums:
        first_player += primes_filter[x] % 2 == 1

    if first_player * 2 == len(nums):
        return None
    if first_player * 2 > len(nums):
        return 'Maria'
    return 'Ben'
