#!/usr/bin/python3
"""
"""

import unittest
from models.base import Base


class TestBaseToJsonString(unittest.TestCase):
    """
    """
    def test_to_json_string_empty(self):
        """
        """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        """
        """
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string(self):
        """
        """
        data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        result = Base.to_json_string(data)
        expected_result = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
