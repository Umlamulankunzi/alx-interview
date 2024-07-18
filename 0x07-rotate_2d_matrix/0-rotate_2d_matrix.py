#!/usr/bin/python3
'''
Script that Rotates 2D Matrix
In place
'''


def rotate_2d_matrix(matrix):
    '''Function rotates a 2D array'''
    #Verify if matrix is of type list
    if type(matrix) != list:
        return

    #is empty 
    if len(matrix) < 1:
        return

    # Rotate matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    n = len(matrix)
    for i in range(n//2):
        for j in range(n):
            matrix[j][i], matrix[j][n-1-i] = matrix[j][n-1-i], matrix[j][i]
