#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import os


class TestBaseLoadFromFile(unittest.TestCase):
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertIsInstance(rectangles[1], Rectangle)

    def test_load_from_file_square(self):
        s1 = Square(5)
        s2 = Square(9, 1, 3)

        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertIsInstance(squares[0], Square)
        self.assertIsInstance(squares[1], Square)


if __name__ == '__main__':
    unittest.main()
