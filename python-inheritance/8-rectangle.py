#!/usr/bin/python3
"""
This module have a class with
a method that raise an exception
"""


class BaseGeometry:
    """
    This is a class with a method that
    raise an exception
    """
    def integer_validator(self, name, value):
        """
        This is a method that checks if the value
        is an integer that is positive and no cero

        Args:

            name(str): a name
            value(int): a number

        TypeError:
            If value is not a integer
        ValueError:
            If value is negative or cero
        """
        if type(value) is bool:
            raise TypeError(f"{name} must be an integer")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """
        method that raise and exception with a message
        """
        raise Exception("area() is not implemented")


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
