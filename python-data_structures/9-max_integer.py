#!/usr/bin/python3
def max_integer(my_list=[]):
    maxi_value = my_list[0]

    if len(my_list) == 0:
        return None
    else:
        for iterator in range(len(my_list)):
            if my_list[iterator] > maxi_value:
                maxi_value = my_list[iterator]
        return maxi_value
