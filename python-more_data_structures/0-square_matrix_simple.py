#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = [row[:] for row in matrix]

    for iter_row in range(len(new_matrix)):
        for iter_column in range(len(new_matrix[iter_row])):
            new_matrix[iter_row][iter_column] = (
                new_matrix[iter_row][iter_column] ** 2
            )
    return new_matrix
