#!/usr/bin/python3
"""
This module provides a function that creates
an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”

    Args:
        filename: The name of the JSON file
    """
    with open(filename, "r") as file:
        return json.load(file)
