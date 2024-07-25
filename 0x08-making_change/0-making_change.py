#!/usr/bin/python3

"""Create a function for making change."""


def makeChange(coins, total):
    """Create a function for making change."""
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    temp_1 = 0
    coins = sorted(coins)[::-1]
    for x in coins:
        while x <= total:
            total -= x
            temp_1 += 1
        if (total == 0):
            return temp_1
    return -1
