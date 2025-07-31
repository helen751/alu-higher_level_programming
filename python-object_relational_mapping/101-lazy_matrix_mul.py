#!/usr/bin/python3
"""
This module contains a function to multiply two matrices using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list): First matrix (list of lists of integers/floats).
        m_b (list): Second matrix (list of lists of integers/floats).

    Returns:
        numpy.ndarray: The product of m_a and m_b.
    """
    return np.matmul(m_a, m_b)
