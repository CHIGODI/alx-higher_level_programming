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
            l1 = []
            if list_objs is None:
                f.write("[]")
            else:
                for item in list_objs:
                    l1.append(item.to_dictionary())
            json.dump(l1, f)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON-formatted string to a list of dictionaries.
        Returns an empty list if the input string is None.
        """
        if not json_string:
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

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Loads objects from a file and returns a list of instances.
        """
        # try to open file if it exists
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                content = f.read()
                list_dicts = cls.from_json_string(content)
                instances = [cls.create(**d) for d in list_dicts]
                return instances
        except FileNotFoundError:
            return []
