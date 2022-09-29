#!/usr/bin/python3
"""add attribute
"""


def add_attribute(obj, name, value):
    """ Function that adds a new attribute to an object
    Args:
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
