#!/usr/bin/python3

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestBaseSaveToFile(unittest.TestCase):
    def tearDown(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
            Base._Base__nb_objects = 0

    def test_save_to_file_empty(self):
        Base.save_to_file(None)
        self.assertTrue(os.path.exists("Base.json"))
        filename = 'Base.json'
        with open(filename, mode='r', encoding='utf-8') as f:
            result = f.read()

        self.assertEqual(result, '[]')

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        filename = 'Rectangle.json'
        with open(filename, mode='r', encoding='utf-8') as f:
            result = json.load(f)

        self.assertTrue(os.path.exists("Rectangle.json"))
        self.assertEqual(result, [{"y": 8, "x": 2, "id": 1, "width": 10,"height"
                                   : 7}, {"y": 0, "x": 0, "id": 2, "width": 2,
                                          "height": 4}])
    def test_save_to_file_square(self):
        s1 = Square(10, 2, 8)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        filename = 'Square.json'
        with open(filename, mode='r', encoding='utf-8') as f:
            result = json.load(f)

        self.assertTrue(os.path.exists("Square.json"))
        self.assertEqual(result, [{"id": 1, "size": 10, "x": 2, "y": 8},
                                  {"id": 2, "size": 2, "x": 0, "y": 0}])

if __name__ == '__main__':
    unittest.main()
