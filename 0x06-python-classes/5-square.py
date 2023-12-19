#!/usr/bin/python3
"""A class representing a square."""


class Square:
    """Represents a square object."""

    def __init__(self, size=0):
        """
        Initializes a Square object with a specified size.

        Parameters:
        size (int): The length of a side of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the value of size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the value of size."""
        if type(value) is not int:
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                for _ in range(self.__size):
                    print("#", end='')
                print()
