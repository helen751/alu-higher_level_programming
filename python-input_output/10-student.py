#!/usr/bin/python3
"""Module that defines a Student class with filtered serialization.
"""


class Student:
    """Defines a student by first_name, last_name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """Instantiate with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dict representation of the Student.
        If attrs is a list of strings, only attributes named in this list
        will be returned.
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {k: getattr(self, k)
                    for k in attrs if hasattr(self, k)}
        return self.__dict__
