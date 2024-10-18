#!/usr/bin/python3
"""
This module have a function that checks if
an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    This function checks if an object is an instance of a class

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    return False
