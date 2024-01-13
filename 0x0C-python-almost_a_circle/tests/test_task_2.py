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
    def test_ractangle(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(2, 10)

        self.assertIsInstance(r1, Base)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, 3)


if __name__ == '__main__':
    unittest.main()
