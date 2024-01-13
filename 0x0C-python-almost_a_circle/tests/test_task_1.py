#!/usr/bin/python3
"""
This module contains tests for task_1 (Base Class)
"""

import unittest
from models.base import Base

class TestClassAttr(unittest.TestCase):
    """
    Test cases for Base class attributes
    """

    def test_class_init(self):
        """
        Test the id attribute of the Base class
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)


if __name__ == "__main__":
    unittest.main()
