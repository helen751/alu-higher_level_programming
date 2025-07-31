#!/usr/bin/python3
"""
This module provides a function to multiply two matrices using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The result of multiplying m_a by m_b.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers/floats,
                   or if their rows are not the same size.
        ValueError: If m_a or m_b is empty, or if the matrices can't be multiplied.
    """

    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if not all(isinstance(x, (int, float)) for row in m_a for x in row):
        raise TypeError("m_a should contain only integers or floats")
    if len({len(row) for row in m_a}) != 1:
        raise TypeError("each row of m_a must be of the same size")

    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(x, (int, float)) for row in m_b for x in row):
        raise TypeError("m_b should contain only integers or floats")
    if len({len(row) for row in m_b}) != 1:
        raise TypeError("each row of m_b must be of the same size")

    # Validate dimensions for multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform multiplication with NumPy
    return np.matmul(m_a, m_b)
