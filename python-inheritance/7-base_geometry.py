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
