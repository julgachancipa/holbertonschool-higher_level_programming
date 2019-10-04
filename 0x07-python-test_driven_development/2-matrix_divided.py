#!/usr/bin/python3
"""
first_name and last_name must be strings otherwise,
raise a TypeError exception with the message first_name
must be a string or last_name must be a string
"""


def matrix_divided(matrix, div):
    """
    prints My name is <first name> <last name>
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    new_mtx = [x[:] for x in matrix]
    sz = len(matrix[0])
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
        if sz != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int\
               and type(matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")
            new_mtx[i][j] = round(matrix[i][j] / div, 2)
    return new_mtx
