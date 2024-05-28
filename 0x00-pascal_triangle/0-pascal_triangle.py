#!/usr/bin/python3
"""Mock interview - Pascal's Triangle"""


def pascal_triangle(n):
    """Execution"""
    int_list = []
    if n > 0:
        for x in range(1, n + 1):
            section = []
            temp = 1
            for y in range(1, x + 1):
                section.append(temp)
                temp = temp * (x - y) // y
            int_list.append(section)
    return int_list
