#!/usr/bin/python3
"""
Module that defines a rebel MyInt class.
"""


class MyInt(int):
    """
    MyInt has == and != operators inverted.
    """
    def __eq__(self, other):
        """
        Invert == to !=.
        """
        return int(self) != other

    def __ne__(self, other):
        """
        Invert != to ==.
        """
        return int(self) == other
