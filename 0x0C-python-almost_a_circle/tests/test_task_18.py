#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseCreate(unittest.TestCase):
    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsInstance(r2, Rectangle)

    def test_create_square(self):
        s1 = Square(2, 3, 4)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsInstance(s2, Square)

    def test_create_with_invalid_class(self):
        invalid_dict = {"invalid_attr": 10}
        instance = Base.create(**invalid_dict)
        self.assertIsNone(instance)


if __name__ == '__main__':
    unittest.main()
