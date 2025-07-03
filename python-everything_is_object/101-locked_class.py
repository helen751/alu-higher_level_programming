#!/usr/bin/python3
"""LockedClass module.
Defines a LockedClass that only allows setting 'first_name' as a new attribute.
"""


class LockedClass:
    """Prevents user from creating new instance attributes except 'first_name'."""
    __slots__ = ('first_name',)
