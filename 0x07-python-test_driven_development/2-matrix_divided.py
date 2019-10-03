#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(div) is not (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new_mtx = [x[:] for x in matrix]
    sz = len(matrix[0])
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if sz != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_mtx[i][j] = round(matrix[i][j] / div, 2)
    return new_mtx
