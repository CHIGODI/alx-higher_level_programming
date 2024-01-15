#!/usr/bin/python3
"""
Test cases for sqaure class
"""

import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """
    def tearDown(self):
        """
        Reset the __nb_objects attribute to its initial value after each
        test method
        """
        Base._Base__nb_objects = 0

    def test_square_creation(self):
        """
        Test the creation of a Square instance with valid data.
        """
        s = Square(5, 2, 3, 1)
        self.assertEqual((s.id, s.width, s.height, s.x, s.y), (1, 5, 5, 2, 3))

    def test_square_str_representation(self):
        """
        Test the string representation of a Square instance.
        """
        s = Square(10, 1, 1, 20)
        self.assertEqual(str(s), "[Square] (20) 1/1 - 10")

    def test_square_invalid_data(self):
        """
        Test cases for invalid data when creating a Square instance.
        """
        # Test invalid size
        with self.assertRaises(ValueError):
            s = Square(0)

        # Test invalid x and y
        with self.assertRaises(ValueError):
            s = Square(5, -1, 2)

if __name__ == '__main__':
    unittest.main()
