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
    
    for symbol in '.?:':
        text = text.replace(symbol, symbol + "\n")

    lines_divided = [line.strip() for line in text.splitlines() if line.strip()]
    
    for line in lines_divided:
        print(line)
