#!/usr/bin/python3

"""A class Square that defines a square."""

class Square:
    """Represents a square object."""

    def __init__(self, size=0):
        """
        param size is private has checks
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
