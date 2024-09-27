#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    else:
        maxi_value = my_list[0]
        for iterator in range(len(my_list)):
            if my_list[iterator] > maxi_value:
                maxi_value = my_list[iterator]
        return maxi_value
