#!/usr/bin/python3
def no_c(my_string):
    new_string = ""

    for iterator in range(len(my_string)):
        if my_string[iterator] == 'c' or my_string[iterator] == 'C':
            continue
        new_string += my_string[iterator]
    return new_string
