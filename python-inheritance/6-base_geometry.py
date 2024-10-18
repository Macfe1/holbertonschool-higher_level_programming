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
    def area(self):
        """
        method that raise and exception with a message

        Args: self
        """
        raise Exception("area() is not implemented")
