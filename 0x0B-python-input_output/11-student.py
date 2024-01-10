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

    def to_json(self, attrs=None):
        """
        class to json
        """
        if attrs is None:
            return self.__dict__
        else:
            store = self.__dict__
            result = {key: store[key] for key in attrs if key in store}
            return result

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance:
        """

        for key, value in json.items():
            setattr(self, key, value)
