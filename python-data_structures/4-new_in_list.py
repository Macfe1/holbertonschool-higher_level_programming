#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp_list = my_list[:]

    if idx < 0:
        return temp_list
    elif idx >= len(my_list):
        return temp_list
    else:
        temp_list[idx] = element
        return temp_list
