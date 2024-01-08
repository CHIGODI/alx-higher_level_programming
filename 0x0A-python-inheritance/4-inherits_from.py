#!/usr/bin/python3
"""
  looking if a class is a subclass of, either directly
  of inherited
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    directly or indirectly from the specified class.

    Arguments:
    obj -- Object to be checked
    a_class -- Specified class

    Returns:
    True if obj is an instance of a class inherited from a_class,
    otherwise False
    """

    obj_class = type(obj)
    return isinstance(obj, a_class) and issubclass(obj_class, a_class) \
        and obj_class != a_class


"""
def inherits_from(obj, a_class):
        obj_class = type(obj)
        if obj_class is a_class:
                return False

        for inherited_class in obj_class.__bases__:
                if inherits_from(inherited_class, a_class):
                        return True
                else:
                        return False
"""
