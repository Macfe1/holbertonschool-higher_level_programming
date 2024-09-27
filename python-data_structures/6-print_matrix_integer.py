#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for iterator, column in enumerate (row):
            if iterator < len(row) - 1:
                print("{:d}".format(column), end=" ")
            else:
                print("{:d}".format(column), end="")
        print()
