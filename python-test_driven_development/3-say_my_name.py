#!/usr/bin/python3
"""
This module provide us a function that prints a full name 
"""
def say_my_name(first_name, last_name=""):
    """
    This funciton prints the first name and the last name
    is are strings otherwise a message is raised.

    Args:
    first_name(str): name, first parameter
    last_name(str): last_name, second parameter

    Print:
    The full name like:
    My name is <first name> <last name>

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
