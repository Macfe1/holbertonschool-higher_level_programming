#!/usr/bin/python3
"""
In this module we'll print a square with the character #
a size number of times
"""


def print_square(size):
    """
    With this fucntion we will print a square with character # printed
    size times

    Args:
    size(int): The size length of the square

    Print:
    A square with the size length
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        return
    for row in range(size):
        print("#" * size)


if __name__ == "__main__":
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
