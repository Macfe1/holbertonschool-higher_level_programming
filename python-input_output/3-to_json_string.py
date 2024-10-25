#!/usr/bin/python3
"""
This module have a a function that returns the JSON
representation of an object (string):
"""
import json

def to_json_string(my_obj):
    """
    This funciton retuns the JSON representation
    of an object (string)
    """
    return json.dumps(my_obj)
