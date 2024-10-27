#!/usr/bin/python3
"""
This module contains the Students class
that retrieves a dictionary representation
of a Student instance
"""


class Student:
    """
    A class to represent a student.

    Attributes:
        first_name: The first name of the student.
        last_name: The last name of the student.
        age: The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary representation of the Student instance.

        Returns:
            new_dictionary: A dictionary containing the student's attributes.
        """
        new_dictionary = self.__dict__
        return new_dictionary
