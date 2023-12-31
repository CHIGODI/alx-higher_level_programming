#!/usr/bin/python3
"""
Defines a class BaseGeometry
"""


class BaseGeometry:
    """
    attributes of this class
    """
    def area(self):
        """
        not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value if its ONLY int
        """
        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
