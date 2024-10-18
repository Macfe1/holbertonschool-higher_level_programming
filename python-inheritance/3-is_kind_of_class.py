#!/usr/bin/python3
"""
This module have a function that checks if
an object is exactly an instance of a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    This function checks if an object is an instance of a class

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        True if the object is exactly an instance of the
        specified class ; otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
