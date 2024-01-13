#!/usr/bin/python3
"""
This is a Base Class
"""

import json


class Base:
    """
    Base class serves as a foundation for other classes.
    It provides functionality for JSON serialization and deserialization,
    as well as methods for creating instances from dictionaries and saving
    instances to a file.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialises an object with public attribute Id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON-formatted string.
        Returns an empty string '[]' if the input list is None or empty.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.
        Converts each object to a dictionary using the 'to_dictionary'
        method.
        """
        with open("Rectangle.json", mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                l1 = []
                for item in list_objs:
                    l1.append(item.to_dictionary())
            json.dump(l1, f)

    @classmethod
    def from_json_string(json_string):
        """
        Converts a JSON-formatted string to a list of dictionaries.
        Returns an empty list if the input string is None.
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of the class using the provided dictionary.
        The dictionary is expected to contain the necessary attributes
        for object creation.
        """
        dummy_class = cls(2, 2)
        dummy_class.update(**dictionary)
        return dummy_class

    @classmethod
    def load_from_file(cls):
        """
        Loads objects from a file and returns a list of instances.
        """
        # try to open file if it exists
        try:
            with open("Rectangle.json", mode="r", encoding="utf-8") as f:
                json_list_dicts = f.read()
        except FileNotFoundError:
            return []
        list_dicts = cls.from_json_string(json_list_dicts)
        return [cls.create(cls, **item) for item in list_dicts]
