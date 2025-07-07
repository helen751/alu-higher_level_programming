#!/usr/bin/python3
"""
Module that defines a class MyList inheriting from list.
"""


class MyList(list):
    """
    MyList inherits from list and adds print_sorted method.
    """
    def print_sorted(self):
        """
        Print the list in ascending order.
        """
        print(sorted(self))
