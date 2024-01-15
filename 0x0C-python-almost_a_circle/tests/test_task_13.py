#!/usr/bin/python3
"""
Tests the to dictioanry method
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleToDictionary(unittest.TestCase):
    """
    """
    def tearDown(self):
        """
        return nb onject to 0 after every test
        """
        Base._Base__nb_objects = 0

    def test_to_dictionary(self):
        """
        Tests the to dictionary method
        """
        r = Rectangle(10, 20, 5, 10, 1)
        expected_dict = {'id': 1, 'width': 10, 'height': 20, 'x': 5, 'y': 10}
        self.assertEqual(r.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
