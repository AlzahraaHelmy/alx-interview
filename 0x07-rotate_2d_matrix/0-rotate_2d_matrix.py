#!/usr/bin/python3
"""
Define a function rotates an nxn 2D matrix 90 degrees in-place
"""


def rotate_2d_matrix(matrix):
    """
    Return:
        Non
    """
    nu = len(matrix)
    for i in range(nu):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(nu):
        for j in range(int(nu / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][nu-1-j]
            matrix[i][nu-1-j] = temp
