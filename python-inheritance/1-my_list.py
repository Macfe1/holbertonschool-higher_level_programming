#!/usr/bin/python3
"""
Module: my_list

This module defines a custom list class `MyList`
that inherits from the built-in Python list.
The `MyList` class includes a method for printing the list in
sorted order.
"""


class MyList(list):
    """
    A class that inherits from the built-in list class.

    This class provides a method to print the list in sorted order.
    """
    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.

        This method does not modify the original list. It creates a
        sorted copy of the list and prints it.
        """
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append("a")
    my_list.print_sorted()
