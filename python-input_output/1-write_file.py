#!/usr/bin/python3
"""
This module provides a function to write in a file.
"""


def write_file(filename="", text=""):
    """
    Write text in a filename and return the number of characters

    Args:
        filename: The file where will write
        text: What we'll write

    Return:
        The number of characters
    """
    with open(filename, "w") as file:
        content = file.write(text)
        return content
