#!/usr/bin/python3
"""
The module have a function that adds
all arguments to a Python list,
and then save them to a JSON file:
"""


import sys
import json

save_to_json_fl = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def from_pylist_to_jsonlist():

    try:
        items = load_from_json_file("add_item.json")

    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_fl(items, "add_item.json")


if __name__ == "__main__":
    from_pylist_to_jsonlist()
