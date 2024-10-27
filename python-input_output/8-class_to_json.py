#!/usr/bin/python3
"""
This module contains a class that
returns a dictionary with the class
attributes
"""


def class_to_json(obj):
    """
    This method returns a dictionary containing
    the attributes of the class, including
    the private ones

    Arg:
        obj: The instance of the class to be serialized

    Return:
        The dicstionary of atributtes
    """
    new_dictionary = obj.__dict__
    return new_dictionary
