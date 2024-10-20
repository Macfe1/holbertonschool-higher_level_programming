#!/usr/bin/python3
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * (self.radius * self.radius)

    def perimeter(self):
        return 2 * self.radius * 3.1416


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


def shape_info(object_o):
    print(f"Area: {object_o.area()}")
    print(f"Perimeter: {object_o.perimeter()}")
