#!/usr/bin/python3
"""
This module appends a string to a file
"""


def append_write(filename="", text=""):
    """
    appends text to a file
    Returns number of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        char_written = f.write(text)
    return char_written
