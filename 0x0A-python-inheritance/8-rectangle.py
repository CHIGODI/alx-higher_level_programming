#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
A rectangle child class of basegeometry
"""


class Rectangle(BaseGeometry):
    """
    Attributes of rectangle
    width: width or rectangle
    heigh: height or rectangle
    """
    def __init__(self, width, height):
        """
        object constructor
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
