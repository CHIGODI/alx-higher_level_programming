#!/usr/bin/python3
"""
confirms if objects is instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    returns true if obj isinstance of a_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
