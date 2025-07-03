#!/usr/bin/python3
"""Defines LockedClass that only allows 'first_name' as an attribute."""


class LockedClass:
    """Prevents new attributes except 'first_name'."""
    __slots__ = ('first_name',)
