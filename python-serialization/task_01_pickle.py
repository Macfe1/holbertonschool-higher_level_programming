#!/usr/in/python3
"""
Represents a custom object with attributes name, age, and is_student.
"""
import pickle


class CustomObject:
    """
     A class to represent a custom object.

    Arg:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): Indicates if the object is a student.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object.
        """
        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file.
        """
        try:
            with open(filename, "wb") as serialized_file:
                pickle.dump(self, serialized_file)
        except (OSError, pickle.PicklingError) as file:
            print(f"Error serializing object: {file}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load an instance of CustomObject from a file.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)

        except (FileNotFoundError, pickle.UnpicklingError, EOFError)\
                as file_err:
            print(f"Error deserializing object: {file_err}")
            return None
