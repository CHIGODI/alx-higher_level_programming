#!/usr/bin/python3
"""
class Student that defines a student by:

Public instance attributes:
first_name
last_name
age
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        object constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        class to json
        """
        return self.__dict__
