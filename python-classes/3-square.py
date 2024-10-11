#!/usr/bin/python3
"""
This module defines a class Square that represents a square.
"""


class Square:
    """
    A class that defines a square by its size.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.

        Arguments:
            size(int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        The area function calculates teh area of the square

        Return: The area of teh square
        """
        return self.__size * self.__size
