#!/usr/bin/python3
"""
this module contains code that write a file
"""


def write_file(filename="", text=""):
    """
    opens a file with 'w' mode and writes into it
    Returns number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        char_written = f.write(text)
    return char_written
