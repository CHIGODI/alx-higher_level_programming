#!/usr/bin/python3

"""
  This module defines the Rectangle class that represents a
  rectangle object.
  It inherits functionality from the BaseGeometry class to
  handle geometry-related operations.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle object inheriting from the BaseGeometry class.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width value for the rectangle.
            height (int): The height value for the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
