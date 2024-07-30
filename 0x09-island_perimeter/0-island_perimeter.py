#!/usr/bin/python3
"""Code the Island Perimeter Interview Question."""


def island_perimeter(grid):
    """Return perimeter of Island."""
    temp_1 = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if (grid[x][y] == 1):
                if (x <= 0 or grid[x - 1][y] == 0):
                    temp_1 += 1
                if (x >= len(grid) - 1 or grid[x + 1][y] == 0):
                    temp_1 += 1
                if (y <= 0 or grid[x][y - 1] == 0):
                    temp_1 += 1
                if (y >= len(grid[x]) - 1 or grid[x][y + 1] == 0):
                    temp_1 += 1
    return temp_1
