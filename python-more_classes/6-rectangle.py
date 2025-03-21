#!/usr/bin/python3
"""
This module defines a class Rectangle
The Rectangle class is empty
"""


class Rectangle:
    """
    An empty class that defines a Rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            string = ""
            for iterator in range(self.__height):
                string += "#" * self.__width
                if iterator < self.height - 1:
                    string += "\n"
        return string

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")


if __name__ == "__main__":
    new_rectangle = Rectangle(3, 5)
    print(new_rectangle)
    print()
    second_new_rectangle = eval(repr(new_rectangle))
    print(second_new_rectangle)
