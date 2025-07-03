#!/usr/bin/python3
"""Defines a LockedClass that only allows 'first_name' as an attribute."""


class LockedClass:
    """LockedClass prevents dynamic creation of attributes except 'first_name'."""
    __slots__ = ("first_name",)
