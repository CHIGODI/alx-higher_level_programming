#!/usr/bin/python3
"""
test the x y in the display method
"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys
from models.base import Base


class TestRectangleDisplay(unittest.TestCase):
    def setUp(self):
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__
        Base._Base__nb_objects = 0

    def test_display(self):
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        expected_output_r1 = '\n\n  ##\n  ##\n  ##\n'
        self.assertEqual(sys.stdout.getvalue(), expected_output_r1)

        # clear previous caputired output
        sys.stdout.truncate(0)
        sys.stdout.seek(0)

        r2 = Rectangle(3, 2, 1)
        r2.display()
        expected_output_r2 = ' ###\n ###\n'
        self.assertEqual(sys.stdout.getvalue(), expected_output_r2)

        # clear previous caputired output
        sys.stdout.truncate(0)
        sys.stdout.seek(0)

        r3 = Rectangle(3, 2, 0, 1)
        r3.display()
        expected_output_r2 = '\n###\n###\n'
        self.assertEqual(sys.stdout.getvalue(), expected_output_r2)


if __name__ == '__main__':
    unittest.main()
