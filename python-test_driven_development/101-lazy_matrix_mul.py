#!/usr/bin/python3
"""Module for lazy matrix multiplication using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy after validation.

    Args:
        m_a: list of lists of int/float
        m_b: list of lists of int/float

    Returns:
        A new matrix as a list of lists.

    Raises:
        TypeError, ValueError: if matrices don't meet requirements
    """

    # Validate m_a and m_b
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(x, (int, float)) for row in m_a for x in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (int, float)) for row in m_b for x in row):
        raise TypeError("m_b should contain only integers or floats")

    if len({len(row) for row in m_a}) > 1:
        raise TypeError("each row of m_a must be of the same size")
    if len({len(row) for row in m_b}) > 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b).tolist()
