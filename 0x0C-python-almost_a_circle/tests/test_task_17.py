#!/usr/bin/python3
"""
Tets the from_json_string method in the base class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseFromJsonString(unittest.TestCase):
    """
    """
    def test_from_json_string_empty(self):
        """
        """
        result = Rectangle.from_json_string(None)
        self.assertEqual(result, [])
        result = Rectangle.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string(self):
        """
        """
        json_string = '[{"id": 1, "width": 2, "height": 3}, {"id": 2, "width":4, "height": 5}]'
        result = Rectangle.from_json_string(json_string)
        expected = [{"id": 1, "width": 2, "height": 3}, {"id": 2, "width": 4, "height": 5}]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
