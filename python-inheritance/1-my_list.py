#!/usr/bin/python3
"""
Module that defines MyList, a subclass of list with a print_sorted method.
"""


class MyList(list):
    """
    MyList class inherits from list.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
