#!/usr/bin/python3
"""
This module provides a function to add two integers
Or to substractif one of the parameters is negative

"""


def add_integer(a, b=98):

    """
    Add two integer.

    The fucntion take two parameters and adds the together.
    If one of the parameters is not float or int a TypeError will be raised.
    If the parameters are float will be casted to an integer and the final step
    is provide the sum or a substraction in the situation that
    one of teh parameters is negative.

    Parameters:
    a (can be int or float): The first number to sum
    b (can be int or float): The second number to sum

    Return:

    The addition of a and b or
    The substraction of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    total = int(a) + int(b)

    return total


if __name__ == "__main__":
    print(add_integer(8, "H"))
