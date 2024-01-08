#!/usr/bin/python3
"""
defines a class square that inherits from class rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Represents a square class inheriting from base class
    Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
