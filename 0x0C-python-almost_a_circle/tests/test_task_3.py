#!/usr/bin/python3
"""
Module containing task 2 testcases (First Rectangle)
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    Test if the 'id' attribute is assigned correctly
    """
    def tearDown(self):
        """
        Reset the __nb_objects attribute to its initial value after each
        test method
        """
        Base._Base__nb_objects = 0

    def test_ractangle(self):
        """
        """
        r1 = Rectangle(10, 2)

        with self.assertRaises(TypeError):
            r12 = Rectangle(2.2, 10)

        with self.assertRaises(TypeError):
            r2 = Rectangle(2, 10.3)

        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 10)

        with self.assertRaises(ValueError):
            r13 = Rectangle(10, 0)

        with self.assertRaises(TypeError):
            r4 = Rectangle("1", 2)

        with self.assertRaises(TypeError):
            r8 = Rectangle(1, "2")

        with self.assertRaises(ValueError):
            r5 = Rectangle(-2, -10)

        r6 = Rectangle(2, 10, 0, 0, 12)

        with self.assertRaises(ValueError):
            r7 = Rectangle(2, 10, -1, 1, 12)

        with self.assertRaises(ValueError):
            r11 = Rectangle(2, 10, 1, -1, 12)

        with self.assertRaises(TypeError):
            r9 = Rectangle(2, 10, 1, "1", 12)

        with self.assertRaises(TypeError):
            r10 = Rectangle(2, 10, 1, "1", 12)


if __name__ == '__main__':
    unittest.main()
