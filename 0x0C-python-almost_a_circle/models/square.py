#!/usr/bin/python3
"""
Represents a square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for the width attribute.
        """
        return self.height

    @size.setter
    def size(self, value):
        """
        Setter method for the width attribute.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
        Updates attributes of rectangle on how they are passed
        """
        if args:
            attr = ['id', 'size', 'x', 'y']
            for key, val in zip(attr, args):
                setattr(self, key, val)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
             returns dictionary representation of square
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
