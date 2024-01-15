#!/usr/bin/python3
"""
Tests the to dictioanry method
"""
import unittest
from models.square import Square
from models.base import Base


class TestSquareToDictionary(unittest.TestCase):
    def test_to_dictionary(self):
        s = Square(15, 3, 5, 1)
        expected_dict = {'id': 1, 'size': 15, 'x': 3, 'y': 5}
        self.assertEqual(s.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
