#!/usr/bin/python3

"""Module defining a class square """


class Square:
    """defining the class attributes and methods """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) for i in value) or value[0] < 0 or \
           value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """ returns area """
    def area(self):
        return self.__size ** 2

    """ prints square """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
                for _ in range(self.__size):
                    print(" " * self.__position[0], end='')
                    print('#' * self.__size)

    """ return square as a string """
    def __str__(self):
        output = ""
        if self.__size == 0:
            output += "\n"
        else:
            for _ in range(self.__position[1]):
                output += "\n"
            for _ in range(self.__size):
                output += " " * self.__position[0]
                output += "#" * self.__size + "\n"
        return output
