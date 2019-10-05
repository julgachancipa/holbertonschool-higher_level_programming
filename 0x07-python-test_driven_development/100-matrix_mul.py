#!/usr/bin/python3
"""
matrix multiplication or matrix product is a
binary operation that produces a matrix from
two matrices with entries in a field
"""


def matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for i in range(len(m_a)):
        if type(m_a[i]) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(m_a[0]) == 0:
            raise ValueError("m_a can't be empty")
        for j in range(len(m_a[i])):
            if type(m_a[i][j]) is not int and type(m_a[i][j]) is not float:
                raise TypeError("m_a should contain only integers or floats")
        if len(m_a[0]) != len(m_a[i]):
            raise TypeError("each row of m_a must be of the same size")

    for i in range(len(m_b)):
        if type(m_b[i]) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(m_b[0]) == 0:
            raise ValueError("m_b can't be empty")
        for j in range(len(m_b[i])):
            if type(m_b[i][j]) is not int and type(m_b[i][j]) is not float:
                raise TypeError("m_b should contain only integers or floats")
        if len(m_b[0]) != len(m_b[i]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    if len(m_a) == 1 and len(m_b[0]) == 1:
        flag = len(m_a)
    else:
        flag = len(m_b)
    n_mtx = []
    for i in range(len(m_a)):
        n_row = []
        for j in range(flag):
            res = 0
            for k in range(len(m_b)):
                res += m_a[i][k] * m_b[k][j]
            n_row.append(res)
        n_mtx.append(n_row)
    return n_mtx
