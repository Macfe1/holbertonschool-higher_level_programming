#!/usr/bin/python3
"""
This module contains a method that
returns a list of lists of integers
representing the Pascal’s triangle
of n
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle
    Each number is the sum of the two directly above it.
    The triangle starts with a single 1 at the top.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists, where each inner list represents a row
              of Pascal's triangle. Returns an empty list if n <= 0.

    Example:
        If n = 5, the function will return:
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
    """
    if n <= 0:
        return []

    list_triangle = []

    for rows in range(n):
        row = [1] * (1 + rows)

        for iterator_row in range(1, rows):
            row[iterator_row] = list_triangle[rows - 1][iterator_row - 1] \
                    + list_triangle[rows - 1][iterator_row]

        list_triangle.append(row)

    return list_triangle
