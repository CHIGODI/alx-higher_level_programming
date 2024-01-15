#!/usr/bin/python3
"""
"""
import unittest
from models.square import Square
from models.base import Base

class TestSquareSizeGetterSetter(unittest.TestCase):
    """
    """
    def tearDwon(self):
        """
        """
        Base._Base__nb_objects = 0

    def test_getter(self):
        """
        """
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_setter(self):
        """
        """
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_setter_with_invalid_size(self):
        """
        """
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = 0

if __name__ == '__main__':
    unittest.main()
