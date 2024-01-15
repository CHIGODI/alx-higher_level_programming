#!/usr/bin/python3
"""
Test the __str__ method
"""

import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys
from models.base import Base


class TestStr(unittest.TestCase):
    """
    """
    def tearDown(self):
        """
        Reset the __nb_objects attribute to its initial value after
        each test method
        """
        Base._Base__nb_objects = 0

    def test_str_method(self):
        """
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        output = StringIO()
        sys.stdout = output
        print(r1)
        print(r2)

        result = output.getvalue()
        sys.stdout = sys.__stdout__

        self.assertEqual(result, '[Rectangle] (12) 2/1 - 4/6\n'
                                 '[Rectangle] (1) 1/0 - 5/5\n')
