#!/usr/bin/python3
"""Solve the N queens problem."""
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be d number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

temp_1 = int(sys.argv[1])


def queens(temp_1, x=0, d=[], e=[], f=[]):
    """Solve the N queens problem."""
    if x < temp_1:
        for y in range(temp_1):
            if y not in d and x + y not in e and x - y not in f:
                yield from queens(temp_1, x + 1, d + [y], e + [x + y], f + [x - y])
    else:
        yield d


def solve(temp_1):
    """Solve the N queens problem."""
    v = []
    x = 0
    for solution in queens(temp_1, 0):
        for g in solution:
            v.append([x, g])
            x += 1
        print(v)
        v = []
        x = 0


solve(temp_1)

