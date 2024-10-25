#!/usr/bin/python3
"""
This module provides a function that appends text in a file
"""


def append_write(filename="", text=""):
    """
    Append a text in a file

    Args:
        filename: The file where will write
        text: What we'll write

    Return:
        The number of characters
    """
    with open(filename, "a") as file:
        return file.write(text)
