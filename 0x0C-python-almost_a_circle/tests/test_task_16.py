#!/usr/bin/python3

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
import json


class TestBaseSaveToFile(unittest.TestCase):
    def tearDown(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

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

if __name__ == '__main__':
    unittest.main()
