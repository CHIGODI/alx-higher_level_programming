#!/usr/bin/python3
"""
   function that returns True if the object is an instane
   of, or if the object is an instance of a clss that inherited
   from the specified class
"""


def is_kind_of_class(obj, a_class):
    """ checks if is instance """
    if isinstance(obj, a_class):
        return True
    else:
        return False
