#!/usr/bin/python3
from abc import ABC, abstractmethod


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
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculate and return
        the area of the circle.
        """
        return 3.1416 * (self.radius * self.radius)

    def perimeter(self):
        """
        Calculate and return
        the perimeter of the circle.
        """
        return 2 * self.radius * 3.1416


class Rectangle(Shape):
    """
    A class representing a Rectangle
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


def shape_info(object_o):
    """
    Prints the area and perimeter of the shape passed in.

    Args:
        object_o (Shape): The shape object (Circle or Rectangle) to calculate.
    """
    print(f"Area: {object_o.area()}")
    print(f"Perimeter: {object_o.perimeter()}")
