#!/usr/bin/python3
"""
creates an object from a JSON file
"""

import json


def load_from_json_file(filename):
    """
    deserialises a JSON string to an object
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
