#!/usr/bin/python3
"""
This module provides functions for serializing data to a file
and loading data from a file using JSON format.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize the given data and save it to a specified file.

    Args:
        data (any): The data to be serialized. This can be any Python
                    data structure that is serializable to JSON.
        filename (str): The name of the file where the serialized data
                        will be saved.

    Returns:
        None: This function does not return a value.
    """
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load data from a specified file and deserialize it from JSON format.

    Args:
        filename (str): The name of the file from which the data will
                        be loaded.

    Returns:
        any: The deserialized data, which can be any Python data
              structure that was previously serialized.
    """
    with open(filename, "r") as file:
        return json.load(file)
