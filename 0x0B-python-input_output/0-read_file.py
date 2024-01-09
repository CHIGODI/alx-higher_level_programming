#!/usr/bin/python3
"""
This module contains code that opens a file and read from
it. prints what is read to stdout
"""


def read_file(filename=""):
    """
    opens a file to read and print contents to stdout
    """
    with open(filename, encoding="utf-8") as f:
        file_contents = f.read()
        print(file_contents, end='')
