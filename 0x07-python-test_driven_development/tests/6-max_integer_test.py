#!/usr/bin/python3
import sys
sys.path.append('..')
import unittest
max_integer = __import__("6-max_integer").max_integer
""" max integer testing module """

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([5,6,4,7,2]), 7)
        self.assertEqual(max_integer([-5,-6,-4,-7,-2]), -2)
        self.assertEqual(max_integer([5,6,4,-7,-2]), 6)
        self.assertEqual(max_integer(['a','b','c','d']), 'd')
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([None]), None)
        self.assertRaises(TypeError, max_integer, [2,3,4],[1,2,3])
        

if __name__ == '__main__':
    unittest.main()
