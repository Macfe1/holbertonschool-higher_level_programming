#!/usr/bin/python3
"""
This module defines a class Square
that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that represents a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.
        Args:
            size (int): The size of the square.
            Must be a positive integer.
        Raises:
            TypeError: If size is not an integer.
                ValueError: If size is less than or equal to zero.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
