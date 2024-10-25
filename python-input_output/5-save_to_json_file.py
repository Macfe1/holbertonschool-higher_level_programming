#!/usr/bin/python3
"""
This module provides a function to save a Python object
to a file in JSON format.
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using JSON representation.

    Args:
        my_obj: The Python object to be serialized to JSON.
        filename (str): The name of the file to
        which the JSON data will be written.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, filename)
