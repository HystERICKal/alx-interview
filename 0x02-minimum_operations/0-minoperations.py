#!/usr/bin/python3
"""Calculate Minimum Operations."""


def minOperations(n):
    """Calculate Minimum Operations."""
    if (n < 2):
        return 0
    temp_1, temp_2 = 0, 2
    while temp_2 <= n:
        if n % temp_2 == 0:
            temp_1 += temp_2
            n = n / temp_2
            temp_2 -= 1
        temp_2 += 1
    return temp_1
