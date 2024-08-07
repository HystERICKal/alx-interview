#!/usr/bin/python3
"""Prime Game interview question."""


def isWinner(x, nums):
    """Returns the player name that won the most rounds."""
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    f = [1 for x in range(sorted(nums)[-1] + 1)]
    f[0], f[1] = 0, 0
    for v in range(2, len(f)):
        rm_multiples(f, v)

    for v in nums:
        if sum(f[0:v + 1]) % 2 == 0:
            ben = ben + 1
        else:
            maria = maria + 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """Helper function to remove multiples of a number."""
    for v in range(2, len(ls)):
        try:
            ls[v * x] = 0
        except (ValueError, IndexError):
            break