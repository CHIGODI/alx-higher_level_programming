#!/usr/bin/python3
"""
Testing area method of rectangle class
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestArea(unittest.TestCase):
    """
    test area method
    """
    def tearDown(self):
        """
         Reset the __nb_objects attribute to its initial value after each
         test method
        """
        Base._Base__nb_objects = 0

    def test_area(self):
        """
        Tests the area method in the Rectangle class
        """
        r1 = Rectangle(3, 2)
        r2 = Rectangle(10, 2, 0, 0, 12)

        with self.assertRaises(ValueError):
            r3 = Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            r5 = Rectangle(1, -2)

        with self.assertRaises(TypeError):
            r4 = Rectangle("1", 2)

        with self.assertRaises(TypeError):
            r6 = Rectangle(1, "2")

        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)


if __name__ == '__main__':
    unittest.main()
