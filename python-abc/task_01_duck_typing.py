#!/usr/bin/python3
"""
Module for geometric shapes
using abstract base classes.

Defines `Shape`, `Circle`, and
`Rectangle` classes, with a `shape_info` function
to print area and perimeter of shapes.

Classes:
    - Shape, Circle, Rectangle

Function:
    - shape_info
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.
    Defines the blueprint for shape objects by enforcing
    the implementation of area and perimeter methods.
    """
    @abstractmethod
    def area(self):
        """
        Calculate and return the
        area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the
        perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    A class representing a circle.
    """
    def __init__(self, radius=0):
        self.radius = radius

    def area(self):
        """
        Calculate and return
        the area of the circle.
        """
        return math.pi * (self.radius * self.radius)

    def perimeter(self):
        """
        Calculate and return
        the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    A class representing a Rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(object_o):
    """
    Prints the area and perimeter of the shape passed in.

    Args:
        object_o (Shape): The shape object (Circle or Rectangle) to calculate.
    """
    print("Area: {}".format(object_o.area()))
    print(f"Perimeter: {}".format(object_o.perimeter()))


if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
