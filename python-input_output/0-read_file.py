#!/usr/bin/python3
"""
This module provides a function to read and print the content of a file.
"""


def read_file(filename=""):
    """
    Reads the content of filename and prints it to the standard output.
    """
    with open(filename, "r") as file:
        content = file.read()
        print(content, end="")
