#!/usr/bin/python3
import json
"""
serialises an object to string
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
