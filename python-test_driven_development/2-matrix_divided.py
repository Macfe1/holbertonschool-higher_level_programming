#!/usr/bin/python3
"""
In this module will take a matrix and
divides every number in there with the number div argument
"""


def matrix_divided(matrix, div):
    """
    This function snip every number of the matrix and
    it is divided by the argument div tis division returns
    a new matrix

    Args:
    matrix(int, float): list of list of integers or floats
    div(int, float): number

    Return:
    a new matrix wiht the result of the division
    """
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a \
                            matrix (list of lists) of integers/floats")
        for number in row:
            if not isinstance(number, (int, float)):
                raise TypeError("matrix must be a \
                                matrix (list of lists) of integers/floats")
    row_length = len(matrix[0])
    for rows in matrix[1:]:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(number / div, 2) for number in row]
        new_matrix.append(new_row)
    return new_matrix


if __name__ == "__main__":
    print(matrix_divided([[1, 2, 3]], 3.0))
