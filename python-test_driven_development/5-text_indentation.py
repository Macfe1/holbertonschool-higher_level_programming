#!/usr/bin/python3
"""
This module contains a function that formats a
given text by adding two new lines after each occurrence
of the following punctuation marks: '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Formats the given text by ensuring there are
    two new lines after each of the specified
    punctuation marks. Removes any trailing spaces from the output lines

    Parameters:
    text (str): The text to be formatted.

    Print:
    The formatted text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""

    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    print(result.strip(), end='')


if __name__ == "__main__":
    text_indentation("Holberton?School")
