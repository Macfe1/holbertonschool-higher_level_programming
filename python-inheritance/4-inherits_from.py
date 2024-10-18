#!/usr/bin/python3
"""
This module have a function that
is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    This function checks if an object
    is an instance of a class that
    inherited (directly or indirectly)
    from the specified class

    Args:
        obj: The object
        a_class: The class where the objec inherited

    Returns:
       True if the object is an instance of a class
       that inherited (directly or indirectly)
       from the specified class ; otherwise False.
    """
    if type(obj) is a_class:
        return False
    return True
