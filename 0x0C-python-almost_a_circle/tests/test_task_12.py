#!/usr/bin/python3
"""
"""
import unittest
from models.square import Square
from models.base import Base

class TestSquareUpdate(unittest.TestCase):
    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_update_with_args(self):
        s = Square(5)
        s.update(10, 20, 30, 40)
        self.assertEqual((s.id, s.size, s.x, s.y), (10, 20, 30, 40))

    def test_update_with_kwargs(self):
        s = Square(5)
        s.update(size=10, x=20, y=30)
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 10, 20, 30))

    def test_update_with_args_and_kwargs(self):
        s = Square(5)
        s.update(id=10, size=20, x=30, y=40)
        self.assertEqual((s.id, s.size, s.x, s.y), (10, 20, 30, 40))

if __name__ == '__main__':
    unittest.main()
