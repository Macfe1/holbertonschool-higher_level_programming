#!/usr/bin/python3
"""
This module have a class with
a method that raise an exception
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle that inherits from BaseGeometry.

    This class uses the integer_validator method from BaseGeometry
    to ensure that the width and height are positive integers.
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            Must be a positive integer.

            height (int): The height of the rectangle.
            Must be a positive integer.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to zero.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


if __name__ == "__main__":
    print(issubclass(Rectangle, BaseGeometry))
