#!/usr.bin/python3
"""
test update method in Rectangle class
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleUpdate(unittest.TestCase):
    """
    """
    def tearDown(self):
        """
        Reset the __nb_objects attribute to its initial value after each
        test method
        """
        Base._Base__nb_objects = 0

    def test_update_method_with_args(self):
        """
        testing the update method given args
        """
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                         (5, 1, 2, 3, 4))

        r.update(10, 20, 30, 40, 50)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                         (10, 20, 30, 40, 50))

        r.update(100, 200)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                         (100, 200, 30, 40, 50))

if __name__ == '__main__':
    unittest.main()
