#!/usr/bin/python3
"""Rotate a 2D Matrix."""


def rotate_2d_matrix(matrix):
    """Rotate it 90 degrees clockwise."""
    temp_1 = len(matrix)
    for z in range(int(temp_1 / 2)):
        temp_2 = (temp_1 - z - 1)
        for v in range(z, temp_2):
            temp_3 = (temp_1 - 1 - v)
            temp_4 = matrix[z][v]
            matrix[z][v] = matrix[temp_3][z]
            matrix[temp_3][z] = matrix[temp_2][temp_3]
            matrix[temp_2][temp_3] = matrix[v][temp_2]
            matrix[v][temp_2] = temp_4
