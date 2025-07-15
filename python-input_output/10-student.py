#!/usr/bin/python3
"""
Defines a Student class with filter for to_json.
"""


class Student:
    """
    Student class.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes in this list are returned.
        """
        if isinstance(attrs, list) and all(type(attr) == str for attr in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
