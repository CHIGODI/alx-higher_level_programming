#!/usr/bin/python3
"""A class representing a square."""


class Square:
    """Represents a square object."""

    def __init__(self, size=0):
        """
        Initializes a Square object with a specified size.

        Parameters:
        size (int): The length of a side of the square.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        int: The area of the square (size * size).
        """
        return self.__size * self.__size
