#!/usr/bin/python3
"""
Module that defines a function to check if an object is an instance of,
or if the object is an instance of a class that inherited from, the
specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of, or inherited from, a_class.
    """
    return isinstance(obj, a_class)
