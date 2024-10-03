#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                        'C': 100, 'D': 500, 'M': 1000}
    integer = 0

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    for iter_input in range(len(roman_string)):
        if (iter_input + 1 < len(roman_string) and
                roman_dictionary[roman_string[iter_input]] <
                roman_dictionary[roman_string[iter_input + 1]]):
            integer -= roman_dictionary[roman_string[iter_input]]
        else:
            integer += roman_dictionary[roman_string[iter_input]]

    return integer
