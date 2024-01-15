#!/usr/bin/python3
"""
testing update Rectangle method
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleUpdate(unittest.TestCase):
    """
    testing update method with *args
    """
    def tearDown(self):
        """
        Reset the __nb_objects attribute to its initial value after each
        test method
        """
        Base._Base__nb_objects = 0

    def test_update_method_with_kwargs(self):
        """
        tests if args updates attributes
        """
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (5, 1, 2, 3, 4))
        r.update(width=20, height=30, x=40, y=50)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                         (5, 20, 30, 40, 50))

        r.update(id=100, height=200)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                         (100, 20, 200, 40, 50))


if __name__ == '__main__':
    unittest.main()
