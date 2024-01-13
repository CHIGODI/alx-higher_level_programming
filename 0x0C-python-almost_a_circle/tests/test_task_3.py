#!/usr/bin/python3
"""
Module containing task 2 testcases (First Rectangle)
"""

import unittest
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    """
    Test if the 'id' attribute is assigned correctly
    """
    def test_ractangle(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2.2, 10)
        r3 = Rectangle(0, 10)
        r4 = Rectangle("str", "str")
        r5 = Rectangle(-2, -10)
        r6 = Rectangle(2, 10, 0, 0, 12)
        r7 = Rectangle(2, 10, -1, -1, 12)

        self.assertEqual(r1.width, 10)
        self.assertRaises(TypeError, getattr, r2, 'width')
        self.assertRaises(ValueError, getattr, r3, 'width')
        self.assertRaises(TypeError, getattr, r4, 'width')
        self.assertRaises(ValueError, getattr, r5, 'width')
        self.assertRaises(ValueError, getattr, r7, 'x')


if __name__ == '__main__':
    unittest.main()
