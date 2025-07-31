#!/usr/bin/python3
"""
This module contains a function to multiply two matrices manually.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list): First matrix (list of lists of integers/floats).
        m_b (list): Second matrix (list of lists of integers/floats).

    Returns:
        list: A new matrix which is the product of m_a and m_b.

    Raises:
        TypeError: If inputs are not lists, lists of lists, or contain invalid types.
        ValueError: If matrices are empty, rows are inconsistent in size,
                    or matrices cannot be multiplied.
    """

    # 1. Validate that m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. Validate that they are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3. Validate non-empty matrices
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 4. Validate all elements are int or float
    if not all(isinstance(el, (int, float)) for row in m_a for el in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(el, (int, float)) for row in m_b for el in row):
        raise TypeError("m_b should contain only integers or floats")

    # 5. Validate matrix is rectangular
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    # 6. Validate multiplication compatibility
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # 7. Matrix multiplication
    result = []
    for row in m_a:
        new_row = []
        for j in range(len(m_b[0])):
            sum_product = 0
            for k in range(len(m_b)):
                sum_product += row[k] * m_b[k][j]
            new_row.append(sum_product)
        result.append(new_row)

    return result
