#!/usr/bin/python3
"""
Class Rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class represents a rectangle and inherits from the Base class.
    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): X-coordinate of the top-left corner of the rectangle.
        __y (int): Y-coordinate of the top-left corner of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """
        Returns area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints in the stdout the Rectangle
        """
        print('\n' * self.__y, end='')
        for _ in range(self.__height):
            print(' ' * self.__x, '#' * self.__width)

    def __str__(self):
        """
        returns string representation of rectangle
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "\
            f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Updates attributes of rectangle on how they are passed
        """
        if args:
            self.id = args[0] if len(args) > 0 else self.id
            self.__width = args[1] if len(args) > 1 else self.__width
            self.__height = args[2] if len(args) > 2 else self.__height
            self.__x = args[3] if len(args) > 3 else self.__x
            self.__y = args[4] if len(args) > 4 else self.__y
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
