#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]

    for iterator in range(len(new_list)):
        if new_list[iterator] == search:
            new_list[iterator] = replace
    return new_list
