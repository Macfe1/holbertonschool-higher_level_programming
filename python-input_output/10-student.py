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

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        If attrs is a list of strings, only the attributes
        contained in this list will be retrieved.

        Args:
            attrs (list): A list of attribute names to retrieve.

        Returns:
            new_dictionary: A dictionary containing the student's attributes.
        """
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, (list, str)):
            new_dictionary = {}

            for iterator in attrs:
                if iterator in self.__dict__:
                    new_dictionary[iterator] = self.__dict__[iterator]
            return new_dictionary

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance.

        Args:
            json (dict): A dictionary containing the attributes to set.
        """
        for key, value in json.items():
            setattr(self, key, value)
