#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_list = a_dictionary.keys()
    sorted_keys = sorted(key_list)

    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")
