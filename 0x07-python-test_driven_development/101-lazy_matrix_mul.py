#!/usr/bin/python3
"""
matrix multiplication or matrix product is a
binary operation that produces a matrix from
two matrices with entries in a field
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices
    """
    A = np.array(m_a)
    B = np.array(m_b)
    return A.dot(B)
