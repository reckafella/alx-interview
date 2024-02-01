#!/usr/bin/python3
'''
Making change module
'''


def makeChange(coins: list, total: int) -> int:
    '''
    determines the fewest number of coins needed to meet a given amount `total`
    '''
    if total <= 0:
        return 0
    if not coins:
        return -1
    coins.sort(reverse=True)

    min_coins = [float('Inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total+1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[total] != float('inf'):
        return min_coins[total]
    else:
        return -1
