#!/usr/bin/python3
"""
This module defines a class Square that represents a square.
"""


class Square:
    """
    A class that defines a square by its size.

    Attributes:
        size (int): The size of the square.

    Methods:
        area(): Returns the area of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with the given size.

        Arguments:
            size(int): The size of the square.

        Raises:
               TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        Arguments:
            value (int): The new size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Number of space before the square is printed

        Arguments:
            value (int): that takes the position of the position
        """

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num_position, int) and
                        num_position >= 0 for num_position in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        The area function calculates the area of the square

        Return: The area of teh square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        my_print fuction prints a # size times cfreating a square

        Print: # size times in every iteration after the spaces where present
        """

        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for iterator in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
