#!/usr/bin/python3

"""
   Module defining reectangle class
"""


class Rectangle:
    """
    Defines a class rectangle with height and width as
    variables
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        Rectangle.number_of_instances += 1

    def area(self):
        """ returning area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returning permiter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """ makes the rectangle printable """
        rectangle = []
        for _ in range(self.__height):
            rectangle.append('#' * self.__width)

        if self.__width == 0 or self.__height == 0:
            return ''
        return '\n'.join(rectangle)

    def __repr__(self):
        """ returns the true code that produces object """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ get rid of obj instance """
        print(f"Bye rectangle...")
        Rectangle.number_of_instances -= 1
