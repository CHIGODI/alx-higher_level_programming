#!/usr/bin/python3
"""
"""

from io import StringIO
import unittest
from models.rectangle import Rectangle
import sys
from models.base import Base


class TestDisplay(unittest.TestCase):
    """
    """
    def tearDown(self):
      """
      Reset the __nb_objects attribute to its initial value after each
      test method
      """
      Base._Base__nb_objects = 0

    def test_display(self):
        """
        Testing the display method without x, y
        """
        r1 = Rectangle(4, 6)

        #redirect stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        r1.display()
        printed_output = captured_output.getvalue()

        sys.stdout = sys.__stdout__

        expected_pattern = '####\n####\n####\n####\n####\n####\n'

        self.assertEqual(printed_output, expected_pattern)


if __name__ == '__main__':
    unittest.main()
